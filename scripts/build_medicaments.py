#!/usr/bin/env python3
"""Construit medicaments.json (code CIP13 -> nom du médicament) à partir de la
Base de données publique des médicaments (ANSM / ministère de la Santé, France).

Usage : python3 scripts/build_medicaments.py [dossier_des_fichiers_txt]
Sans argument, télécharge CIS_bdpm.txt et CIS_CIP_bdpm.txt.
"""
import json, os, sys, urllib.request

BASES = [
    "https://base-donnees-publique.medicaments.gouv.fr/download/file/{f}",
    "https://base-donnees-publique.medicaments.gouv.fr/telechargement.php?fichier={f}",
]

def lire(nom, dossier):
    if dossier:
        data = open(os.path.join(dossier, nom), "rb").read()
    else:
        data, err = None, None
        for b in BASES:
            try:
                req = urllib.request.Request(b.format(f=nom), headers={"User-Agent": "Mozilla/5.0 (Wergui SN demo)"})
                data = urllib.request.urlopen(req, timeout=120).read()
                if len(data) > 10000 and b"<html" not in data[:500].lower():
                    break
                data = None
            except Exception as e:
                err = e
        if data is None:
            sys.exit(f"Téléchargement impossible : {nom} ({err})")
    try:
        txt = data.decode("utf-8")
    except UnicodeDecodeError:
        txt = data.decode("latin-1")
    return [l.split("\t") for l in txt.splitlines() if l.strip()]

def main():
    dossier = sys.argv[1] if len(sys.argv) > 1 else None
    cis = {}
    for c in lire("CIS_bdpm.txt", dossier):
        if len(c) >= 3:
            cis[c[0].strip()] = (c[1].strip(), c[2].strip())  # dénomination, forme
    out = {}
    for c in lire("CIS_CIP_bdpm.txt", dossier):
        if len(c) < 7:
            continue
        code, cip13, pres = c[0].strip(), c[6].strip(), c[2].strip()
        if not cip13.isdigit() or len(cip13) != 13 or code not in cis:
            continue
        den, forme = cis[code]
        nom = den.split(",")[0].strip()
        out[cip13] = [nom, forme, pres]
    if len(out) < 1000 and not dossier:
        sys.exit(f"Base trop petite ({len(out)} présentations) : téléchargement suspect.")
    with open("medicaments.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(f"medicaments.json : {len(out)} présentations, {os.path.getsize('medicaments.json')//1024} Ko")

if __name__ == "__main__":
    main()
