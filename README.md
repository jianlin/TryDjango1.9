
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


    
