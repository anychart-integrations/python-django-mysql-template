[<img src="https://cdn.anychart.com/images/logo-transparent-segoe.png?2" width="234px" alt="AnyChart - Robust JavaScript/HTML5 Chart library for any project">](https://www.anychart.com)
# Python Django basic template
This example shows how to use Anychart library with the Python programming language, Django web framework and MySQL database.

## Running

To use this sample you must have Python 2.* installed (if not please visit [python download page](https://www.python.org/downloads/release/python-2712/)), PIP - Python package manager (if not please check [isntallation guide](https://pip.pypa.io/en/stable/installing/)) and
MySQL installed and running (if not please check out [MySQL download page](https://dev.mysql.com/downloads/installer/) and follow [instructions](http://dev.mysql.com/doc/refman/5.7/en/installing.html))

To check your installations, run the following command in the command line:
```
$ python --version
Python 2.7.6 # sample output
$ pip -V
pip 1.5.4 from /usr/lib/python2.7/dist-packages (python 2.7) # sample output
$ mysql --version
mysql  Ver 14.14 Distrib 5.5.52, for debian-linux-gnu (x86_64) using readline 6. # sample output
```

To start this example run commands listed below.

Clone the repository from github.com:
```
$ git clone git@github.com:anychart-integrations/python-django-mysql-template.git
```

Navigate to the repository folder:
```
$ cd python-django-mysql-template
```

Make sure you have installed Django and MySQL-python dependencies:
```
$ pip freeze
# sample output
...
Django==1.10.2
MySQL-python==1.2.5
...
```

if not, please, install them:
```
$ pip install MySQL-python

$ pip install django
```
For more details about installation see [Django installation guide](https://docs.djangoproject.com/es/1.10/topics/install/)

Set up MySQL database, use -u -p flags to provide username and password:
```
$  mysql < database_backup.sql
```

Run example:
```
$ python manage.py runserver 8000
```

Open browser at http://127.0.0.1:8000/

## Workspace
Your workspace should look like:
```
python-django-mysql-template/
    fruits/
            migrations/
                __init__.py
        static/
            css/
                style.css       # css style
        templates/
            fruits/
                index.html      # html template
        __init__.py
        admin.py
        apps.py
        models.py               # app's models
        test.py
        urls.py                 # app routes
        views.py                # app views
    python-django-mysql-template/
        __init__.py
        settings.py             # basic settings, including MySQL settings
        urls.py                 # project routes
        wsgi.py
    database_backup.sql         # MySQL database dump
    LICENSE
    manage.py                   # main Django script
    README.md

```
More about Django folder structure you can read [here](http://django-project-skeleton.readthedocs.io/en/latest/structure.html).

## Technologies
Language - [Python](https://www.python.org/)<br />
Web framework - [Django](https://www.djangoproject.com/)<br />
Database - [MySQL](https://www.mysql.com/)<br />


## Further Learning
* [Documentation](https://docs.anychart.com)
* [JavaScript API Reference](https://api.anychart.com)
* [Code Playground](https://playground.anychart.com)
* [Technical Support](https://www.anychart.com/support)

## License
AnyChart Python/Django/MySQL integration sample includes two parts:
- Code of the integration sample that allows to use Javascript library (in this case, AnyChart) with Python language, Django framework and MySQL database. You can use, edit, modify it, use it with other Javascript libraries without any restrictions. It is released under [Apache 2.0 License](https://github.com/anychart-integrations/python-django-mysql-template/blob/master/LICENSE).
- AnyChart JavaScript library. It is released under Commercial license. You can test this plugin with the trial version of AnyChart. Our trial version is not limited by time and doesn't contain any feature limitations. Check details [here](https://www.anychart.com/buy/).

If you have any questions regarding licensing - please contact us. <sales@anychart.com>
