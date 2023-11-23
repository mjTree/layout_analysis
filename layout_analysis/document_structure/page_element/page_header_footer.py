# coding:utf-8
from layout_analysis.common.const import DEFAULT_ELEMENT_PRIORITY
from layout_analysis.document_structure.page_element.abstract_page_element import AbstractPageElement


class PageHeaderFooter(AbstractPageElement):

    def __init__(self, page, text_range_list, element_id='', is_header=True):
        x, y, width, height = self.get_page_element_region(text_range_list)
        AbstractPageElement.__init__(self, page, text_range_list, DEFAULT_ELEMENT_PRIORITY, x, y, width, height,
                                     element_id)
        self._is_header = is_header

    @property
    def element_type(self):
        return 'page_header_footer'

    @property
    def is_header(self):
        return self._is_header

    @property
    def is_footer(self):
        return not self._is_header
