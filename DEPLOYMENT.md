# Deployment

## Table of Contents

- [Deployment](#deployment)
- [Create repository](#create-repository)
- [Cloning](#cloning-a-github-repository)
- [Creating project and app](#creating-project-and-app)
- [Create Heroku app and connect your repository](#create-heroku-app-and-connect-your-repository)

---

To deploy the repository on Heroku I followed these steps:

## Create repository

To create a new repository I used the following link [Template to crete a new repository](https://github.com/Code-Institute-Org/ci-full-template)
then cloned the repository

## Cloning a GitHub Repository

1. Open your terminal or command prompt on your local machine.

1. Navigate to the directory where you want to clone the repository using the `cd` command.

   ```bash
   cd path/to/your/directory
   ```

1. Go to the GitHub repository you want to clone.
1. Click on the "Code" button on the repository page.
1. Copy the URL provided (either HTTPS or SSH).
1. In your terminal, use the git clone command followed by the copied URL.

    For HTTPS:

    ```bash
    git clone https://github.com/username/repository.git
    ```

    For SSH

    ```bash
    git clone git@github.com:username/repository.git
    ```

    Replace the URL with the one you copied.

1. Press Enter, and Git will clone the repository to your local machine.

## Creating project and app

1. Create a virtual environment:

    ```bash
    python -m venv .venv
    ```

1. Install Django v5.0

    ```bash
     pip install django 
    ```

1. Install psycopg2 v2.9.9

   ```bash
     pip install psycopg2
   ```

1. Create a new Django project

   ```bash
    django-admin startproject my_project 
   ```

1. Create file `env.py` and add:

    ```python
    import os

    os.environ["LOCALHOST"] = "my ip address"
    ```

1. In `settings.py` add:

   ```python
   ALLOWED_HOSTS = [os.environ.get('LOCALHOST')]
   ```

1. Run the following command:

    ```python
    python manage.py startapp my_app
    ```

1. In settings.py add my app in the INSTALLED_APPS section

### Create Heroku App and connect your repository

1. On the Heroku dashboard select create a new app

1. In settings select config var and add a key of `DISABLE_COLLECTSTATIC` and a value of `1` and click Add.

1. On your platform/device where the repo is cloned Install gunicorn v21.2.0:

   ```bash
     pip install gunicorn
   ```

1. List all of your requirements in requirements.txt:

    ```bash
     pip3 freeze --local > requirements.txt
   ```

1. Create a file named Procfile at the root directory of the project

1. In the Procfile add:

    ```python
    web: gunicorn my_project.wsgi
    ```

1. In settings.py add `.herokuapp.com` to allowed hosts:

    ```python
    ALLOWED_HOSTS = ['.herokuapp.com', os.environ.get('LOCALHOST'),]
    ```

1. Push your updated code to the github repo

1. On The Heroku website, select dashboard, myapp, then Deploy

1. In the Deployment method section enable GitHub integration by clicking on Connect to GitHub and add your repo name

1. Click on Deploy Branch

1. Then select open app

---

Back to [README.md](./README.md)
