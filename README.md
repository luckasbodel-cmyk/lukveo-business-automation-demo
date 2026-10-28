# LUKVEO Business Automation — démonstration Python / SQLite

Extraits de code issus du **prototype personnel** LUKVEO AI PRO, adaptés pour être exécutés hors du PC de développement. Le projet ne prospecte personne et n’envoie **aucun email**.

## Fonctionnalités démontrées

- `api/business_autopilot.py` : base locale SQLite, création et consultation de fiches `prospect`, `produit` et `opportunite` ; validation des champs.
- `api/prospect_qualification.py` : sélection prudente d’une prestation depuis un catalogue contrôlé, brouillon de proposition, stockage d’une validation explicite en SQLite.
- `core/fast_brain.py` : **substitut de démonstration** ; le moteur IA privé original n’est **pas** fourni. La branche `qualification` qui fait appel à l’IA n’est donc pas opérationnelle dans cette publication.
- `samples/OFFRES_LUKVEO.md` : **catalogue fictif** d’exemple ; le fichier original privé n’est pas publié.

## Lancer une démo sans clé ni réseau

```bash
python demo_local.py
```

Le script utilise uniquement une entreprise **fictive** et une base SQLite temporaire ; il ne transmet aucune donnée.

## Adaptations depuis le code source

- Remplacement du chemin Windows vers le catalogue privé par un fichier d’exemple inclus dans ce dépôt.
- Remplacement de la dépendance `core.fast_brain` par un adaptateur qui signale explicitement l’absence du moteur IA.
- Aucune modification des scripts originaux dans `C:\LUKVEO_DEV`.

## Limites

Ces exemples sont des modules de travail en cours, pas une application SaaS ni une preuve de déploiement commercial. Avant mise en production : tests de sécurité, gestion multi-utilisateurs, authentification, qualité des données, conformité RGPD et revue des messages commerciaux.

**Sécurité :** ne pas publier le vrai catalogue, les bases prospects, les clés API, fichiers `.env`, historiques ou dossiers de sauvegarde.
