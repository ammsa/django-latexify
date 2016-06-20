import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-latexify',
    version='0.1',
    packages=['latexify'],
    install_requires=[],
    include_package_data=True,
    license='MIT License',
    description='A django-app to render text and math equations to look like LaTeX.',
    long_description=README,
    url='https://github.com/AmmsA/django-latexify',
    author='Mustafa S',
    author_email='mabualsaud@outlook.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
