# encoding: utf-8

"""
Returns corresponding objects to call for creating
the different docx elements.
"""
from docx.html.tag_dispatchers.blockquote import BlockquoteDispatcher
from docx.html.tag_dispatchers.code import CodeDispatcher
from docx.html.tag_dispatchers.emphasis import EmphasisDispatcher
from docx.html.tag_dispatchers.heading import HeadingDispatcher
from docx.html.tag_dispatchers.linebreak import LineBreakDispatcher
from docx.html.tag_dispatchers.link import LinkDispatcher
from docx.html.tag_dispatchers.list import ListDispatcher
from docx.html.tag_dispatchers.paragraph import ParagraphDispatcher
from docx.html.tag_dispatchers.strong import StrongDispatcher


def get_tag_dispatcher(html_tag):
    """
    Returning the object creating OOXML for the given HTML tag
    """
    return _dispatch_html.get(html_tag)


# map of HTML tags and their corresponding objects
heading_dispatcher = HeadingDispatcher()
_dispatch_html = dict(
    p=ParagraphDispatcher(),
    a=LinkDispatcher(),
    li=ListDispatcher(),
    br=LineBreakDispatcher(),
    code=CodeDispatcher(),
    strong=StrongDispatcher(),
    em=EmphasisDispatcher(),
    h1=heading_dispatcher,
    h2=heading_dispatcher,
    h3=heading_dispatcher,
    h4=heading_dispatcher,
    h5=heading_dispatcher,
    h6=heading_dispatcher,
    blockquote=BlockquoteDispatcher(),
)
