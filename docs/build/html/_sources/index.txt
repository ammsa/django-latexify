django-:math:`\LaTeX` ify documentation
=======================================

django-latexify let's you easily render text and math equations from your template to look like LaTeX.
The app lets you render math equations written in LaTeX on your HTML, or even just regular plain text.

It uses `Katex <https://github.com/Khan/KaTeX>`_ (a fast, easy-to-use JavaScript library for TeX math rendering on the web) for rending math equations and a modification of `WiTex <https://github.com/AndrewBelt/WiTeX>`_ (LaTeX like CSS) for rending plain text.

Installation
============

To install, just run::

   pip install django-latexify

or manually install it by running::

   python setup.py install

And that's it! The app need's some little configuarions, so read below.


Configurations
==============
The following are required configurations to make django-latexify work.

1. In your settings.py, add ``latexify`` to your ``INSTALLED_APPS`` like this:

The following is a SQL statement.

   .. code-block:: python
      :emphasize-lines: 3

      INSTALLED_APPS = (
          ...
          'latexify',
          ...
      )

2. In the template where you need to run django-latexify, load the template tag by including::

   {% load latexify %}

3. The template should also have django-latexify specific CSS, so in your HTML header, include::

   {% include 'latexify/stylesheets.html' %}

4. For the math to be rendered, some JS should be included to your template, so in the bottom of your HTML body, include::

   {% include "latexify/scripts.html" %}

and that's it! Read below or go to the examples section to see how to use django-latexify.


Quick Usage
===========

To render plain text,

   .. code-block:: html

      {% latexify 'Hello World!' %}

This will surround `Hello World!` with a span tag that have django-latexify CSS classes.


To render a math equation inline,

   .. code-block:: html

      {% latexify 'f(x) = \sqrt{\frac{x^2}{2}}' math_inline=True %}

This will output :math:`f(x) = \sqrt{\frac{x^2}{2}}`.

To render a math equation centered in a new line,

   .. code-block:: html

      {% latexify '\binom{n}{k} = \frac{n!}{k!(n-k)!}' math_block=True %}

which will output

.. math::

   \binom{n}{k} = \frac{n!}{k!(n-k)!}


you can also render text with inline math by surrounding your math equation with ``\$`` tags and setting ``parse_math`` argument to true.

   .. code-block:: html

      {% latexify 'My favourite eq: \$ \frac{d}{dx}\left( \int_{0}^{x} f(u)\,du\right)=f(x). \$' parse_math=True %}

which will give you

This will output `My mathy stuyff:` :math:`\frac{d}{dx}\left( \int_{0}^{x} f(u)\,du\right)=f(x).`

replacing the ``\$`` tag with ``\$$`` will render the math equation in a new line.


Guide
^^^^^

.. toctree::
   :maxdepth: 2

   example
   settings
   license
   help


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

