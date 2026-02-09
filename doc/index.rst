.. Orange County Lettings documentation master file, created by
   sphinx-quickstart on Sat Feb  7 16:34:38 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Orange County Lettings documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Description
-----------

Orange County Lettings is a lettings application developed as a study project.
The goal of the project was to put in place a functional CI/CD pipeline with automatic site deployment.
The website itself presents a simple website listing user accounts and fictional lettings.

Orange County Lettings is divided into three Django applications:
- oc_lettings_site
- lettings
- profiles

Installation
------------

To install this project on your local machine:
1. Import the GitHub repository:

   .. code-block:: bash

      git clone https://github.com/Dakimen/P13_Lettings

2. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv

3. Activate your virtual environment:

   .. code-block:: bash

      venv\Scripts\Activate # On Windows
      # Or
      source venv/bin/activate # On Linux

4. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

5. Create a .env file at the project root and include in it:

   .. code-block:: env

      SENTRY_DSN = Your Sentry DSN
      SECRET_KEY = Your Django Secret Key

6. Launch the application locally:

   .. code-block:: bash

      python manage.py runserver

7. Open **http://localhost:8000** in your browser of choice.

Quick Start
-----------

To quickly run the project locally:

1. Clone the repository
2. Install dependencies
3. Run the development server

   .. code-block:: bash

      git clone https://github.com/Dakimen/P13_Lettings
      cd P13_Lettings
      python -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
      python manage.py runserver

Open http://localhost:8000 in your browser.

Technologies Stack
------------------

This application uses:

- Python 3.8
- SQLite3 for the database
- Django 3.0
- Docker
- Yandex Cloud Services for deployment
- Sentry
- HTML5
- CSS3
- JavaScript

Database
--------

Orange County Lettings uses SQLite3 to store its data locally.
The database consists of four main entities.

- User - Django default User model

- Profile:
   - user - One-To-One field to User object
   - favorite_city - CharField containing profile's favorite city.

- Address:
   - number - PositiveIntegerField building number
   - street - Charfield street name
   - city - Charfield city name
   - state = Charfield 2-letter state code
   - zip_code - PositiveIntegerField zip code
   - country_iso_code - CharField 3-letter country code

- Letting:
   - title - CharField letting title
   - address = One-To-One field to Address object

Model Relationships
~~~~~~~~~~~~~~~~~~~
- Each Profile is linked to exactly one User (one-to-one relationship).
- Each Letting is linked to exactly one Address (one-to-one relationship).
- Deleting a User or Letting cascades deletion to the related model.

Programming interface
---------------------
This application exposes web interfaces through Django views.

Main routes include:

- `/` – Home page
- `/lettings/` – List of available lettings
- `/lettings/<id>/` – Letting detail page
- `/profiles/` – List of user profiles
- `/profiles/<username>/` – User profile detail page

The Django Admin interface is available at:

- `/admin/`

These interfaces are intended for web usage only; no public REST API is exposed.

Use Cases
---------
Use Case 1: Browse lettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A visitor can access the home page and browse available lettings.  
Clicking on a letting displays detailed address information.

Use Case 2: View user profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Users can view profiles showing usernames and favorite cities.

Use Case 3: Administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Administrators can manage users, profiles, addresses, and lettings via the Django Admin interface.

Deployment
----------

To deploy this application, you will need the following:

- Sentry account with a personal DSN
- DockerHub account
- Yandex Cloud account
- Yandex Cloud CLI installed
- GitHub account
- Yandex Cloud Service Account

1. Configure your Yandex Cloud Service Account

   Assign Cloud-level permissions to your account:

   - ``editor``
   - ``viewer``

   Assign other permissions:

   - ``container-registry.images.puller``
   - ``lockbox.payloadViewer``
   - ``kms.keys.encrypterDecrypter``

2. Create your Yandex Lockbox Secret

   During creation:

   1. Select **User Secret** Type
   2. Add key-value pairs:

      - ``SENTRY_DSN`` — your Sentry DSN
      - ``DJANGO_SECRET_KEY`` — your Django secret key

   Click **Create**.

3. Create your Yandex Cloud Container Registry named **orange-lettings**

4. Create your Yandex Cloud Serverless Container
   Note: Your Service Account should have **functions.admin** permission in your Serverless Container.

5. Generate Service Account Key

Replace ``<SA_ID>`` with your Service Account ID.

   .. code-block:: bash

      yc iam key create --service-account-id <SA_ID> --output sa-key.json

.. warning::

   Be careful **not** to commit or push the generated service account key
   to your GitHub repository.

6. Add GitHub Actions secrets

   Add the following values to your GitHub repository secrets:

   - ``CONTAINER_ID`` — ID of your Serverless Container
   - ``DOCKERHUB_TOKEN`` — DockerHub access token
   - ``DOCKERHUB_USERNAME`` — your DockerHub username
   - ``LOCKBOX_SECRET_ID`` — ID of your Lockbox secret
   - ``SA_ID`` — Service Account ID
   - ``DJANGO_SECRET_KEY`` — Django secret key
   - ``YANDEX_CLOUD_ID`` — Yandex Cloud ID
   - ``YANDEX_CR`` — ``cr.yandex/<ContainerRegistryID>``
   - ``YANDEX_FOLDER_ID`` — Folder hosting your services
   - ``YANDEX_SA_KEY`` — Full JSON key generated earlier

7. Deploy

   Commit and push to the ``master`` branch to trigger the CI/CD pipeline:

   - CI runs tests and linting
   - CD builds Docker images and pushes them to DockerHub and Yandex Cloud
   - Deployment creates a new Serverless Container revision

   Make sure the revision is set to **Public** in Yandex Cloud so the
   application is accessible via the generated URL.

Application Management
----------------------

Monitoring and Error Tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The application uses Sentry to monitor runtime errors and exceptions.

Configuration is handled via the `SENTRY_DSN` environment variable.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~
Sensitive configuration values are stored securely using Yandex Lockbox
and injected at deployment time.

Updating the Application
~~~~~~~~~~~~~~~~~~~~~~~~
Any push to the `master` branch triggers the CI/CD pipeline, which:

- Runs automated tests and verifies linting
- Builds Docker images
- Deploys a new serverless container revision

Any push or pull request to any other branch only triggers the CI part of the pipeline, which:

- Runs automated tests
- Verifies linting

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
