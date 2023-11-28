# coding:utf-8
from layout_analysis.document_structure.interface.range import Range


class TextRange(Range):

    def __init__(self, character_list):
        if character_list:
            start_char, end_char = character_list[0], character_list[-1]
            x = start_char.x
            y = start_char.y
            width = end_char.x + end_char.width - x
            height = max([char.height for char in character_list])
        else:
            x, y, width, height = 0, 0, 0, 0
        Range.__init__(self, x, y, width, height)
        self.character_list = character_list

    @property
    def content(self):
        return ''.join([character.char for character in self.character_list])

    def serialization(self, resource):
        pass

    @classmethod
    def deserialization(cls, resource):
        pass

    def __str__(self):
        return self.content
