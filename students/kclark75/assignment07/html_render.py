#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for just text
    This allows the Element classes to render either Element objects or
    plain text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)

class Element(object):

    tag = "html"

    # TODO kwargs - How do you store something so that it
    # can be used in another method??

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = ['this is some text']
        elif content is not None:
            self.contents = [content]

    def append(self, new_content):

#        self.contents.append(TextWrapper(str(new_content)))
        self.contents.append(new_content)

    def render(self, out_file, **kwargs):
        # loop through the list of contents:
        # TODO script to render 'p' does not add attribute
#        open_tag = ["<{} ".format(self.tag)]
#        open_tag.append(">\n")
#        out_file.write("".join(open_tag))

        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")

        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):

        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
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


class Hr(Element):
    tag = "hr"
