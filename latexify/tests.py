from django.test import TestCase
from django.template import Context, Template
from django.template import TemplateSyntaxError
from django.conf import settings



class LatexifyTests(TestCase):

    def tag_test(self, template, context, output):
        t = Template("{}{}".format('{% load latexify %}', template))
        c = Context(context)
        self.assertEqual(t.render(c), output)

    def test__normal_text(self):
        template = '{% latexify test_text %}'
        context = {'test_text': 'hello world'}
        output = u'<span class="django-latexify text">hello world</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_and_no_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': 'hello world'}
        output = u'<span class="django-latexify text">hello world</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_and_inline_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(2)\$'}
        output = u'<span class="django-latexify text">' \
                 u'<span class="django-latexify math inline">' \
                 u'f(x)=\\sqrt(2)</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_and_block_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(2)\$$'}
        output = u'<span class="django-latexify text">' \
                 u'<span class="django-latexify math block">' \
                 u'f(x)=\\sqrt(2)</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_and_block_and_inline_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(4)\$$ is \$f(x)=2\$'}
        output = u'<span class="django-latexify text">' \
                 u'<span class="django-latexify math block">' \
                 u'f(x)=\\sqrt(4)</span> is ' \
                 u'<span class="django-latexify math inline">f(x)=2</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_and_inline_and_block_math_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(4)\$ is \$$f(x)=2\$$'}
        output = u'<span class="django-latexify text">' \
                 u'<span class="django-latexify math inline">' \
                 u'f(x)=\\sqrt(4)</span> is ' \
                 u'<span class="django-latexify math block">f(x)=2</span>' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_not_closed_inline_math_tag_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(4)'}
        output = u'<span class="django-latexify text">\\$f(x)=\\sqrt(4)</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_not_closed_block_math_tag_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(4)'}
        output = u'<span class="django-latexify text">' \
                 u'\\$$f(x)=\\sqrt(4)' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_unmatching_math_tags_in_text(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$f(x)=\sqrt(4)\$'}
        output = u'<span class="django-latexify text">' \
                 u'\\$$f(x)=\\sqrt(4)\\$' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_unmatching_math_tags_reversed(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$f(x)=\sqrt(4)\$$'}
        output = u'<span class="django-latexify text">' \
                 u'\\$f(x)=\\sqrt(4)\\$$' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_inline_tag_inside_block_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$$g(x)=\$\sqrt(9)\$\$$'}
        output = u'<span class="django-latexify text">' \
                 u'\\$$g(x)=\\$\\sqrt(9)\\$\\$$' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_block_tag_inside_inline_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text': '\$y(x)=\$$\sqrt(16)\$$\$'}
        out = u'<span class="django-latexify text">' \
              u'\\$y(x)=\\$$\\sqrt(16)\\$$\\$' \
              u'</span>'
        self.tag_test(template, context, out)

    def test__parse_math_is_true_normal_text_then_block_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text':
                   'The following math eq: \$$y(x)=\sqrt(16)\$$ is complete'}
        output = u'<span class="django-latexify text">' \
                 u'The following math eq: ' \
                 u'<span class="django-latexify math block">' \
                 u'y(x)=\\sqrt(16)</span>' \
                 u' is complete</span>'
        self.tag_test(template, context, output)

    def test__parse_math_is_true_normal_text_then_inline_tag(self):
        template = '{% latexify test_text parse_math=True %}'
        context = {'test_text':
                   'The following math eq: \$y(x)=\sqrt(16)\$ is complete'}
        output = u'<span class="django-latexify text">' \
                 u'The following math eq: ' \
                 u'<span class="django-latexify math inline">' \
                 u'y(x)=\\sqrt(16)</span>' \
                 u' is complete</span>'
        self.tag_test(template, context, output)

    def test__both_inline_and_block_args_are_true(self):
        template = '{% latexify test_text math_inline=True math_block=True %}'
        context = {'test_text':
                   'The following math eq: \$y(x)=\sqrt(16)\$ is complete'}
        output = u'<span class="django-latexify math inline">' \
                 u'The following math eq: ' \
                 u'\\$y(x)=\\sqrt(16)\\$ is complete' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__math_block_set_true(self):
        template = '{% latexify test_text math_block=True %}'
        context = {'test_text':
                   'The following math eq: \$$y(x)=\sqrt(16)\$$ is complete'}
        output = u'<span class="django-latexify math block">' \
                 u'The following math eq: ' \
                 u'\\$$y(x)=\\sqrt(16)\\$$ ' \
                 u'is complete</span>'
        self.tag_test(template, context, output)

    def test__latex_css_is_specified(self):
        template = '{% latexify test_text latex_css="my_css_class" %}'
        context = {'test_text':
                   'Hello world'}
        output = u'<span class="django-latexify my_css_class">' \
                 u'Hello world' \
                 u'</span>'
        self.tag_test(template, context, output)

    def test__value_from_setting(self):
        template = '{% value_from_settings "LATEX_MATH_INLINE_CSS_CLASS" %}'
        context = {}
        output = u'django-latexify math inline'
        self.tag_test(template, context, output)

    def test__value_from_setting_no_arg(self):
        with self.assertRaises(TemplateSyntaxError):
            template = '{% value_from_settings %}'
            context = {}
            output = u''
            self.tag_test(template, context, output)
