# Credits ------------------------

__author__ = "Doğu Kaan Eraslan <kaaneraslan@gmail.com>"

__license__ = "MIT License, see LICENSE"

# ---------------------------------

# Packages --------------------------

import sys

sys.path.append("../")

from catf_feature_extractor.extractor import cAtfFeatExtractor

import unittest
import ast


# ------------------------------------------

# Test File ----------------------------------

with open("Modified_P462811.txt","r",encoding="utf-8", newline="\n") as f:
    test_file = f.read()



class testCatfFeatExtractor(unittest.TestCase):
    """
    Test Functions for cAtfFeatExtractor
    """
    #
    textClass = cAtfFeatExtractor.cAtfTextBuilder(test_file)
    #
    def test_get_atf_section_textBuilderClass(self):
        """
        tests if it can isolate the
        transliteration section which involves only
        one text.
        """
        atf_section = self.textClass.get_atf_section()
        with open("atf_section.txt","r",encoding="utf-8", newline="\n") as test:
            atf_read = test.read()
        #
        self.assertEqual(atf_section, atf_read)
    #
    def test_get_object_parts_textBuilderClass(self):
        """
        tests if we can get the object parts
        from the isolated section
        """
        object_part_list = self.textClass.get_object_parts()
        with open("part_list.txt","r",encoding="utf-8", newline="\n") as part:
            objPart_list_str = part.read()
            objPart_list = ast.literal_eval(objPart_list_str)
        #
        self.assertEqual(object_part_list, objPart_list)
    #
    def test_splitLinesOParts_textBuilderClass(self):
        """
        Tests if the object parts in the list can be seperated
        correctly into lines.
        """
        #
        object_part_line_list = self.textClass.splitLinesOParts()
        #
        with open("Osplitlines.txt","r", encoding="utf-8", newline="\n") as f:
            lines = f.read()
            line_list = ast.literal_eval(lines)
        #
        self.assertEqual(object_part_line_list, line_list)
    #
    def test_get_ObjectIdPart_textBuilderClass(self):
        """
        Tests the isolation of the part in which the text
        has an id.
        """
        #
        object_id_part = self.textClass.get_ObjectIdPart()
        part_list = ['&P462811 = RINAP 3/1 Sennacherib 03 composite ', 'atf: lang akk ']
        #
        self.assertEqual(object_id_part, part_list)
    #
    def test_get_text_id_textBuilderClass(self):
        """
        Tests getting the id from id part.
        """
        #
        object_id = self.textClass.get_text_id()
        oId = {'text_id': 'P462811', 'text_language': 'akk'}
        #
        self.assertEqual(object_id, oId)
    #
    def test_set_textLang_textBuilderClass(self):
        """
        test setting textLang attribute
        """
        #
        textLang = self.textClass.set_textLang()
        text_lang = "akk"
        #
        self.assertEqual(textLang, text_lang)
    #
    def test_get_objectTypePart_textBuilderClass(self):
        """
        test getting object type parts.
        """
        #
        objectType = self.textClass.get_objectTypePart()
        object_type = "@object composite text"
        #
        self.assertEqual(objectType, object_type)
    #
    def test_get_textParts_textBuilderClass(self):
        """
        tests getting the text parts from the separated object parts
        list
        """
        #
        textParts = self.textClass.get_textParts()
        # TODO Nested object parts should be dealt with
        # here
        with open("textpartList.txt","r",encoding="utf-8", newline="\n") as f:
            checkTextParts = f.read()
            textPart_list = ast.literal_eval(checkTextParts)
        #
        self.assertEqual(textParts, textPart_list)
        #
    #
    def test_get_single_lines_textBuilderClass(self):
        """
        tests getting the single lines in the
        text parts
        """
        #
        with open("textpartList.txt","r",encoding="utf-8", newline="\n") as f:
            checkTextParts = f.read()
            textPart_list = ast.literal_eval(checkTextParts)
        single_line_list = self.textClass.get_single_lines(textPart_list)
        check_single_line_list = [0, 3, 6, 7, 9]
        #
        self.assertEqual(single_line_list, check_single_line_list)
    #
    def test_set_textRange_list_textBuilderClass(self):
        """
        tests if it can establish the ranges from the single line
        list.
        """
        #
        single_line_list = [0, 3, 6, 7, 9]
        range_list = self.textClass.set_textRange_list(single_line_list)
        check_range_list = [[0, 1, 2, 3], [3, 4, 5, 6], [7, 8, 9]]
        #
        self.assertEqual(range_list, check_range_list)
    #
    def test_get_partHierarchy_textBuilderClass(self):
        """
        tests getting the part hierarchy from the range list
        """
        #
        range_list = [[0, 1, 2, 3], [3, 4, 5, 6], [7, 8, 9]]
        # Notice the 3 is in i and i + 1 whereas 6 is only in i.
        part_hierarchy = self.textClass.get_partHierarchy(range_list)
        #
        check_partHierarchy = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [7, 8]]
        #
        self.assertEqual(part_hierarchy, check_partHierarchy)
        #
    def test_set_partHierarchy_textBuilderClass(self):
        """
        Tests setting the part hierarchy, the wrapper method
        for the above methods.
        """
        #
        partHierarchy = self.textClass.set_partHierarchy()
        check_partHierarchy = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [7, 8]]
        #
        self.assertEqual(partHierarchy, check_partHierarchy)
    #
    def test_textPartString_textBuilderClass(self):
        """
        Tests for method getting the str representation
        of the part.
        """
        #
        textpart = self.textClass.objectTextParts[4]
        textpart_str = self.textClass.textPartString(textpart)
        check_part_str = "1. qe2-reb hur-sza2-a-ni zaq-ru-te _a-sza3_ nam-ra-s,i i-na _ansze-kur-ra_ ar-kab-ma _{gesz}gigir giri3-min_-ia i-na ti-ik-ka-a-te u2-sza2-asz2-szi asz2-ru szup-szu-qu i-na _giri3-min_-ia ri-ma-nisz at-tag-gisz \n2. {iri}e2-{disz}ki-lam-za-ah _iri_ dan-nu-ti-szu2-nu al-me ak-szud{ud} _ug3-mesz tur gal ansze-kur-ra-mesz {ansze}kunga-mesz ansze-mesz gu4-mesz_ u3 _us5-udu hi-a_ ul-tu qer-bi-szu u2-sze-s,a-am-ma szal-la-tisz am-nu "
        #
        self.assertEqual(textpart_str, check_part_str)
        #
    def test_get_ALs_textBuilderClass(self):
        """
        tests the part level Another Language getter.
        """
        #
        part_str = "1. qe2-reb hur-sza2-a-ni zaq-ru-te _a-sza3_ nam-ra-s,i i-na _ansze-kur-ra_ ar-kab-ma _{gesz}gigir giri3-min_-ia i-na ti-ik-ka-a-te u2-sza2-asz2-szi asz2-ru szup-szu-qu i-na _giri3-min_-ia ri-ma-nisz at-tag-gisz \n2. {iri}e2-{disz}ki-lam-za-ah _iri_ dan-nu-ti-szu2-nu al-me ak-szud{ud} _ug3-mesz tur gal ansze-kur-ra-mesz {ansze}kunga-mesz ansze-mesz gu4-mesz_ u3 _us5-udu hi-a_ ul-tu qer-bi-szu u2-sze-s,a-am-ma szal-la-tisz am-nu "
        test_als = self.textClass.get_ALs(part_str)
        #
        with open("al_test.txt","r",encoding="utf-8", newline="\n") as f:
            al_txt = f.read()
            al_dictList = ast.literal_eval(al_txt)
        #
        self.assertEqual(test_als, al_dictList)
    #
    def test_lineDicts_textBuilderClass(self):
        """
        tests the line dict builder for text builder.
        """
        #
        text_line = self.textClass.objectTextParts[4][2]
        lineDict = self.textClass.lineDicts(text_line)
        #
        with open("test_lineDict_textBuilder.txt","r", encoding="utf-8", newline="\n") as f:
            line_dict_str = f.read()
            lineDict_eval = ast.literal_eval(line_dict_str)
        #
        self.assertEqual(lineDict_eval, lineDict)
        #
    def test_worDictBuilder_textBuilderClass(self):
        """
        tests the word dict builder for text builder
        """
        #
        word_dict = self.textClass.worDictBuilder("szal-la-tisz")
        #
        with open("testWordDict_textBuilder.txt","r", encoding="utf-8", newline="\n") as f:
            word_dict_str = f.read()
            wordDict = ast.literal_eval(word_dict_str)
        #
        self.assertEqual(word_dict, wordDict)
    #
    def test_signDictBuilder_textBuilderClass(self):
        """
        tests the sign dict builder for text builder
        """
        #
        sign = "|AN.IR3.((BAR@t~a@TAM2@k~v).MESZ+AN)+AN|#"
        signDict = self.textClass.signDictBuilder(sign)
        #
        with open("test_signDict_textClass.txt","r",encoding="utf-8", newline="\n") as f:
            sign_dict_str = f.read()
            check_signDict = ast.literal_eval(sign_dict_str)
        #
        self.assertEqual(signDict, check_signDict)
    #















