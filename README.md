# Wergui SN – stock pharmacie (démo)

Prototype cliquable d'un logiciel de gestion de stock pour les pharmacies, en français, payé en Mobile Money.

- **Péremptions** : suivi par lot, alertes 90 jours avant, lots périmés bloqués à la caisse, « invendables prévus » selon le rythme des ventes, retour grossiste ou vente en priorité.
- **Caisse** : sortie des lots qui périment en premier (FEFO), espèces, Wave, Orange Money, tiers payant IPM/mutuelle.
- **Commandes** : suggestions par grossiste selon les ventes, le stock et le délai de livraison ; bon de commande par WhatsApp ; réception avec n° de lot et date.
- **Scanner** : photo ou caméra du téléphone. Le DataMatrix GS1 des boîtes remplit seul le produit, le n° de lot et la date de péremption (sans internet, sans IA). Codes-barres et QR codes aussi ; alerte si une boîte déjà scannée revient (double saisie ou contrefaçon).
- **Inventaire tournant**, rayon par rayon, sans fermer la pharmacie.
- **Abonnement** : 15 000 F/mois par pharmacie, payé par Wave, Orange Money ou Free Money.

Ouvrir `index.html` dans un navigateur, ou activer GitHub Pages (Settings → Pages → branche `main`, dossier racine).

Données d'exemple uniquement : rien n'est sauvegardé, envoyé ni payé.
