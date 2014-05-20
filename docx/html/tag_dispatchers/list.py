# encoding: utf-8
from docx.html.tag_dispatchers import TagDispatcher, replace_whitespaces

# map of HTML list tags and their docx styles
from docx.text import Paragraph

_list_style = dict(
    ol='ListNumber',
    ul='ListBullet',
)


class ListDispatcher(TagDispatcher):
    def __init__(self):
        super(ListDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_list_item(element, element.text, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_list_item(element, element.tail, container)

    @classmethod
    def _append_list_item(cls, element, text, container):
        """
        <li> Create a list item element inside a docx container from.
        Choose the style depending on its HTML parents class
        """
        style = _list_style.get(element.getparent().tag, 'ListBullet')
        text = replace_whitespaces(text)
        text = '' if text == ' ' else text

        if isinstance(container, Paragraph):
            container.add_run(text=text, style=style)
            return container
        return container.add_paragraph(text=text, style=style)