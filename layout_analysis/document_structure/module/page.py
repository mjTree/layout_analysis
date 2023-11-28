# coding:utf-8
from layout_analysis.document_structure.interface.range import Range


class Page(Range):

    def __init__(self, width, height, page_num, element_list):
        Range.__init__(self, 0, 0, width, height)
        self.page_num = page_num
        self.element_list = element_list or []

    @property
    def content(self):
        return ''.join([element.content for element in self.element_list])

    def serialization(self, resource):
        pass

    @classmethod
    def deserialization(cls, resource):
        pass

