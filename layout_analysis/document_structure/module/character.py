# coding:utf-8
from layout_analysis.document_structure.interface.range import Range


class Character(Range):
    __slots__ = (
        'page_num',
        'char',
        'font_name',
    )

    def __init__(self, x, y, width, height, page_num, char, font_name=''):
        Range.__init__(self, x, y, width, height)
        self.page_num = page_num
        self.char = char
        self.font_name = font_name

    def serialization(self, resource):
        pass

    @classmethod
    def deserialization(cls, resource):
        pass
