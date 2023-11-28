# coding:utf-8
import uuid
from typing import List, Text

from layout_analysis.document_structure.interface.range import Range
from layout_analysis.document_structure.module.page import Page
from layout_analysis.document_structure.module.text_range import TextRange


class AbstractPageElement(Range):

    def __init__(
            self,
            page: Page,
            text_range_list: List[TextRange],
            priority: int,
            x: float = None,
            y: float = None,
            width: float = None,
            height: float = None,
            element_id: Text = '',
    ):
        if not all((x, y, width, height)):
            x, y, width, height = self.get_page_element_region(text_range_list)
        Range.__init__(self, x, y, width, height)
        self.page = page
        self.text_range_list = text_range_list or []
        self.priority = priority
        self.element_id = element_id or str(uuid.uuid4())

    @property
    def content(self):
        return ''.join([text_range.content for text_range in self.text_range_list])

    @staticmethod
    def get_page_element_region(text_range_list):
        x, y, width, height = 0, 0, 0, 0
        if text_range_list:
            start_char = text_range_list[0].character_list[0]
            x1, y1 = start_char.x, start_char.y
            x2, y2 = start_char.x + start_char.width, start_char.y
            for text_range in text_range_list:
                for character in text_range.character_list:
                    x1 = min(character.x, x1)
                    y1 = min(start_char.y - character.height, y1)
                    x2 = max(character.x + character.width, x2)
                    y2 = max(start_char.y, y2)
            x, y, width, height = x1, y1, x2 - x1, y2 - y1
        return x, y, width, height

    def serialization(self, resource):
        pass

    @classmethod
    def deserialization(cls, resource):
        pass

    def __str__(self):
        return self.content
