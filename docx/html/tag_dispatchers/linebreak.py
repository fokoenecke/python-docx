# encoding: utf-8
from docx.enum.text import WD_BREAK
from docx.html.tag_dispatchers import TagDispatcher


class LineBreakDispatcher(TagDispatcher):
    def __init__(self):
        super(LineBreakDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_line_break(container)

    @classmethod
    def append_tail(cls, element, container):
        pass

    @classmethod
    def _append_line_break(cls, container):
        """
        <br> Creates a break item inside the given container.
        """
        run = container.add_run()
        run.add_break(break_type=WD_BREAK.LINE_CLEAR_RIGHT)
        return container
