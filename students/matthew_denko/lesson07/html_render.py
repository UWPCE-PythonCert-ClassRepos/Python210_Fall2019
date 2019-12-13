#!/usr/bin/env python3

# - assignment description -----------------------------------------------------

"""
A class-based system for rendering html.
"""
# - function description -------------------------------------------------------

class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        print("contents is:", self.contents)
        if self.contents == [None]:
            self.contents = list()
        else:
            self.contents.append(content)


    def append(self, new_content):
        self.contents.append(new_content)
        pass

    def render(self, out_file, **kwargs):
         # loop through the list of contents:
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
                out_file.write("\n")
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    "defining new subclass to override main render"
    def render(self, out_file):

        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def _open_tag(self):
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))

    def _close_tag(self):
        for content in self.contents:
            content.render(out_file)
            out_file.write("\n")

    def render(self, out_file):
        # loop through the list of contents:
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(self._close_tag())
        out_file.write("\n")

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        super().__init__(content, **kwargs)
