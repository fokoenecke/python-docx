# encoding: utf-8

"""
Returns corresponding functions to call for creating
the different docx elements.
"""
from docx.enum.text import WD_BREAK
from docx.text import Run, Paragraph


def get_append_call(html_tag):
    """
    Returning the function call for creating the given HTML tag
    """
    return _dispatch_html.get(html_tag)


def append_paragraph(element, container):
    """
    <p> creates a paragraph element inside a docx container element.
    """
    return container.add_paragraph(text=element.text)


def append_list_item(element, container):
    """
    <li> Create a list item element inside a docx container from.
    Choose the style depending on its HTML parents class
    """
    style = _list_style.get(element.getparent().tag, 'ListBullet')
    return container.add_paragraph(text=element.text, style=style)


def append_line_break(element, container):
    """
    <br> Creates a break item inside the given container.
    """
    if isinstance(container, Run):
        return container.add_break(break_type=WD_BREAK.LINE)
    elif isinstance(container, Paragraph):
        run = container.add_run()
        return run.add_break(break_type=WD_BREAK.LINE)


def append_bold_run(element, container):
    """
    <strong> Creates a bold text run inside the paragraph container.
    Appends remainder of text as a additional run
    """
    if isinstance(container, Paragraph):
        run = container.add_run(element.text)
        run.bold = True
        container.add_run(element.tail)
        return run

    elif isinstance(container, Run):
        container.bold = True
        container.add_text(element.text)
        return container


#TODO Runs have to be 'prebuild' to match their possible nesting
def append_italic_run(element, container):
    """
    <em> Creates an italic text run inside the paragraph container.
    Appends remainder of text as a additional run
    """
    if isinstance(container, Paragraph):
        run = container.add_run(element.text)
        run.italic = True
        container.add_run(element.tail)
        return run

    elif isinstance(container, Run):
        container.italic = True
        container.add_text(element.text)
        return container


def append_heading(element, container):
    """
    <hx> Creates a heading paragraph inside the document container
    """
    container.add_heading(element.text, int(element.tag[1:]))

# map of HTML list tags and their docx styles
_list_style = dict(
    ol='ListNumber',
    ul='ListBullet',
)

# map of HTML tags and their corresponding functions
_dispatch_html = dict(
    p=append_paragraph,
    li=append_list_item,
    br=append_line_break,
    strong=append_bold_run,
    em=append_italic_run,
    h1=append_heading,
    h2=append_heading,
    h3=append_heading,
    h4=append_heading,
    h5=append_heading,
    h6=append_heading,
)
