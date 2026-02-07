## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- Compte Sentry

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Installer les dépendances

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`

#### Créer un fichier d'environnement

- Créez un nouveau fichier .env dans la racine du projet.
- Dans ce fichier insérez:
- `SENTRY_DSN = # votre DSN Sentry ici`
- `DJANGO_SECRET_KEY = # votre DJANGO SECRET KEY ici`

#### Exécuter le site

- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Cette application est déployée automatiquement grâce à une pipeline CI/CD basée sur GitHub Actions, Docker et Yandex Cloud Serverless Containers.

### Vue d’ensemble du déploiement

Le déploiement fonctionne de la manière suivante :

- Chaque modification poussée sur la branche `master` déclenche une pipeline CI/CD.
- La partie **CI** exécute les tests unitaires et vérifie le linting du code.
- Si la CI est validée, la partie **CD** :
  - construit une image Docker de l’application,
  - pousse l’image vers DockerHub et le registre de conteneurs Yandex Cloud,
  - déploie une nouvelle révision du conteneur serverless sur Yandex Cloud.
- Une fois la révision déployée et rendue publique, l’application devient accessible via l’URL fournie par Yandex Cloud.

Les erreurs et exceptions en production sont surveillées via Sentry.

---

### Configuration requise pour le déploiement

Pour que le déploiement fonctionne correctement, les éléments suivants sont nécessaires :

- Un compte **GitHub** avec accès au repository
- Un compte **DockerHub**
- Un compte **Yandex Cloud**
- Un **Service Account Yandex Cloud** avec les permissions suivantes :
  - `editor`, `viewer`
  - `container-registry.images.puller`
  - `lockbox.payloadViewer`
  - `kms.keys.encrypterDecrypter`
- Un compte **Sentry** avec un DSN valide
- L’outil **Yandex Cloud CLI (`yc`)** installé localement
- Un secret **Yandex Lockbox** contenant :
  - `SENTRY_DSN`
  - `DJANGO_SECRET_KEY`

---

### Procédure de déploiement

1. **Configurer le Service Account Yandex Cloud**
   - Créer un Service Account.
   - Lui attribuer les permissions listées ci-dessus.

2. **Créer un secret Yandex Lockbox**
   - Type : _User secret_
   - Ajouter les clés :
     - `SENTRY_DSN`
     - `DJANGO_SECRET_KEY`

3. **Créer un Container Registry Yandex Cloud**
   - Nom requis : `orange-lettings`

4. **Créer un Serverless Container**
   - Associer le Service Account au conteneur.

5. **Générer une clé pour le Service Account**
   ```bash
   yc iam key create --service-account-id <SA_ID> --output sa-key.json
   ```

- Ne jamais versionner ce fichier dans le repository.

6. **Configurer les secrets GitHub Actions**

- Ajouter les variables suivantes dans Settings → Secrets and variables → Actions :

- CONTAINER_ID
- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN
- LOCKBOX_SECRET_ID
- SA_ID - ID du Compte Service Yandex
- DJANGO_SECRET_KEY
- YANDEX_CLOUD_ID
- YANDEX_FOLDER_ID
- YANDEX_CR - doit avoir la forme de cr.yandex/ID de votre Container Registry
- YANDEX_SA_KEY (contenu JSON complet du fichier généré)

7. Lancer le déploiement

- Pousser les changements sur la branche master.

- GitHub Actions déclenche automatiquement la pipeline CI/CD.

- Une fois le déploiement terminé, vérifier que la révision du conteneur est définie comme publique dans Yandex Cloud.

### Mise à jour de l’application

- Toute modification poussée sur master redéploie automatiquement l’application.

- Les autres branches déclenchent uniquement la CI (tests et linting).

- Aucun déploiement manuel n’est nécessaire.

### Supervision et maintenance

- Les erreurs en production sont remontées dans Sentry.
- Les variables sensibles sont stockées dans Yandex Lockbox.
- Les logs et l’état du déploiement peuvent être consultés depuis :
  - GitHub Actions
  - Yandex Cloud Console
