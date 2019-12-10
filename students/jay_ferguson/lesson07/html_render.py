#!/usr/bin/env python3

# Adapted from earlier works by davidpokrajac

class Element:
    """
    Base class for all HTML child elements
    """
    Tag = 'html'

    def __init__(self, content=None, **kwargs):
        """
        Instantiate class.
        :param content: Object or text to add to element.
        :param kwargs: attribute=value pairs of elements.
                       Note - to specify 'class=value', use keyword _class.
        """
        self.Content = []  # List of elements
        self.Content.append(content)

        if '_class' in kwargs:
            kwargs['class'] = kwargs.pop('_class')

        self._attributes = kwargs

    @property
    def attributes(self):

        if self._attributes == {}: # See if there are any kwargs. If not, return blank attributes.

            return ''

        else:
            attributes = ['{}="{}"'.format(key, self._attributes[key]) for key in self._attributes.keys()]
            attribute_tag = ' '

            for attribute in attributes:
                attribute_tag += attribute

                if attributes.index(attribute) < len(attributes) - 1:
                    attribute_tag += ', '

                else:
                    attribute_tag += ' '

            return attribute_tag



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

        data = '<' + self.Tag + self.attributes + '>\n' + Content + '\n' + \
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


# class A(Element):
#     Tag = 'a'
#
#     def __init__(self, link, content):
#         self.Content = content
#         self.link = link
#
#     def render(self, out_file=None):
#
#         data = '<' + self.Tag + 'href="' + self.link + '">\n' + self.Content + '\n' + \
#                  '</' + self.Tag + '>'
#
#         if out_file is None:
#             pass
#         else:
#             try:
#                 with open(out_file, 'w+') as f:
#                     f.write(data)
#             except TypeError:  # Catch error if a StringIO object is passed
#                 out_file.write(data)


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


class SelfClosingTag(OneLineTag):
    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

        if content is not None:
            raise TypeError('Element cannot contain content')

    def render(self, out_file=None):

        data = '<' + self.Tag + self.attributes + '/>\n'

        if out_file is None:
            pass
        else:
            try:
                with open(out_file, 'w+') as f:
                    f.write(data)
            except TypeError:  # Catch error if a StringIO object is passed
                out_file.write(data)

        return data  # we need to return. When we call recursively, we will have file argument just for first


class Br(SelfClosingTag):
    Tag = 'br'


class Hr(SelfClosingTag):
    Tag = 'hr'

    def len(self):
        print(len(self.Content))


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