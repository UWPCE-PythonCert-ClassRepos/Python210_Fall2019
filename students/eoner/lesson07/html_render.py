#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop the content list
        # add tags to beginning / end
        open_tag = ["<{}".format(self.tag)]
        #if any kwargs, add them in to starting tag
        if self.attributes!={}:
            for k, v in self.attributes.items():
                open_tag.append(' {}="{}"'.format(k, v))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))

        #out_file.write("<{}>".format(self.tag))
        for content in self.contents:
            try:
                if content is not None:
                    content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>".format(self.tag))

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file):
    # loop the content list
    # add tags to beginning / end
        out_file.write("<{}>".format(self.tag))
        for content in self.contents:
            try:
                if content is not None:
                    out_file.write(str(content))
            except AttributeError:
                out_file.write(content)
        out_file.write("</{}>\n".format(self.tag))
    
    # make sure you can't append
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):

    #try to catch any content added
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file):
        # loop the content list
        # add tags to beginning / end
        open_tag = ["<{}".format(self.tag)]
        if self.attributes!={}:
            for k, v in self.attributes.items():
                open_tag.append(' {}="{}"'.format(k, v))
        out_file.write("".join(open_tag))
        out_file.write(" />\n")
    
    def append(self, content):
        raise TypeError

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, *args):
        self.attributes = args
        
    def render(self, out_file):
    # loop the content list
    # add tags to beginning / end
        out_file.write("<{} href>".format(self.tag))
        for arg in self.attributes:
            out_file.write('"{}"'.format(str(arg)))
            if self.attributes.index(arg)< (len(self.attributes)-1):
                out_file.write(', ')
        out_file.write("</{}>".format(self.tag))

class H(A):
    tag = "h"

class Ul(SelfClosingTag):
    tag = "ul"

class Li(Element):
    tag = "li"