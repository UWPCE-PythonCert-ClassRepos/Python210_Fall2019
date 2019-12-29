
class html_element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):

        if content is None:
            self.contents = []
        else:
            self.contents = [content]

        self.attributes = kwargs


    def append(self, new_content):
        if(new_content is not None):
            self.contents.append(new_content)

    def render(self, out_file, indent = 0):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))

        indent += 4

        for content in self.contents:
            try:
                out_file.write(" " * indent)
                content.render(out_file, indent)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
 
        out_file.write(" " *( indent - 4))
        out_file.write(f"</{self.tag}>\n")

class Body(html_element):
    tag = "body"

class Html(html_element):
    tag = "html"

    def render(self, out_file, indent = 0):


        open_tag = [" " * indent + "<!DOCTYPE html>\n"]
        open_tag.append(" " * indent + "<{}".format(self.tag))
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))

        indent += 4

        for content in self.contents:
            try:
                out_file.write(" " * indent)
                content.render(out_file, indent)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(" " * (indent - 4))
        out_file.write(f"</{self.tag}>\n")

class Paragraph(html_element):
    tag = "p"

class Head(html_element):
    tag = "head"

class OneLineTag(html_element):
    def render(self, out_file, indent = 0):

        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

    def _open_tag(self):
        """Private method that provides open tag with attributes
        """
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return ''.join(open_tag)

class Title(OneLineTag):
    tag = "title"

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class H(OneLineTag):
    def __init__(self, header_level ,content=None):
        super().__init__(content)
        self.header_level = header_level
        self.tag = "h{}".format(self.header_level)

class SelfClosingTag(html_element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile, indent = 0):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(tag)

    def _open_tag(self):
        open_tag = ["<{} ".format(self.tag)]

        for key, value in self.attributes.items():
            open_tag.append('{}="{}" '.format(key, value))
        return ''.join(open_tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Header(SelfClosingTag):
    tag = "hr"

class Break(SelfClosingTag):
    tag = "br"

class Metatag(SelfClosingTag):
    tag = "meta"

class Ul(html_element):
    tag = 'ul'

class List(html_element):
    tag = 'li'

if __name__ == "__main__":
    e = html_element("Yo")
