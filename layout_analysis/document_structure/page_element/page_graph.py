# coding:utf-8
from layout_analysis.common.const import DEFAULT_ELEMENT_PRIORITY
from layout_analysis.document_structure.page_element.abstract_page_element import AbstractPageElement


class PageGraph(AbstractPageElement):

    def __init__(self, page, text_range_list, x, y, width, height, element_id=''):
        if not all((x, y, width, height)):
            raise Exception(f'there is an empty value in {[x, y, width, height]}')
        AbstractPageElement.__init__(self, page, text_range_list, DEFAULT_ELEMENT_PRIORITY, x, y, width, height,
                                     element_id)

    @property
    def element_type(self):
        return 'page_graph'
