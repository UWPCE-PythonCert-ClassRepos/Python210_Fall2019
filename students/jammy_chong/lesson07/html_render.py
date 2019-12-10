"""
A class-based system for rendering html.
"""
import os

# This is the framework for the base class
class Element:
    """
    Element superclass for all subsequent elements.
    It contains the !DOCTYPE element at the beginning of the html file.
    """

    Tag = "<!DOCTYPE html>\n" #Comment to run pytest
    # Tag = "html" #Use to run pytest
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.content.append(content)
        self.attributes = {**kwargs}
        self.class_attribute()


    def class_attribute(self):
        if 'clas' in self.attributes:
            self.attributes['class'] = self.attributes.pop('clas')


    def append(self, new_content):
        self.content.append(new_content)


    def create_content(self, separator='\n', cur_ind=""):
        Out_Content = ""
        for _ in self.content:
            if _ is None:
                pass
            else:
                try:
                    Out_Content += _.render(cur_ind=(cur_ind + self.indent)) + separator
                except AttributeError:
                    if isinstance(self, OneLineTag):
                        Out_Content += _ + separator
                    else:
                        Out_Content +=  cur_ind + self.indent + _ + separator
        return Out_Content


    def create_attributes(self):
        attributes = ""
        if bool(self.attributes):
            for _ in self.attributes:
                attributes += ' {}="{}"'.format(_, self.attributes[_])
        return attributes


    def write_content(self, String, out_file):
        if out_file is None:
            pass
        else:
            out_file.write(Element.Tag) # Comment to run pytest
            out_file.write(String)


    def render(self, out_file=None, cur_ind=""):
        String = cur_ind + '<' + self.Tag + self.create_attributes() + '>' + \
        '\n' + self.create_content(cur_ind=cur_ind) + cur_ind + '</' + self.Tag + '>'

        self.write_content(String, out_file)
        return String


class OneLineTag(Element):
    """
    Overrides the Superclass's render method to return a One Line element.
    """

    def render(self, out_file=None, cur_ind=""):
        String = cur_ind + '<' + self.Tag + self.create_attributes() + '>' + \
                 self.create_content(separator="", cur_ind="") + '</' + self.Tag + '>'

        self.write_content(String, out_file)
        return String


class SelfClosingTag(Element):
    """
    Overrides the Superclass's render method to return a Self-closing element.
    It does not parse content, it will return a TypeError if that's the case.
    """

    def __init__(self, **kwargs):
        self.attributes = {**kwargs}
        self.class_attribute()

    def render(self, out_file=None, cur_ind=""):
        String = cur_ind + '<' + self.Tag + self.create_attributes() + ' />'

        self.write_content(String, out_file)
        return String


class Html(Element):
    Tag = "html"


class Head(Element):
    Tag = "head"


class Body(Element):
    Tag = "body"


class P(Element):
    Tag = "p"


class Title(OneLineTag):
    Tag = "title"


class Hr(SelfClosingTag):
    Tag = "hr"


class Br(SelfClosingTag):
    Tag = "br"


class Meta(SelfClosingTag):
    Tag = "meta"


class Ul(Element):
    Tag = "ul"


class Li(Element):
    Tag = "li"


class A(OneLineTag):
    Tag = "a"
    def __init__(self, link, content):
        self.content = []
        self.content.append(content)
        self.attributes = {'href':link}
        self.class_attribute()


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        __class__.Tag = "h" + str(level)
        OneLineTag.__init__(self, content, **kwargs)
