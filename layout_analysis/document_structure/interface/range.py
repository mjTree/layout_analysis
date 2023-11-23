# coding:utf-8
from abc import ABC

from layout_analysis.document_structure.interface.serializer import Serializer


class Range(Serializer, ABC):
    __slots__ = (
        'x',
        'y',
        'width',
        'height',
    )

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
