#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "abstract_tag"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = dict(**kwargs)
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        self.cur_ind = "4".join(self.indent)
        print(self.cur_ind)
        out_file.write(self._open_tag())
        out_file.write('\n')
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write(self._close_tag())


    def _open_tag(self):
        open_tag = f'<{self.tag}'
        for key, value in self.attributes.items():
            open_tag += f' {key}="{value}"'
        open_tag += '>'
        return open_tag

    def _close_tag(self):
        close_tag = f'</{self.tag}>'
        return close_tag


class Html(Element):
    tag = "html"
    def render(self, out_file, cur_ind=""):
        out_file.write('<!DOCTYPE html>\n')
        super().render(out_file)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = "abstract_tag"

    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())

    def append(self, new_content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class H2(OneLineTag):
    tag = "h2"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You cannot add content to a SelfClosingTag")

    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />"
        out_file.write(tag)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = f'h{level}'
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)














