from django import template


register = template.Library()


class django_latexify(template.Node):

    def __init__(self, name):
        self.name = template.Variable(name)


    def render(self, context):
        name = self.name.resolve(context)

        try:
            filepath = find(name)
            fp = open(filepath, "r")
            output = fp.read()
            # Only python 2.x needs decoding
            if isinstance(output, bytes):
                output = output.decode(conf.FILE_CHARSET)
            fp.close()
            output = ('<script id="%s" type="text/html">\n'
                      % name) + output + "\n</script>\n"
        except (IOError, ICanHazTemplateNotFound):
            output = ""
            if conf.DEBUG:
                raise

        return output