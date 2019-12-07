#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None, id='', style='', clas='', width=''):
        self.content = [content, ]
        self.style = style
        self.id = id
        self.clas = clas
        self.width = width

    def append(self, new_content):
        if self.content[0] is None:
            self.content[0] = new_content
        else:
            self.content.append(new_content)

    def render(self, out_file, ind=''):
        out_file.write('<' + self.tag + '>\n')
        for item in self.content:
            if type(item) == str:
                out_file.write(item + '\n')
            else:
                item.render(out_file)
        out_file.write('</' + self.tag + '> \n')


class Body(Element):
    tag = 'body'


class Html(Element):
    tag = 'html'


class P(Element):
    tag = 'p'

    def render(self, out_file, ind=''):
        if self.style:
            out_file.write('<' + self.tag + ' style=\"' + self.style + '\">\n')
        for item in self.content:
                out_file.write(item + '\n')
        out_file.write('</' + self.tag + '> \n')


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write('<' + self.tag + '> ')
        for item in self.content:
            out_file.write(item)
        out_file.write('</' + self.tag + '>\n')


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, out_file):
        if self.width:
            out_file.write('<' + self.tag + ' width=\"' + self.width + '/>')
        else:
            out_file.write('<' + self.tag + '/>\n')


class Hr(SelfClosingTag):
    tag = 'hr '


class br(SelfClosingTag):
    tag = 'br '


class A(Element):
    def __init__(self, link=None, content=None):
        self.content = content
        self.link = link

    def render(self, out_file, ind=''):
        out_file.write('<a href=' + self.link + '>link' + self.content + '</a>\n')



