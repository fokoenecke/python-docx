# encoding: utf-8

"""
Converter recursively iterating over HTML ElementTree(etree)
mapping HTML tags to their corresponding docx create functions.
Appending full HTML structure to the given document.
"""
from docx.html.dispatcher import get_append_call


class DocxBuilder(object):
    """
    Taking the document our html should be appended to
    """
    def __init__(self, document):
        super(DocxBuilder, self).__init__()
        self._document = document

    def from_html_tree(self, root):
        """
        Appending all the HTML elements, beginning at root object
        """
        self._append_docx_elements(root, self._document)

    def _append_docx_elements(self, html_element, container):
        """
        Retrieving and calling a creating function for
        the given HTML tag. Recursive call for all
        children of the element.
        """
        append_call = get_append_call(html_element.tag)
        # only call when a function is attached to tag
        new_container = container
        if append_call:
            new_container = append_call(html_element, container)

        children = list(html_element)
        for child in children:
            self._append_docx_elements(child, new_container)
