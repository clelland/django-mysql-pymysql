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
)
