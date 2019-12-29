#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"
    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
        else:
            self.contents = []
        self.attrs = kwargs


    def append(self, new_content):
        self.contents.append(new_content)

    def render_attrs(self):
        attrs = ""
        for i , (attr, val) in enumerate(self.attrs.items()):
            attrs += f' {attr}="{val}"'
        return attrs

    def render(self, out_file):
        # loop through the list of contents:
        attrs = self.render_attrs()
        out_file.write("<{}{}>\n".format(self.tag, attrs))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = "html"

    def render(self, out_file):
        out_file.write("<!DOCTYPE html>\n")
        super(Html, self).render(out_file)



class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        # loop through the list of contents:
        attrs = self.render_attrs()
        out_file.write("<{}{}>".format(self.tag, attrs))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write("</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError
        super(SelfClosingTag, self).__init__(content, **kwargs)


    def render(self, out_file):
        # loop through the list of contents:
        attrs = self.render_attrs()
        out_file.write("<{}{} />".format(self.tag, attrs))


class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super(A, self).__init__(content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    tag = "h"
    def __init__(self, num, content=None, **kwargs):
        self.tag += str(num)
        super(H, self).__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"