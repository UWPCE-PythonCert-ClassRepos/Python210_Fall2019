"""
Eric Gosnell
12.08.2019
Lesson 07 - HTML rendering

     *****      Pytest module  *****
"""

from io import StringIO
from html_elements import *
import pytest


def render_result(element, data="", ind=""):
    f = StringIO()
    if data:
        element.render(f, ind)
    else:
        element.render(f, ind)
    return f.getvalue()


# ----------------- STEP 1 ----------------- #


def test_init():
    e = Element()
    e = Element("this is some text")
    print(e.contents)


def test_append():
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    e = Element("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e, ind="").strip()
    print(file_contents)
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.index("this is") < file_contents.index("and this")
    assert file_contents.startswith("<>")
    assert file_contents.endswith("</>")


def test_render_element2():
    e = Element()
    e.append("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e, ind="").strip()
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.index("this is") < file_contents.index("and this")
    assert file_contents.startswith("<>")
    assert file_contents.endswith("</>")


# ----------------- STEP 2 ----------------- #


def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e, ind="").strip()
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    print(file_contents)
    assert file_contents.startswith("<!DOCTYPE html>")
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e, ind="").strip()
    print(file_contents)
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")
    file_contents = render_result(e, ind="").strip()
    assert "this is some text" in file_contents
    assert "and this is some more text" in file_contents
    print(file_contents)
    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")
    file_contents = render_result(page, ind="")
    print(file_contents) # so we can see it if the test fails
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    assert "<p>" in file_contents
    assert "</p>" in file_contents


# ----------------- STEP 3 ----------------- #


def test_head_element():
    page = Html()
    page.append(Head("A header!"))
    page.append(Head("Another header!"))
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")
    file_contents = render_result(page, ind="")
    print(file_contents)  # so we can see it if the test fails
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert "A header!" in file_contents
    assert "Another header!" in file_contents


def test_one_line_tag_append():
    e = OneLineTag()
    with pytest.raises(NotImplementedError):
        e.append("some more content")
    file_contents = render_result(e, ind="").strip()
    print(file_contents)


def test_title():
    e = Title("This is a Title")
    file_contents = render_result(e).strip()
    assert "This is a Title" in file_contents
    print(file_contents)
    assert file_contents.startswith("<title>")
    assert file_contents.endswith("</title>")


# ----------------- STEP 4 ----------------- #


def test_attributes():
    e = P("A paragraph of text", style="text-align: center", id="intro")
    file_contents = render_result(e, ind="").strip()
    print(file_contents)
    assert file_contents.endswith("</p>")
    assert file_contents.startswith("<p")
    assert 'style="text-align: center"' in file_contents
    assert 'id="intro"' in file_contents


# ----------------- STEP 5 ----------------- #


def test_hr():
    hr = Hr()
    file_contents = render_result(hr, ind="")
    print(file_contents)
    assert file_contents == '<hr />\n'


def test_hr_attr():
    hr = Hr(width=400)
    file_contents = render_result(hr, ind="")
    print(file_contents)
    assert file_contents == '<hr width="400" />\n'


def test_br():
    br = Br()
    file_contents = render_result(br, ind="")
    print(file_contents)
    assert file_contents == "<br />\n"


def test_content_in_br():
    with pytest.raises(TypeError):
        br = Br("some content")


def test_append_content_in_br():
    with pytest.raises(TypeError):
        br = Br()
        br.append("some content")


# ----------------- STEP 6 ----------------- #


def test_anchor():
    a = A("http://google.com", "link to google")
    file_contents = render_result(a, ind="").strip()
    print(file_contents)
    assert file_contents.startswith('<a ')


# ----------------- STEP 7 ----------------- #


def test_ul():
    u_list = Ul(id="TheList", style="line-height:200%")
    file_contents = render_result(u_list, ind="").strip()
    print(file_contents)
    assert file_contents.startswith('<ul ')
    assert file_contents.endswith("</ul>")
    assert 'id="TheList"' in file_contents
    assert 'style="line-height:200%"' in file_contents


def test_li():
    a_list = Li("This is the second item", style="color: red")
    file_contents = render_result(a_list, ind="").strip()
    print(file_contents)
    assert file_contents.startswith('<li ')
    assert file_contents.endswith("</li>")
    assert 'style="color: red"' in file_contents


# ----------------- STEP 8 ----------------- #


def test_meta():
    m = Meta()
    file_contents = render_result(m, ind="").strip()
    print(file_contents)
    assert file_contents == '<meta />'


def test_meta_attr():
    m = Meta(charset="UTF-8")
    file_contents = render_result(m, ind="").strip()
    print(file_contents)
    assert file_contents == '<meta charset="UTF-8" />'


# ----------------- STEP 9 ----------------- #


def test_indent():
    html = Html("some content")
    file_contents = render_result(html, ind="   ").rstrip()  #remove the end newline
    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[-1].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")


def test_indent_contents():
    html = Element("some content")
    file_contents = render_result(html, ind="")
    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(html.indent)


def test_multiple_indent():
    body = Body()
    body.append(P("some text"))
    html = Html(body)
    file_contents = render_result(html)
    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith(i * html.indent + "<")
    assert lines[4].startswith(3 * html.indent + "some")


def test_element_indent1():
    e = Html("this is some text")
    file_contents = render_result(e).strip()
    print(file_contents)
    assert "this is some text" in file_contents
    lines = file_contents.split('\n')
    assert lines[1] == "<html>"
    assert lines[2].startswith(e._indent + "thi")
    assert lines[3] == "</html>"
    assert file_contents.endswith("</html>")
