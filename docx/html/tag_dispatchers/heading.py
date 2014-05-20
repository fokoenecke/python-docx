# encoding: utf-8
from docx.html.tag_dispatchers import TagDispatcher


class HeadingDispatcher(TagDispatcher):
    def __init__(self):
        super(HeadingDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_heading(element.text, element.tag, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_heading(element.tail, element.tag, container)

    @classmethod
    def _append_heading(cls, text, tag, container):
        """
        <hx> Creates a heading paragraph inside the document container
        """
        container.add_heading(text=text, level=int(tag[1:]))
