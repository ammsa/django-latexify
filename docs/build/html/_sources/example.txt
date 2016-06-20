Usage
-----

Examples
========



Bellow is a full example:

This is just a simple view that will include `my_mathy_paragraph` variable to be included in the context passed to the template

.. code-block:: python

    #  views.py
    from django.views.generic.base import TemplateView
    from somewhere import my_mathy_paragraph

    class HomePageView(TemplateView):
        template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['my_mathy_paragraph'] = my_mathy_paragraph
        return context


In the HTML that will use django-latexify

.. code-block:: html

    {% load staticfiles %}
    {% load latexify %}

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My math blog</title>
        {% include 'latexify/stylesheets.html' %}
    </head>

    <body>
        <h2>Welcome to my mathy blog</h2>

        <p>{% latixfy my_mathy_paragraph parse_math=True %}</p>

        <p>{% latixfy 'My latex like plain text'%}</p>

        <p>My inline math {% latixfy 'e=mc^2' inline_math=True %}</p>

        <p>My block math {% latixfy 'e=mc^2' block_math=True %}</p>


        {% include "latexify/scripts.html" %}
    </body>
    </html>

