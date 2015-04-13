import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-conf-vars',
    version='0.1',
    packages=['django_admin_conf_vars'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to have configuration variables for your project with the Django admin.',
    long_description=README,
    url='https://github.com/maoaiz/django-admin-conf-vars',
    packages=find_packages(),
    install_requires=['django>=1.7', ],
    author='Mauricio Aizaga',
    author_email='mauricioaizaga@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)