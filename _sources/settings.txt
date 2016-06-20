
Settings
========

You can modify the CSS classes in the ``<span ..>`` s django-latexify creates by including the following in your ``settings.py``

.. code-block:: python

    #  most outer span CSS classes
    LATEX_TEXT_CSS_CLASS = "django-latexify text"

    #  the CSS classes for inline math
    LATEX_MATH_INLINE_CSS_CLASS = "django-latexify math inline"

    #  the CSS classes for block math
    LATEX_MATH_BLOCK_CSS_CLASS = "django-latexify math block"
