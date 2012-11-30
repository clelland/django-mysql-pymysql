from setuptools import setup, find_packages
setup(
    name = "django-mysql-pymysql",
    version = "0.1",
    packages = find_packages('src'),
    package_dir = {'':'src'},

    # metadata for upload to PyPI, one day
    author = "Ian Clelland",
    author_email = "clelland@gmail.com",
    description = "Django MySQL backend for PyMySQL adapter",
    license = "BSD",
    keywords = "django mysql pymysql",
    url = "https://github.com/clelland/django-mysql-pymysql",

    classifiers = [
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Database :: Front-Ends",
    ],

    long_description = """
django-mysql-pymysql
====================

This is a Django database backend for MySQL, using the PyMySQL database adapter. It is intended to be a drop-in replacement for the built-in MySQLdb backend, and leverages quite a bit of its code.

It is currently experimental, and has only been tested against Django trunk (1.4-pre-alpha), and Vinay Sajip's Py3k branch on BitBucket (https://bitbucket.org/vinay.sajip/django). At the moment, it won't work with Django 1.3, as it uses Aymeric Augustin's timezone-aware datetime patch.


Requirements
------------

* Django trunk or Py3k Branch
* PyMySQL (patches here: https://github.com/clelland/PyMySQL)

Installation
------------

::

1. Clone and install into your site-packages directory:

        $ git clone https://github.com/clelland/django-mysql-pymysql
        $ cd django-mysql-pymysql
        $ python setup.py install

2. Edit your settings file:

::

        DATABASES = {
            'default': {
                'ENGINE': 'mysql_pymysql',
                'HOST': ...,
                'USER': ...,
                'PASSWORD': ...,
            }
        }


3. You're done.
    """
)
