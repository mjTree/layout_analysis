# coding:utf-8
from layout_analysis.document_structure.interface.serializer import Serializer


class Document(Serializer):

    def __init__(self, page_list):
        self.page_list = page_list

    def serialization(self, resource):
        pass

    @classmethod
    def deserialization(cls, resource):
        pass
