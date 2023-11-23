# coding:utf-8
from layout_analysis.common.const import DEFAULT_ELEMENT_PRIORITY
from layout_analysis.document_structure.page_element.abstract_page_element import AbstractPageElement


class PageTable(AbstractPageElement):

    def __init__(self, page, x, y, width, height, cells, mask, border_lines, element_id=''):
        text_range_list = []
        AbstractPageElement.__init__(self, page, text_range_list, DEFAULT_ELEMENT_PRIORITY, x, y, width, height,
                                     element_id)
        self.cells = cells
        self.mask = mask
        self.border_lines = border_lines

    @property
    def element_type(self):
        return 'page_table'
