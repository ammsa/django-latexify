django-latexify |travis| |coveralls| |pypi|
========================


django-latexify let’s you easily render text and math equations from your template to look like LaTeX. The app lets you render math equations written in LaTeX on your HTML, or even just regular plain text.

It uses Katex (a fast, easy-to-use JavaScript library for TeX math rendering on the web) for rending math equations and a modification of WiTex (LaTeX like CSS) for rending plain text.


installation
-----------

       python setup.py install

Quick start
-----------

1. Add "latexify" to your INSTALLED_APPS setting like this:

      .. code-block:: python

         INSTALLED_APPS = (
             ...
             'latexify',
             ...
         )

2. In your template, load latexify by including::

        {% load latexify %}

3. In the HTML header of your template, include::

        {% include 'latexify/stylesheets.html' %}


4. In the bottom of your HTML body, include the following to load the JS associated with latexify::

        {% include "latexify/scripts.html" %}

5. Latexify your text by including the template tag, for example

      .. code-block:: html

         {% latexify context_arg %}
         {% latexify context_arg parse_math=True %}
         {% latexify 'c = \pm\sqrt{a^2 + b^2}' math_inline=True %}
         {% latexify 'c = \pm\sqrt{a^2 + b^2}' math_block=True %}



Contributing
-----------

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

License
-----------

All parts of django-latexify are free to use and abuse under the `open-source MIT license`_.


.. |travis| image:: https://travis-ci.org/AmmsA/django-latexify.svg?branch=master
   :alt: Build Status - master branch
   :target: https://travis-ci.org/AmmsA/django-latexify
.. |coveralls| image:: https://img.shields.io/coveralls/AmmsA/django-latexify/master.svg
   :target: https://coveralls.io/github/AmmsA/django-latexify       

.. |pypi| image:: https://img.shields.io/pypi/v/django-latexify.svg
   :target: https://pypi.python.org/pypi/django-latexify
   :alt: Latest PyPI version