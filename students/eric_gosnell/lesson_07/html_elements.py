"""
Eric Gosnell
12.08.2019
Lesson 07 - HTML rendering

     *****     Module contains classes only     *****
"""

if __name__ == "__main__":
    raise Exception("This file is not meant to be run by itself.")


class Element:
    """ Base class for sub-classing and rendering HTML file elements """
    def __init__(self, content=None, **kwargs):
        if content:
            self._contents = [content]
        else:
            self._contents = []
        if kwargs:
            self._attributes = kwargs
        else:
            self._attributes = None
        self._tag = ""
        self._indent = "    "

    def __repr__(self):
        return f'{self.__class__.__name__} element'

    def append(self, new_content):
        self._contents.append(new_content)

    def _open_tag(self):
        if self._tag != "html":
            open_tag = [f"<{self._tag}"]
        else:
            open_tag = [f"<!DOCTYPE html>\n<{self._tag}"]
        if self.attributes is not None:
            for k, v in self.attributes.items():
                open_tag.append(f' {k}="{v}"')
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return f"</{self._tag}>"

    def render(self, outfile, curr_ind=""):
        outfile.write(f'{curr_ind}{self._open_tag()}' + "\n")
        for content in self.contents:
            try:
                content.render(outfile, curr_ind + self._indent)
            except AttributeError:
                outfile.write(f'{curr_ind}{self._indent}{content}' + "\n")
        outfile.write(f'{curr_ind}{self._close_tag()}' + "\n")
        return outfile

    @property
    def contents(self):
        return self._contents

    @property
    def attributes(self):
        return self._attributes

    @property
    def indent(self):
        return self._indent


class Html(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "html"


class Body(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "body"


class P(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "p"


class Head(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "head"


class Ul(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "ul"


class Li(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "li"


class OneLineTag(Element):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

    def render(self, outfile, curr_ind=""):
        outfile.write(f'{curr_ind}{self._open_tag()}')
        for content in self.contents:
            outfile.write(content)
        outfile.write(f'{self._close_tag()}' + "\n")
        return outfile

    def append(self, content):
        raise NotImplementedError("Can not append content to OneLineTag")


class Title(OneLineTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "title"


class A(OneLineTag):
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
        self._tag = "a"


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = f"h{level}"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("Can not add content to a SelfClosingTag")
        else:
            super().__init__(**kwargs)

    def render(self, outfile, curr_ind=""):
        outfile.write(f'{curr_ind}{self._open_tag()[:-1]}' + " />\n")
        return outfile

    def append(self, content):
        raise TypeError("Can not append content to a SelfClosingTag")


class Hr(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "hr"


class Br(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "br"


class Meta(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self._tag = "meta"
