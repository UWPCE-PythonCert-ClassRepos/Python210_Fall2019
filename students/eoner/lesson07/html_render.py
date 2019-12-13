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
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    
    # make sure you can't append
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, out_file):
        # loop the content list
        # add tags to beginning / end
        open_tag = ["<{}".format(self.tag)]
        if self.attributes!={}:
            for k, v in self.attributes.items():
                open_tag.append(' {}="{}"'.format(k, v))
        for content in self.contents:
            try:
                if content is not None:
                    raise TypeError
            except AttributeError:
                out_file.write(content)
        out_file.write("".join(open_tag))
        out_file.write(" />\n")
    
    def append(self, content):
        raise TypeError

class Hr(SelfClosingTag):
    tag = "hr"
    #Hr(width=400)

class Br(SelfClosingTag):
    tag = "br"