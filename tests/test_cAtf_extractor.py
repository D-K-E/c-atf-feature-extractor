# Credits ------------------------

__author__ = "Doğu Kaan Eraslan <kaaneraslan@gmail.com>"

__license__ = "MIT License, see LICENSE"

# ---------------------------------

# Packages --------------------------

import os

current_dir = os.getcwd()

os.chdir("../")

# -----------------------------------------------
# Import modules from main directory ----------

from catf_feature_extractor.extractor import cAtfFeatExtractor


# Return to Current Directory for importing texts

os.chdir(current_dir)

import unittest
import ast


# ------------------------------------------

# Test File ----------------------------------

print(os.getcwd())

with open("Modified_P462811_reasonableText.txt","r",encoding="utf-8", newline="\n") as f:
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
        # DONE
        atf_section = self.textClass.get_atf_section()
        with open("atf_section.txt","r",encoding="utf-8", newline="\n") as test:
#            test.write(atf_section)
            atf_read = test.read()
        #
        self.assertEqual(atf_section, atf_read)
    #
    def test_get_object_parts_textBuilderClass(self):
        """
        tests if we can get the object parts
        from the isolated section
        """
        # DONE
        object_part_list = self.textClass.get_object_parts()
        with open("test_object_part_list_textBuilderClass.txt","r",encoding="utf-8", newline="\n") as part:
            objPart_list_str = part.read()
            check_objPart_list = ast.literal_eval(objPart_list_str)
        #
        self.assertEqual(object_part_list, check_objPart_list)
    #
    def test_splitLinesOParts_textBuilderClass(self):
        """
        Tests if the object parts in the list can be seperated
        correctly into lines.
        """
        # DONE
        #
        object_part_line_list = self.textClass.splitLinesOParts()
        #
        with open("test_split_object_part_textBuilderClass.txt","r", encoding="utf-8", newline="\n") as f:
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
        # DONE
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
        # DONE
        #
        object_id = self.textClass.get_text_id()
        oId = {'text_id': 'P462811',
               'text_language': 'akk'}
        #
        self.assertEqual(object_id, oId)
    #
    def test_set_textLang_textBuilderClass(self):
        """
        test setting textLang attribute
        """
        # DONE
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
        # DONE
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
        # DONE
        textParts = self.textClass.get_textParts()
        # TODO Nested object parts should be dealt with
        # here
        with open("test_get_textParts_textBuilderClass.txt","r",encoding="utf-8", newline="\n") as f:
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
        # DONE
        #
        with open("test_get_textParts_textBuilderClass.txt","r",encoding="utf-8", newline="\n") as f:
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
        # DONE
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
        # DONE
        #
        range_list = [[0, 1, 2, 3], [3, 4, 5, 6], [7, 8, 9]]
        # Notice the 3 is in i and i + 1, whereas 6 is only in i.
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
        # DONE
        #
        partHierarchy = self.textClass.set_partHierarchy()
        check_partHierarchy = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [7, 8]]
        #
        self.assertEqual(partHierarchy, check_partHierarchy)
    #
    def test_set_text_PartInfo_textBuilderClass(self):
        """
        test for method which sets the info related to part
        to text_dict
        """
        # DONE
        #
        part_info = self.textClass.set_text_PartInfo()
        check_part_info = {'text_id': 'P462811',
                           'text_language': 'akk',
                           'text_objectType': '@object composite text',
        'text_textPartCount': 9}
        #
        self.assertEqual(part_info, check_part_info)
    #
    def test_textPartString_textBuilderClass(self):
        """
        Tests for method getting the str representation
        of the part.
        """
        # DONE
        #
        textpart = ['@column 1',
                    '1. qe2-reb hur-sza2-a-ni zaq-ru-te _a-sza3_ nam-ra-s,i i-na _ansze-kur-ra_ ar-kab-ma _{gesz}gigir giri3-min_-ia i-na ti-ik-ka-a-te u2-sza2-asz2-szi asz2-ru szup-szu-qu i-na _giri3-min_-ia ri-ma-nisz at-tag-gisz',
        '2. {iri}e2-{disz}ki-lam-za-ah _iri_ dan-nu-ti-szu2-nu al-me ak-szud{ud} _ug3-mesz tur gal ansze-kur-ra-mesz {ansze}kunga-mesz ansze-mesz gu4-mesz_ u3 _us5-udu hi-a_ ul-tu qer-bi-szu u2-sze-s,a-am-ma szal-la-tisz am-nu']
        textpart_str = self.textClass.textPartString(textpart)
        check_part_str = """1. qe2-reb hur-sza2-a-ni zaq-ru-te _a-sza3_ nam-ra-s,i i-na _ansze-kur-ra_ ar-kab-ma _{gesz}gigir giri3-min_-ia i-na ti-ik-ka-a-te u2-sza2-asz2-szi asz2-ru szup-szu-qu i-na _giri3-min_-ia ri-ma-nisz at-tag-gisz\n2. {iri}e2-{disz}ki-lam-za-ah _iri_ dan-nu-ti-szu2-nu al-me ak-szud{ud} _ug3-mesz tur gal ansze-kur-ra-mesz {ansze}kunga-mesz ansze-mesz gu4-mesz_ u3 _us5-udu hi-a_ ul-tu qer-bi-szu u2-sze-s,a-am-ma szal-la-tisz am-nu"""
        #
        self.assertEqual(textpart_str, check_part_str)
        #
    def test_get_ALs_textBuilderClass(self):
        """
        tests the part level Another Language getter.
        """
        #
        # DONE
        part_str = """1. qe2-reb hur-sza2-a-ni zaq-ru-te _a-sza3_ nam-ra-s,i i-na _ansze-kur-ra_ ar-kab-ma _{gesz}gigir giri3-min_-ia i-na ti-ik-ka-a-te u2-sza2-asz2-szi asz2-ru szup-szu-qu i-na _giri3-min_-ia ri-ma-nisz at-tag-gisz\n2. {iri}e2-{disz}ki-lam-za-ah _iri_ dan-nu-ti-szu2-nu al-me ak-szud{ud} _ug3-mesz tur gal ansze-kur-ra-mesz {ansze}kunga-mesz ansze-mesz gu4-mesz_ u3 _us5-udu hi-a_ ul-tu qer-bi-szu u2-sze-s,a-am-ma szal-la-tisz am-nu"""
        test_als = self.textClass.get_ALs(part_str)
        #
        with open("test_get_ALs_textBuilderClass.txt","r",encoding="utf-8", newline="\n") as f:
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
        with open("test_lineDict_textBuilderClass.txt","r", encoding="utf-8", newline="\n") as f:
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
        word_dict = self.textClass.worDictBuilder("ak-szud{ud}")
        #
        with open("test_wordDictBuilder_textBuilderClass.txt","r", encoding="utf-8", newline="\n") as f:
            word_dict_str = f.read()
            wordDict = ast.literal_eval(word_dict_str)
        #
        self.assertEqual(word_dict, wordDict)
    #
    def test_signDictBuilder_textBuilderClass(self):
        """
        tests the sign dict builder for text builder
        """
        # DONE
        #
        sign = "|AN.IR3.((BAR@t~a@TAM2@k~v).MESZ+AN)+AN|#"
        signDict = self.textClass.signDictBuilder(sign)
        #
        with open("test_signDictBuilder_textBuilderClass.txt","r",encoding="utf-8", newline="\n") as f:
            sign_dict_str = f.read()
            check_signDict = ast.literal_eval(sign_dict_str)
        #
        self.assertEqual(signDict, check_signDict)
    #
    def test_get_SignDicts_textBuilderClass(self):
        """
        tests the sign dict builder for text builder
        """
        # DONE
        #
        with open("test_wordDictBuilder_textBuilderClass.txt","r", encoding="utf-8", newline="\n") as f:
            word_dict_str = f.read()
            wordDict = ast.literal_eval(word_dict_str)
        #
        signDict = self.textClass.get_SignDicts(wordDict)
        #
        with open("test_get_signDicts_textClassBuilder.txt","r", encoding="utf-8",newline="\n") as sign:
            sign_dict_str = sign.read()
            check_sign_dict = ast.literal_eval(sign_dict_str)
        #
        self.assertEqual(signDict, check_sign_dict)
        #
    #
    def test_get_WordDicts_textBuilderClass(self):
        """
        tests the word dict builder for text builder
        """
        # TODO Test Fails change the second
        # file to write then retry
        with open("test_lineDict_textBuilderClass.txt","r", encoding="utf-8", newline="\n") as f:
            line_dict_str = f.read()
            lineDict = ast.literal_eval(line_dict_str)
        #
        line_dict = self.textClass.get_WordDicts(lineDict)
        #
        with open("test_get_wordDicts_textBuilderClass.txt","r", encoding="utf-8", newline="\n") as fi:
            check_line_dict_str = fi.read()
            check_line_dict = ast.literal_eval(check_line_dict_str)
        #
        self.assertEqual(line_dict, check_line_dict)
        #
    #
    def test_set_partDict_textBuilderClass(self):
        """
        tests the set_partDict method of textBuilderClass
        """
        #
        #
        textpart = ['@column 1',
                    '1. qe2-reb hur-sza2-a-ni zaq-ru-te _a-sza3_ nam-ra-s,i i-na _ansze-kur-ra_ ar-kab-ma _{gesz}gigir giri3-min_-ia i-na ti-ik-ka-a-te u2-sza2-asz2-szi asz2-ru szup-szu-qu i-na _giri3-min_-ia ri-ma-nisz at-tag-gisz',
                    '2. {iri}e2-{disz}ki-lam-za-ah _iri_ dan-nu-ti-szu2-nu al-me ak-szud{ud} _ug3-mesz tur gal ansze-kur-ra-mesz {ansze}kunga-mesz ansze-mesz gu4-mesz_ u3 _us5-udu hi-a_ ul-tu qer-bi-szu u2-sze-s,a-am-ma szal-la-tisz am-nu']
        #
        part_dict = self.textClass.set_partDict(textpart)
        #
        with open("test_set_partDict_textBuilderClass.txt","r", encoding="utf-8", newline="\n") as fi:
            check_part_dict_str = fi.read()
            check_part_dict = ast.literal_eval(check_part_dict_str)
        #
        self.assertEqual(part_dict, check_part_dict)
    #
    def test_buildTextDict_FP_textBuilderClass(self):
        """
        Tests the buildTextDict_FP method of textbuilder class
        """
        #
        text_dict_fp = self.textClass.buildTextDict_FP()
        #
        with open("test_buildTextDict_FP_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            check_text_dict_str = fi.read()
            check_text_dict_FP = ast.literal_eval(check_text_dict_str)
            #
        #
        self.assertEqual(text_dict_fp, check_text_dict_FP)
    #
    # TODO write the tests for set_lineStack 
    #
    def test_relSignSetter_textBuilderClass(self):
        """
        Tests the relSignSetter method of textBuilderClass
        """
        #
        with open("test_buildTextDict_FP_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            check_text_dict_str = fi.read()
            text_dict_fp = ast.literal_eval(check_text_dict_str)
        #
        self.textClass.catf_text_dict = text_dict_fp
        sign_catf_dict = self.textClass.relSignSetter()
        rel_sign_list = sign_catf_dict["text_RelSignPositions"]
        #
        with open("test_relSignSetter_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            check_rel_sign_list_str = fi.read()
            check_rel_sign_list = ast.literal_eval(check_rel_sign_list_str)
        #
        self.assertEqual(rel_sign_list, check_rel_sign_list)
    #
    def test_relWordSetter_textBuilderClass(self):
        """
        Tests relWordSetter method of textBuilderClass
        """
        #
        with open("test_buildTextDict_FP_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            check_text_dict_str = fi.read()
            text_dict_fp = ast.literal_eval(check_text_dict_str)
        #
        self.textClass.catf_text_dict = text_dict_fp
        #
        with open("test_relSignSetter_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            rel_sign_list_str = fi.read()
            rel_sign_list = ast.literal_eval(rel_sign_list_str)
        #
        self.textClass.catf_text_dict["text_RelSignPositions"] = rel_sign_list
        rel_word_dict = self.textClass.relWordSetter()
        #
        with open("test_relWordSetter_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            check_rel_word_list_str = fi.read()
            check_rel_word_list = ast.literal_eval(check_rel_word_list_str)
        #
        rel_word_list = rel_word_dict["text_RelWordPositions"]
        #
        self.assertEqual(check_rel_word_list, rel_word_list)
    #
    def test_relLineSetter_textBuilderClass(self):
        """
        Tests the relLineSetter method of textBuilderClass
        """
        #
        with open("test_buildTextDict_FP_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            check_text_dict_str = fi.read()
            text_dict_fp = ast.literal_eval(check_text_dict_str)
        #
        self.textClass.catf_text_dict = text_dict_fp
        #
        with open("test_relSignSetter_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            rel_sign_list_str = fi.read()
            rel_sign_list = ast.literal_eval(rel_sign_list_str)
        #
        self.textClass.catf_text_dict["text_RelSignPositions"] = rel_sign_list
        #
        with open("test_relWordSetter_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            rel_word_list_str = fi.read()
            rel_word_list = ast.literal_eval(rel_word_list_str)
        #
        self.textClass.catf_text_dict["text_RelWordPositions"] = rel_word_list
        rel_line_dict = self.textClass.relLineSetter()
        rel_line_list = rel_line_dict["text_RelLinePositions"]
        #
        with open("test_relLineSetter_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            check_rel_line_list_str = fi.read()
            check_rel_line_list = ast.literal_eval(check_rel_line_list_str)
        #
        self.assertEqual(rel_line_list, check_rel_line_list)
    #
    def test_buildTextDict_SP_textBuilderClass(self):
        """
        Tests the buildTextDict_SP method of textBuilderClass
        """
        #
        text_dict_sp = self.textClass.buildTextDict_SP()
        #
        with open("test_buildTextDict_SP_textBuilderClass.txt","r",encoding="utf-8",newline="\n") as fi:
            #
            check_text_dict_str = fi.read()
            check_text_dict_SP = ast.literal_eval(check_text_dict_str)
            #
        #
        self.assertEqual(text_dict_sp, check_text_dict_SP)











