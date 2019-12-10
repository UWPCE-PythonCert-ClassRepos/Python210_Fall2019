#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        # self.contents = [content]
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

        #self.contents = []
        #self.append(content)
        self.attributes = kwargs

        #print("contents is:", self.contents)

    def append(self, new_content):
        if(new_content is not None):
            self.contents.append(new_content)


    def render(self, out_file, curr_ind = 0):
        # loop through the list of contents:

        # curr_ind adds current number of indent spaces
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))

        # Adding indent
        curr_ind += 4

        for content in self.contents:
            try:
                out_file.write(" " * curr_ind)
                content.render(out_file, curr_ind)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        # Subtracts indent so close tag can align with open tag
        out_file.write(" " *( curr_ind - 4))
        out_file.write(f"</{self.tag}>\n")



class Body(Element):
    tag = "body"

class Html(Element):
    tag = "html"

    def render(self, out_file, curr_ind = 0):

        # open_tag = ["<!DOCTYPE html>\n<{}".format(self.tag)]
        open_tag = [" " * curr_ind + "<!DOCTYPE html>\n"]
        open_tag.append(" " * curr_ind + "<{}".format(self.tag))
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))

        # Adding indent after initial html tag
        curr_ind += 4

        for content in self.contents:
            try:
                out_file.write(" " * curr_ind)
                content.render(out_file, curr_ind)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(" " * (curr_ind - 4))
        out_file.write(f"</{self.tag}>\n")

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, curr_ind = 0):
        #out_file.write("<{}>".format(self.tag))
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

    def _open_tag(self):
        """Private method that provides open tag with attributes
        """
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return ''.join(open_tag)


class Title(OneLineTag):
    tag = "title"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    def __init__(self, header_level ,content=None):
        super().__init__(content)
        self.header_level = header_level
        self.tag = "h{}".format(self.header_level)


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)


    def render(self, outfile, curr_ind = 0):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(tag)


    def _open_tag(self):
        open_tag = ["<{} ".format(self.tag)]

        for key, value in self.attributes.items():
            open_tag.append('{}="{}" '.format(key, value))
        return ''.join(open_tag)


    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"



class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'





if __name__ == "__main__":
    e = Element("Yo")