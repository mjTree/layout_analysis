# coding:utf-8
from layout_analysis.document_structure.page_element.abstract_page_element import AbstractPageElement


class PageParagraph(AbstractPageElement):

    @property
    def element_type(self):
        return 'page_paragraph'
