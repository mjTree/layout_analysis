# coding:utf-8
import fitz
from fitz.fitz import Document as MupdfDocument
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTChar, LTTextBoxHorizontal

from layout_analysis.document_structure.document import Document
from layout_analysis.document_structure.module.character import Character
from layout_analysis.document_structure.module.page import Page
from layout_analysis.document_structure.module.text_range import TextRange
from layout_analysis.document_structure.page_element.page_paragraph import PageParagraph


class PdfParse:

    def __init__(self, parse_pdf_path):
        self.parse_pdf_path = parse_pdf_path

    def gen_document_by_pdfminer(self):
        page_list = []
        for page_idx, lt_page in enumerate(extract_pages(self.parse_pdf_path)):
            page: Page = Page(lt_page.width, lt_page.height, page_idx + 1, [])
            for lt_text_box in lt_page._objs:
                if not isinstance(lt_text_box, LTTextBoxHorizontal):
                    continue
                for lt_text_line in lt_text_box._objs:
                    text_range_chars = []
                    for lt_char in lt_text_line._objs:
                        if not isinstance(lt_char, LTChar):
                            continue
                        # 过滤pdf可视界面外的字符
                        if lt_char.x0 >= 0 and lt_char.y0 >= 0 and lt_char.width > 0 and lt_char.height > 0:
                            text_range_chars.append(Character(
                                round(lt_char.x0, 2),
                                round(lt_page.height - lt_char.y0 - lt_char.height, 2),
                                round(lt_char.width, 2),
                                round(lt_char.height, 2),
                                page_idx + 1,
                                lt_char._text,
                                lt_char.fontname,
                            ))
                    if text_range_chars:
                        text_range = TextRange(text_range_chars)
                        page.element_list.append(PageParagraph(page, [text_range], priority=10))
            page_list.append(page)
        return Document(page_list)

    def gen_document_by_pymupdf(self):
        page_list = []
        mupdf_document = MupdfDocument(self.parse_pdf_path)
        for page_idx, mupdf_page in enumerate(mupdf_document):
            page = Page(mupdf_page.rect.width, mupdf_page.rect.height, page_idx + 1, [])
            raw_dict = page.get_text(option='rawdict', flags=fitz.TEXT_PRESERVE_IMAGES)
            for block in raw_dict['blocks']:
                if block['type'] != 0:
                    continue
                for line in block['lines']:
                    for span in line['spans']:
                        text_range_chars = []
                        for char in span['chars']:
                            x1, y1, x2, y2 = char['bbox']
                            width, height = x2 - x1, y2 - y1
                            # color = span['color']
                            if x1 >= 0 and y1 >= 0 and width > 0 and height > 0:
                                text_range_chars.append(Character(
                                    round(x1, 2),
                                    round(y1, 2),
                                    round(width, 2),
                                    round(height, 2),
                                    page_idx + 1,
                                    char['c'],
                                    span['font'],
                                ))
                        if text_range_chars:
                            text_range = TextRange(text_range_chars)
                            page.element_list.append(PageParagraph(page, [text_range], priority=10))
            page_list.append(page)
        return Document(page_list)
