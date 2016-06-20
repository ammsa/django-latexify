from django.test import TestCase
from django.template import Context, Template


class LatexifyTests(TestCase):

    def tag_test(self, template, context, output):
        t = Template("{}{}".format('{% load latex %}', template))
        c = Context(context)
        self.assertEqual(t.render(c), output)

    def test_latexify__when_normal_text(self):
        template = '{% latexify test_text %}'
        context = {'test_text': 'hello world'}
        output = u'<span class="django-latex text">hello world</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_and_no_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': 'hello world'}
        output = u'<span class="django-latex text">hello world</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_and_inline_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(2)\$'}
        output = u'<span class="django-latex text">' \
                 u'<span class="django-latex math inline">' \
                 u'f(x)=\\sqrt(2)</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_and_block_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(2)\$$'}
        output = u'<span class="django-latex text">' \
                 u'<span class="django-latex math block">' \
                 u'f(x)=\\sqrt(2)</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_and_block_and_inline_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(4)\$$ is \$f(x)=2\$'}
        output = u'<span class="django-latex text">' \
                 u'<span class="django-latex math block">' \
                 u'f(x)=\\sqrt(4)</span> is ' \
                 u'<span class="django-latex math inline">f(x)=2</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_and_inline_and_block_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(4)\$ is \$$f(x)=2\$$'}
        output = u'<span class="django-latex text">' \
                 u'<span class="django-latex math inline">' \
                 u'f(x)=\\sqrt(4)</span> is ' \
                 u'<span class="django-latex math block">f(x)=2</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_not_closed_inline_math_tag_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(4)'}
        output = u'<span class="django-latex text">\\$f(x)=\\sqrt(4)</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_not_closed_block_math_tag_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(4)'}
        output = u'<span class="django-latex text">\\$$f(x)=\\sqrt(4)</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_unmatching_math_tags_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(4)\$'}
        output = u'<span class="django-latex text">\\$$f(x)=\\sqrt(4)\\$</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_unmatching_math_tags_reversed(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(4)\$$'}
        output = u'<span class="django-latex text">\\$f(x)=\\sqrt(4)\\$$</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_inline_tag_inside_block_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$g(x)=\$\sqrt(9)\$\$$'}
        output = u'<span class="django-latex text">\\$$g(x)=\\$\\sqrt(9)\\$\\$$</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_block_tag_inside_inline_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$y(x)=\$$\sqrt(16)\$$\$'}
        output = u'<span class="django-latex text">\\$y(x)=\\$$\\sqrt(16)\\$$\\$</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_normal_text_then_block_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': 'The following math eq: \$$y(x)=\sqrt(16)\$$ is complete'}
        output = u'<span class="django-latex text">' \
                 u'The following math eq: ' \
                 u'<span class="django-latex math block">' \
                 u'y(x)=\\sqrt(16)</span>' \
                 u' is complete</span>'
        self.tag_test(template, context, output)

    def test_latexify__when_parse_math_is_true_normal_text_then_inline_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': 'The following math eq: \$y(x)=\sqrt(16)\$ is complete'}
        output = u'<span class="django-latex text">' \
                 u'The following math eq: ' \
                 u'<span class="django-latex math inline">' \
                 u'y(x)=\\sqrt(16)</span>' \
                 u' is complete</span>'
        self.tag_test(template, context, output)

