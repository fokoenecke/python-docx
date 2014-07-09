# encoding: utf-8
from docx.html.tag_dispatchers import TagDispatcher


class CodeDispatcher(TagDispatcher):
    def __init__(self):
        super(CodeDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_code(element.text, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_code(element.tail, container)

    @classmethod
    def _append_code(cls, text, container):
        """
        <code> Creates a specially styled run inside the given container.
        """
        #TODO find out how to monospace in oodocx
        monospace_style = 'NoSpacing'

        if isinstance(container, Paragraph):
            container.add_run(text=text, style=monospace_style)
            return container

        return container.add_paragraph(text=text, style=monospace_style)