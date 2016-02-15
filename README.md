
# On a Mac with Mavericks

## Making sure you have Python

Since some 3rd party modules may not work with Python 3 and require Python 2, so
for the moment, let's stick with Python 2.

Python is pre-installed on Macs. To see it:

    $ python --version
    Python 2.7.5

## Install pip, by going to

https://pip.pypa.io/en/latest/installing/#do-i-need-to-install-pip

get

https://bootstrap.pypa.io/get-pip.py

now run

    $ sudo python get-pip.py

and now if you check that pip is installed:

    $ pip --version
    pip 8.0.2 from /Library/Python/2.7/site-packages (python 2.7)

## Now install virtualenv

The webpage is at http://virtualenv.readthedocs.org/en/latest/installation.html

To install on Mac:

    $ sudo pip install virtualenv

Checking it is installed:

    $ virtualenv --version
    14.0.6


## Install virtualenvwrapper

virtualenvwrapper makes it easier to use, than using virtualenv alone.

To install, follow the instructions on http://virtualenvwrapper.readthedocs.org/en/latest/install.html

Essentially, it is

    $ sudo pip install virtualenvwrapper

and adding these lines to your ~/.profile or ~/.bashrc

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

## So now you have "workon", due to virtualenvwrapper

Restart your bash.  This is important.

Now you can use workon, which gives you an empty list

    $ workon
    $             # <-- nothing is printed

Now you can create a virtual environment and go into it:

    $ mkvirtualenv django19try01
    New python executable in /Users/pyay/.virtualenvs/django19try01/bin/python
    Installing setuptools, pip, wheel...done.

Note that now, the prompt in Bash has the environment "(django19try01)" at the very beginning:

    (django19try01) $

and if we type workon, then it will show the list of environments we have:    

    (django19try01) $ workon
    django19try01   

### Create one more virtual environment:

    (django19try01) $ mkvirtualenv django19try02
    New python executable in /Users/pyay/.virtualenvs/django19try02/bin/python
    Installing setuptools, pip, wheel...done.

    (django19try02) $

Note that the prompt shows that we are in the environment "django19try02".

and listing the environments will show:

    (django19try02) $ workon
    django19try01
    django19try02

### To switch to another environment:

    (django19try02) $ workon django19try01
    (django19try01) $

Note that the prompt changed, indicating we are now in "django19try01".

## Now install Django:

Note that since we have virtual environments, any pip commands we do, we do not need
to preceed it with a "sudo".

So, to install Django:

    (django19try01) $ pip install Django
    Collecting Django
    # ...
      Downloading Django-1.9.2-py2.py3-none-any.whl (6.6MB)
        100% |████████████████████████████████| 6.6MB 74kB/s
    Installing collected packages: Django
    Successfully installed Django-1.9.2
    (django19try01) $

 So we see, Django 1.9.2 was installed.  

 If we want to install a particular version of Django, it is:

     $ pip install Django==1.9.2

## Now, you can start using Django

And the place to look at is: https://docs.djangoproject.com/en/1.9/intro/

### To make sure Django is installed:

    $ python
    >>> import django
    >>> django.get_version()
    '1.9.2'

## Create a new Django Project

More info is on https://docs.djangoproject.com/en/1.9/intro/tutorial01/

To create a new Django project:

    $ django-admin startproject mysite

Note that the above command will create a folder with a bunch of files in it.
I tend to use git to track what files are created in each phase of the project,
so at this point, I may

    $ cd mysite
    $ git init
    $ git add .
    $ git commit -am "initial Django 1.9 Project"

and you can git push to your github or gitlab account if you want.

## Starting your website:

    $ cd mysite    # if you are not already in it
    $ python manage.py runserver

Now go to your web browser, and type in

> http://127.0.0.1:8000/

and you will see your website running.

## Running a database migration

When you start the web server, Django will tell you:

    You have unapplied migrations; your app may not work properly until they are applied.
    Run 'python manage.py migrate' to apply them.

So to migrate:

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, contenttypes, auth, sessions
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying sessions.0001_initial... OK

Now at this point, the sqlite database has been updated, as seen by git status:

    $ git st
    On branch master
    Your branch is up-to-date with 'origin/master'.
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

    	modified:   db.sqlite3

    no changes added to commit (use "git add" and/or "git commit -a")

## Creating an "app" in the "project"

From now on, we will follow https://docs.djangoproject.com/en/1.9/intro/tutorial01/

You can read that page and move on, or read the summary below:

We already had a project, and a project is a collection of "apps".

To create an app call "polls":

    $ python manage.py startapp polls

Now make polls/views.py contain the following:

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")

Create a file polls/urls.py and make it  contain the following:

    from django.conf.urls import url

    from . import views

    urlpatterns = [
        url(r'^$', views.index, name='index'),
    ]     

And finally, edit mysite/urls.py to make it:

    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        url(r'^polls/', include('polls.urls')),
        url(r'^admin/', admin.site.urls),
    ]       

Note that there is a "include" added to the first line, if compared to the
original file that Django created.

Now when you run the server:

    $ python manage.py runserver    

and go to

> http://127.0.0.1:8000/polls/

You will see your polls main page loaded in your browser.

## Adding data and playing with the Django shell

Now you can go to https://docs.djangoproject.com/en/1.9/intro/tutorial02/

Just that before you define the instance method `__str__` for the Question
class, you actually can see all objects this way:

    >>> [vars(obj) for obj in Question.objects.all()]
    [{'pub_date': datetime.datetime(2016, 2, 15, 7, 2, 44, 743849, tzinfo=<UTC>), 'question_text': u"What's new?", '_state': <django.db.models.base.ModelState object at 0x1088f6810>, 'id': 1}]
