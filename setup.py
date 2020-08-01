import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-latexify',
    version='0.3',
    packages=['latexify'],
    install_requires=[],
    include_package_data=True,
    license='MIT License',
    description='Easy LaTeX rendering for Django.',
    long_description=README,
    long_description_content_type='text/x-rst',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    # Enable django-setuptest
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
        # Required by django-setuptools on Python 2.6
        'argparse'
    ),
)
