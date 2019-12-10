#!/usr/bin/env python3

# Adapted from earlier works by davidpokrajac

class Element:
    """
    Base class for all HTML child elements
    """
    Tag = 'html'

    def __init__(self, content=None):
        self.Content = []  # List of elements
        self.Content.append(content)

    def append(self, new_content):
        if isinstance(new_content, str):
            self.Content.append(TextWrapper(new_content))
        else:
            self.Content.append(new_content)

    def render(self, out_file=None):
        Content = ''
        for _ in self.Content:
            if _ is None:
                pass
            else:
                try:
                    Content += _.render()
                except AttributeError:  # Detect base case for recursion
                    Content += _

        data = '<' + self.Tag + '>\n' + Content + '\n' + \
                 '</' + self.Tag + '>'

        if out_file is None:
            pass
        else:
            try:
                with open(out_file, 'w+') as f:
                    f.write(data)
            except TypeError:  # Catch error if a StringIO object is passed
                out_file.write(data)

        return data  # we need to return. When we call recursively, we will have file argument just for first

class Body(Element):
    Tag = 'body'


class Html(Element):
    Tag = 'html'


class P(Element):
    Tag = 'p'

class Head(Element):
    Tag = 'head'


class OneLineTag(Element):
    """
    Parent class for all single line tags
    """

    def render(self, out_file=None):
        data = super().render(out_file=None)
        return data.replace('\n', '')

class Title(OneLineTag):
    Tag = 'title'

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text.
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/html_renderer.html#notes-on-handling-duck-typing
    """
    def __init__(self, text):
        self.text = text

    def render(self, out_file=None):
        if out_file is None:
            pass
        else:
            with open(out_file, 'w+') as f:
                f.write(self.text)

        return self.text