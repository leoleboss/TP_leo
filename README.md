# TD - Financial Reporting

## Contexte

Vous travaillez pour une institution financière qui gère un portefeuille de clients particuliers (PP) et professionnels (PM). Chaque client est associé à un score de risque (`score`) et un score précédent (`score_prev`), permettant de suivre l'évolution de son profil.

Le champ `drc_complet` indique si le dossier réglementaire du client est complet. L'`id_agent` identifie l'action d'un conseiller sur le profil du client.

L'objectif de ce TD est de produire automatiquement un rapport Excel de suivi à partir de ces données brutes.

## Démarrage

### 1. Créez votre dépôt depuis le template

Cliquez sur **Use this template** → **Create a new repository**

> Donnez-lui un nom explicite, ex: `td-reporting-<votre-prenom>`

### 2. Clonez votre dépôt

```bash
git clone https://github.com/<votre-username>/<nom-du-repo>.git
cd <nom-du-repo>
```

## Données

Les données sont disponibles ici :
```
https://minio.lab.sspcloud.fr/fabienhos/td-reporting-financial/financial_data.parquet
```

## Partie 1 — Exploration dans le notebook

Commencez par `notebook.ipynb`. Cette partie est intentionnellement libre : 
c'est un espace d'expérimentation pour forger vos intuitions.

## Partie 2 — Structuration en projet `Python flat`

Une fois l'exploration terminée et votre logique validée dans le notebook, 
vous allez **restructurer votre code en projet Python propre**.

### Pourquoi cette étape ?

Un notebook est pratique pour explorer, mais difficile à maintenir, tester et 
déployer. L'objectif est de transformer votre code en modules réutilisables.

### Structure cible potentielle

```
<projet>/
├── src/
│   └── <projet>/
│       ├── __init__.py
│       ├── data.py        
│       ├── indicators.py
│       └── report.py
├── template/
│   └── template_reporting.xlsx
├── main.py                  # Point d'entrée
├── pyproject.toml
└── README.md
```

### Point d'entrée

`main.py` doit pouvoir s'exécuter en une commande :

```bash
uv run main.py
```

Et produire le fichier Excel final sans intervention manuelle.

### Conseils de migration notebook → scripts

- Chaque cellule qui *fait quelque chose* devient une **fonction**
- Chaque fonction va dans le module qui correspond à sa responsabilité
- Le notebook peut rester comme documentation / démonstration

## Objectifs pédagogiques

- Lire des données au format Parquet
- Explorer et nettoyer un DataFrame
- Générer un rapport Excel avec `openpyxl` et `pandas`
- Structurer son code et sa pensée.
- Passer d'un notebook exploratoire à un **projet Python structuré et exécutable**
