# encoding: utf-8
from docx.html.tag_dispatchers import TagDispatcher, replace_whitespaces
from docx.text import Paragraph


class ParagraphDispatcher(TagDispatcher):
    def __init__(self):
        super(ParagraphDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_paragraph(element.text, element, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_paragraph(element.tail, element, container)

    @classmethod
    def _append_paragraph(cls, text, element, container):
        """
        <p> creates a paragraph element inside a docx container element.
        """
        text = replace_whitespaces(text)
        if not text:
            return container

        style = 'Normal'
        if element.getparent().tag == 'blockquote':
            style = 'IntenseQuote'

        if isinstance(container, Paragraph):
            container.add_run(text=text, style=style)
            return container

        return container.add_paragraph(text=text, style=style)
