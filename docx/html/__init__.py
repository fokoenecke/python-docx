# encoding: utf-8

"""
Wrapper methods used for mapping HTML to docx objects
"""

from lxml.html import fromstring

from docx.html.converter import DocxBuilder


def add_html(document, html_string):
    root = fromstring(html_string)
    builder = DocxBuilder(document=document)
    builder.from_html_tree(root=root)