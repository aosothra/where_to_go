# where_to_go - See Moscow through Artyom's eyes!

This project constitutes a web application that provides photos and trivia about places of interest in city of Moscow.

As a User, you will be greeted by an interactive map with numerous markers representing places of interest. By clicking on these markers you will be provided with text trivia and set of photos related to the selected location. 

As an Administrator, you will be able to create/edit/delete those markers including corresponding data.

You can check the demo of the site [here](https://bakutso.pythonanywhere.com/)! (link may expire in the future)

The project is built upon [Django Web Framework](https://docs.djangoproject.com/en/4.0/)

## Basic installation

Make sure you have Python3 installed on your system.

It is strongly advised to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation.

After cloning this repository, you may use `pip` (or `pip3` to avoid conflict with Python2) to install dependencies.

```
pip install -r requirements.txt
```

### Environment setup

This project expects `.env` file in the root folder in order to set up the environment for development / production. So, make sure to create one.

Inside your `.env` file you can specify following settings for our Django project:

| Key | Type | Default (if optional) | Description |
| - | - | - | - |
| `SECRET_KEY` | `str` |  | A special token used to provide cryptographic signing. Must be set to a unique, unpredictable value. [(See Django doc)](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SECRET_KEY)
| `ALLOWED_HOSTS` | `list(str)` | `[]` | A list of strings representing the host/domain names that this Django site can serve. [(See Django doc)](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts)
| `DEBUG` | `bool` | `False` | A flag that specifies whether debug mode is on. Never deploy a site into production with DEBUG turned on! [(See Django doc)](https://docs.djangoproject.com/en/4.0/ref/settings/#debug)
| `MEDIA_ROOT` | `str` | `{path to your project}/media` | Absolute path to the directory that (in our case) stores uploaded images. [(See Django doc)](https://docs.djangoproject.com/en/4.0/ref/settings/#media-root)
| `STATIC_ROOT` | `str` | `{path to your project}/staticfiles` | The absolute path to the directory where collectstatic will collect static files for deployment. [(See Django doc)](https://docs.djangoproject.com/en/4.0/ref/settings/#static-root)
| `CSRF_COOKIE_SECURE` | `bool` | `True` | Security flag to control whether to use a secure cookie for the CSRF cookie. [(See Django doc)](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-cookie-secure)
| `SESSION_COOKIE_SECURE` | `bool` | `True` | Security flag to control whether to use a secure cookie for the session cookie. [(See Django doc)](https://docs.djangoproject.com/en/4.0/ref/settings/#session-cookie-secure)

For the purposes of development you can set up your `.env` file as follows:

```
SECRET_KEY = 'absolute-maximum-security-banana-tango-foxtrot'
DEBUG = True
```

### Creating and managing database

Once you've set up your environment, you may continue with database creation. In our project database is used to store data about our places of interest, as well as photos related to them.

Create at configure your database by running the following command:

```
python3 manage.py migrate
```

In order to access and populate the newly created database, you must register your admin credentials. Luckily, Django has a handy function to take care of that:

```
python3 manage.py createsuperuser
```

Once the procedure is done you may start your project:

```
python3 manage.py runserver
```

This will start a development server on http://127.0.0.1:8000. If you've followed the instructions correctly, by opening this link you ought to see an interactive map of Moscow. There is no data on it yet, as we have not created any.

For that, we shall use Django built-in admin application, which can be accessed over http://127.0.0.1:8000/admin/ using your previously provided admin credentials. 

Now you can access `Places` table editor to begin populating the database.

### `load_place` utility command

Adding places one-by-one from the very beginning may become quite cumbersome and tiring. To avoid that you may use special `load_place` command:

```
python3 manage.py load_place <url>
```

where URL must lead to a JSON file with following schema:

``` JavaScript
{
    "title": "New place title",
    "imgs": [
        "https://url.to/your/image.jpg",
        ...
    ],
    "description_short": "Short description of new place",
    "description_long": "Long description of new place (allows HTML for styling)",
    "coordinates": {
        "lng": "37.623191",
        "lat": "55.753989"
    }
}
```

## Basic Usage

If you haven't started your application yet, do it now:

```
python3 manage.py runserver
```

Go to http://127.0.0.1:8000

That's it!

## Project goals

This project was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.


