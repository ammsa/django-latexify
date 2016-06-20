=====
django-latexify
=====
|travis|

Quick start
-----------

1. Add "latexify" to your INSTALLED_APPS setting like this::

        INSTALLED_APPS = (
               ...
               'latexify',
        )


2. In your template, load latexify by including::

        {% load latexify %}

3. In the HTML header of your template, include::

        {% include 'latexify/stylesheets.html' %}


4. In the bottom of your HTML body, include the following to load the JS associated with latexify::

        {% include "latexify/scripts.html" %}

5. Latexify your text by including the template tag, for example

    .. code-block:: html
        :linenos:

        <!-- renders text argument to look like LaTeX-->
        {% latexify context_arg %}
        <!-- parses math equations using special tags (See examples) and renders text argument -->
        {% latexify context_arg parse_math=True %}
        <!-- render math equation inline -->
        {% latexify 'c = \pm\sqrt{a^2 + b^2}' math_inline=True %}
        <!-- render math equation in a centered new line -->
        {% latexify 'c = \pm\sqrt{a^2 + b^2}' math_block=True %}


which will render

    .. math::

    c = \pm\sqrt{a^2 + b^2}


installation
-----------

       python setup.py install

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