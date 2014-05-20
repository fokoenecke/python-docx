# encoding: utf-8
import re


class TagDispatcher(object):
    def __init__(self):
        super(TagDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        raise NotImplementedError("Implemented in inheriting classes")

    @classmethod
    def append_tail(cls, element, container):
        raise NotImplementedError("Implemented in inheriting classes")


def replace_whitespaces(text):
    """
    replaces multiple whitespaces and line breaks by a single whitespace
    """
    if text:
        text = ' '.join(text.split('\n'))
        text = re.sub(' +', ' ', text)

    return text if text else ''