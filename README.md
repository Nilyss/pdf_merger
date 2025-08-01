# PDF Merger

Un outil simple pour fusionner plusieurs fichiers PDF en un seul.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

1. Placez vos fichiers PDF dans le dossier `source/`
2. Exécutez le script:

```bash
python merge_pdfs.py
```

Le fichier fusionné sera créé dans le dossier `output/` sous le nom `merged.pdf`.

### Options avancées

```bash
python merge_pdfs.py [dossier_source] [dossier_sortie] [nom_fichier_sortie]
```

Exemple:
```bash
python merge_pdfs.py mes_pdfs resultat mon_fichier_fusionne.pdf
```

## Structure du projet

```
pdf-merger/
├── source/          # Placez vos PDF ici
├── output/          # Les PDF fusionnés apparaîtront ici
├── merge_pdfs.py    # Script principal
├── requirements.txt # Dépendances
└── README.md       # Ce fichier
```