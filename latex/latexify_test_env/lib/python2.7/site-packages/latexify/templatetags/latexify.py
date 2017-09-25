import re

from django import template
from django.utils.safestring import mark_safe

from .. import settings as latex_settings

register = template.Library()


regex_math_inline = r'(?<!\\)\\\$(([^\$]).*?)(?<!\\)(\\\$)(?=[^\$]|$)'
regex_math_block = r'(?<!\\)\\\$\$((.*?))(?<!\\)\\\$\$'


@register.inclusion_tag('latexify/latexify.html')
def latexify(text,
             parse_math=False,
             math_inline=False,
             math_block=False,
             latex_css=None):
    """

    Args:
        text: Text to be rendered to look like LaTeX
        parse_math: Boolean to check whether we should
                    parse the math from regular text
        math_inline: renders math equation inline
        math_block: renders math equation as a block
        latex_css: Extra CSS to be included in the span
                   of the rendered LaTeX

    Returns:
        latex_type: the CSS classes of the most outer
                    span of the rendered LaTeX
        latex_text: The html-safe text that inside the
                    most-outer span

    """

    if not latex_css:
        if math_inline:
            latex_type = latex_settings.LATEX_MATH_INLINE_CSS_CLASS
        elif math_block:
            latex_type = latex_settings.LATEX_MATH_BLOCK_CSS_CLASS
        else:
            latex_type = latex_settings.LATEX_TEXT_CSS_CLASS
    else:
        #  always add 'django-latexify' to user specified classes
        latex_type = 'django-latexify {}'.format(latex_css)

    if math_inline and math_block:
        #  can't have both inline and block together, not parsing.
        return {'latex_type': latex_type,
                'latex_text': mark_safe(text)}

    # span tag to be surrounded by the parsed math
    surround = r'<span class="{}">\1</span>'

    if parse_math:
        try:
            error_msg = 'Can\t have two different tags in the same level'

            # check if there is inline tags inside block tag
            matches = re.findall(regex_math_block, text)
            if matches:
                for m in matches[0]:
                    if re.findall(regex_math_inline, m) or \
                       re.findall(regex_math_block, m):
                        raise ValueError(error_msg)

            # check if there is block tags inside inline tag
            matches = re.findall(regex_math_inline, text)
            if matches:
                for m in matches[0]:
                    if re.findall(regex_math_block, m):
                        raise ValueError(error_msg)

        except ValueError:
            #  invalid text input, not parsing.
            return {'latex_type': latex_type,
                    'latex_text': mark_safe(text)}

        # find and replace block math tags
        text = re.sub(regex_math_block,
                      surround.format(
                              latex_settings.LATEX_MATH_BLOCK_CSS_CLASS
                      ),
                      text, flags=re.DOTALL)

        # find and replace inline math tags
        text = re.sub(regex_math_inline,
                      surround.format(
                            latex_settings.LATEX_MATH_INLINE_CSS_CLASS
                      ),
                      text, flags=re.DOTALL)

    return {'latex_type': latex_type,
            'latex_text': mark_safe(text)}


@register.tag
def value_from_settings(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, var = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument"
                                           % token.contents.split()[0])
    return ValueFromSettings(var)


class ValueFromSettings(template.Node):
    def __init__(self, var):
        self.arg = template.Variable(var)

    def render(self, context):
        return getattr(latex_settings,
                       re.sub(r'\W+', '', str(self.arg)))
