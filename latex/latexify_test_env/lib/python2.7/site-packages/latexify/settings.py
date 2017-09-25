# django-latexify settings file.
#
# Please consult the docs for more information about each setting.

from django.conf import settings

LATEX_TEXT_CSS_CLASS = getattr(settings,
                               'LATEX_TEXT_CSS_CLASS',
                               "django-latexify text")

LATEX_MATH_INLINE_CSS_CLASS = getattr(settings,
                                      'LATEX_MATH_INLINE_CSS_CLASS',
                                      "django-latexify math inline")

LATEX_MATH_BLOCK_CSS_CLASS = getattr(settings,
                                     'LATEX_MATH_BLOCK_CSS_CLASS',
                                     "django-latexify math block")
