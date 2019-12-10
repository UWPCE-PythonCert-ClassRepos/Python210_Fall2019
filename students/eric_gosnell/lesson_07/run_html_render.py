"""
Eric Gosnell
12.08.2019
Lesson 07 - HTML rendering

     *****      Main execution module  *****
"""

from io import StringIO
import html_elements as hr


if __name__ == "__main__":

    def render_page(page, filename, ind=""):
        f = StringIO()
        if ind is None:
            page.render(f, ind)
        else:
            page.render(f, ind)

        print(f.getvalue())
        with open(filename, 'w') as outfile:
            outfile.write(f.getvalue())


    print('#----------------- STEP 1 -----------------#\n')

    page = hr.Html()
    print(page)
    page.append("Here is a paragraph of text -- there could be more of them, "
                "but this is enough to show that we can do some text")
    print(page.contents[-1])
    page.append("And here is another piece of text -- you should be able to add any number")
    print(page.contents[-1])
    render_page(page, "test_html_output1.html")

    print('#----------------- STEP 2 -----------------#\n')

    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    render_page(page, "test_html_output2.html")

    print('#----------------- STEP 3 -----------------#\n')

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    render_page(page, "test_html_output3.html")

    print('#----------------- STEP 4 -----------------#\n')

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    page.append(body)
    render_page(page, "test_html_output4.html")

    print('#----------------- STEP 5 -----------------#\n')

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    page.append(body)
    render_page(page, "test_html_output5.html")

    print('#----------------- STEP 6 -----------------#\n')

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    body.append("And this is a ")
    body.append(hr.A("http://google.com", "link to Google"))
    page.append(body)
    render_page(page, "test_html_output6.html")

    print('#----------------- STEP 7 -----------------#\n')

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.H(2, "PythonClass - Class 6 example"))
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    a_list = hr.Li("This is the second item", style="color: red")
    a_list.append( hr.Li("The first item in a list") )
    a_list.append( hr.Li("This is the second item", style="color: red") )
    item = hr.Li()
    item.append("And this is a ")
    item.append(hr.A("http://google.com", "link"))
    item.append("to google")
    a_list.append(item)
    body.append(a_list)
    page.append(body)
    render_page(page, "test_html_output7.html")

    print('#----------------- STEP 8 -----------------#\n')

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Meta(charset="UTF-8"))
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append( hr.H(2, "PythonClass - Example") )
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    a_list = hr.Ul(id="TheList", style="line-height:200%")
    a_list.append( hr.Li("The first item in a list") )
    a_list.append( hr.Li("This is the second item", style="color: red") )
    item = hr.Li()
    item.append("And this is a ")
    item.append(hr.A("http://google.com", "link"))
    item.append("to google")
    a_list.append(item)
    body.append(a_list)
    page.append(body)
    render_page(page, "test_html_output8.html")

    print('#----------------- STEP 8 -----------------#\n')

    page = hr.Html()
    head = hr.Head()
    head.append(hr.Meta(charset="UTF-8"))
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.H(2, "PythonClass - Example"))
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    a_list = hr.Ul(id="TheList", style="line-height:200%")
    a_list.append(hr.Li("The first item in a list") )
    a_list.append(hr.Li("This is the second item", style="color: red"))
    item = hr.Li()
    item.append("And this is a ")
    item.append(hr.A("http://google.com", "link"))
    item.append("to google")
    a_list.append(item)
    body.append(a_list)
    page.append(body)
    render_page(page, "test_html_output8.html")
