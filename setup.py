from setuptools import setup, find_packages
import os

CLASSIFIERS = []

setup(
    author="Martin Ogden",
    author_email="martin@cahoona.co.uk",
    name='django-spektrix',
    version='0.0.1',
    description='A Python / Django wrapper and utilities for spektrix.co.uk ticket provider API',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    license='Attribution 3.0 Unported (CC BY 3.0)',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'django',
        'lxml',
    ],
    package_data={'': ['templates']},
    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,
)
