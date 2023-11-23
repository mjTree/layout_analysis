# coding:utf-8
import unittest

from layout_analysis.document_structure.module.character import Character
from layout_analysis.document_structure.document import Document
from layout_analysis.document_structure.module.page import Page
from layout_analysis.document_structure.page_element.page_paragraph import PageParagraph
from layout_analysis.document_structure.module.text_range import TextRange


class TestDocumentStructure(unittest.TestCase):

    def setUp(self):
        ...

    def test_build_document(self):
        page_list = []
        for page_num in range(1, 3):
            character_list = []
            page = Page(1123, 794, page_num, [])  # A4-96dpi
            for index in range(1, 11):
                character_list.append(Character(index, index, 1, 1, page_num, str(index)))
            text_range = TextRange(character_list)
            page_paragraph = PageParagraph(page, [text_range], priority=10)
            page.element_list.append(page_paragraph)
            page_list.append(page)
        document = Document(page_list)
        self.assertEqual(len(document.page_list), 2)

    def tearDown(self):
        ...


if __name__ == "__main__":
    unittest.main()
