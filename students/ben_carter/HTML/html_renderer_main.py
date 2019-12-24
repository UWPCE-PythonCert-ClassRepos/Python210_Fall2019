"""
a simple script can run and test your html rendering classes.
Uncomment the steps as you add to your rendering.
"""

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render_classes as html_render

# writing the file out:
def render_page(page, filename, indent=None):
    """
    render the tree of elements
    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    if indent is None:
        page.render(f)
    else:
        page.render(f, indent)

    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


page = html_render.Html()

head = html_render.Head()
head.append(html_render.Metatag(charset="UTF-8"))
head.append(html_render.Title("PythonClass = Revision 1087:"))

page.append(head)

body = html_render.Body()

body.append(html_render.H(2, "PythonClass - Example"))

body.append(html_render.Paragraph("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
                 style="text-align: center; font-style: oblique;"))

body.append(html_render.Header())

list = html_render.Ul(id="TheList", style="line-height:200%")

list.append(html_render.List("The first item in a list"))
list.append(html_render.List("This is the second item", style="color: red"))

item = html_render.List()
item.append("And this is a ")
item.append(html_render.A("http://google.com", "link"))
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_output8.html")
