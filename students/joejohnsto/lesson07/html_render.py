#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


from io import StringIO


# This is the framework for the base class
class Element(object):
    """
    A class which is an element of html
    Subclasses include common elements such as body, head, title, etc
    
    input
    content: accepts strings or other Elements
    kwargs: accepts html attributes as attribute="attribute definition"
            or as a dictionary {attribute: attribute definition}
    """

    Tag = 'html'
    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = kwargs
        if content:
            self.content.append(content)

    @property
    def open_tag(self):
        if self.attributes:
            att_list = [' ' + k + '="' + v + '"' for k, v in self.attributes.items()]
            return self.Tag + ''.join(att_list)
        else:
            return self.Tag
    
    @property
    def content_string(self):
        content_string = ''
        for _ in self.content:
            try:
                f = StringIO()
                _.render(f)
                content_string += f.getvalue()
            except AttributeError:
                content_string += _
            finally:
                if _ is not self.content[-1]:
                    content_string += '\n'
        return content_string
    
    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_string = '<' + self.open_tag + '>\n' + self.content_string + '\n</' + self.Tag + '>'
        out_file.write(out_string)


class Html(Element):
    Tag = 'html'
    
    def render(self, out_file):
        out_string = '<!DOCTYPE html>\n<' + self.open_tag + '>\n' + self.content_string + \
                     '\n</' + self.Tag + '>'
        out_file.write(out_string)


class Body(Element):
    Tag = 'body'


class P(Element):
    Tag = 'p'


class Head(Element):
    Tag = 'head'


class Ul(Element):
    Tag = 'ul'


class Li(Element):
    Tag = 'li'


class onelinetag(Element):
    """
    A subclass of Element which takes the same arguments but does not include /n characters
    """
    
    def render(self, out_file):
        out_string = '<' + self.open_tag + '> ' + self.content_string + ' </' + self.Tag + '>'
        out_file.write(out_string)


class Title(onelinetag):
    Tag = 'title'


class A(onelinetag):
    Tag = 'a'
    
    def __init__(self, link, content):
        super().__init__(content, href=link)


class H(onelinetag):
    
    def __init__(self, level, content, **kwargs):
        self.Tag = 'h' + str(level)
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    """
    A subclass of Element which does not include content or a separate closing tag
    """
    
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('Content is not allowed in Self Closing Elements!')
        super().__init__(content=None, **kwargs)
    
    def append(self):
        raise TypeError('Content is not allowed in Self Closing Elements!')
    
    def render(self, out_file):
        out_string = '<' + self.open_tag + ' />'
        out_file.write(out_string)


class Hr(SelfClosingTag):
    Tag = 'hr'


class Br(SelfClosingTag):
    Tag = 'br'


class Meta(SelfClosingTag):
    Tag = 'meta'