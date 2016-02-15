
# On a Mac with Mavericks

## Making sure you have Python

Since some 3rd party modules may require Python 2, so
for the moment, let's stick with Python 2.

To make sure it is installed on your Mac:

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

Follow the instructions on http://virtualenvwrapper.readthedocs.org/en/latest/install.html

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

    
