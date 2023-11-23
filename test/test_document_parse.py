# coding:utf-8
import unittest

from layout_analysis.document_parse.pdf_parse import PdfParse
from layout_analysis.document_structure.document import Document


class TestDocumentParse(unittest.TestCase):

    def setUp(self):
        ...

    def test_pdfminer_parse(self):
        pdf_parse: PdfParse = PdfParse('***.pdf')
        document: Document = pdf_parse.gen_document_by_pdfminer()
        self.assertTrue(len(document.page_list) > 0)

    def tearDown(self):
        ...


if __name__ == "__main__":
    unittest.main()
