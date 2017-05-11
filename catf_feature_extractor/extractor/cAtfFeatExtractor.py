"""

A pure python feature extractor for c-atf encoded texts in order to
train classifiers.

"""

# Packages ------------------------------

import re
import itertools

# ---------------------------------

# Credits --------------------------------

__author__ = "Doğu Kaan Eraslan, <kaaneraslan@gmail.com>"
__license__ = "MIT, see LICENSE"

# -----------------------------------------


class cAtfLineTester(object):
    """
    a class for testing lines of c-atf texts
    """
    def __init__(self, atf_line):
        #
        self.cAtf_line = atf_line
        #
    #
    def test_id_line(self):
        """
        params: atf_line, str.
        return: boolean

        Tests if the line starts with &, the id marker.
        """
        #
        find_id_line = re.search("(^&P\d+)", self.cAtf_line)
        #
        if find_id_line is None:
            return False
        else:
            return True
    #
    #
    def test_language_line(self):
        """
        params: atf_line, str.
        return: boolean

        tests if the line gives the language of the text
        """
        #
        find_lang_line = re.search("atf: lang", self.cAtf_line)
        #
        if find_lang_line is None:
            return False
        else:
            return True
    #
    #
    def test_line_content(self):
        """
        params: atf_line, str.
        return: boolean

        Tests if the line is commentary about the line content
        """
        #
        find_line_content_comment = re.search("^#.*", self.cAtf_line)
        #
        if find_line_content_comment is None:
            return False
        else:
            return True
    #
    #
    def test_object_type_object_part(self):
        """
        params: atf_line, str.
        return: boolean

        Tests if the line indicates the object type or object part
        """
        #
        find_object_type_part = re.search("^@.*", self.cAtf_line)
        #
        if find_object_type_part is None:
            return False
        else:
            return True
    #
    #
    def test_text_structure(self):
        """
        params: atf_line, str.
        return: boolean

        Tests if the line belongs to a commentary on the text structure
        """
        #
        find_text_structure = re.search("^\$.*", self.cAtf_line)
        #
        if find_text_structure is None:
            return False
        else:
            return True
    #
    #
    def test_text_line(self):
        """
        params: atf_line, str.
        return: boolean

        Tests if the line belongs to a translitteration of a text
        """
        #
        find_text_line = re.search("^\d.*", self.cAtf_line)
        #
        if find_text_line is None:
            return False
        else:
            return True
    #
    #
    def test_lineHas_anotherLanguage(self):
        """
        params: atf_line, str.
        return: boolean
        """
        #
        find_logogram = re.search("_.*?_", self.cAtf_line)
        #
        if find_logogram is None:
            return False
        else:
            return True



class cAtfALTester(object):
    """
    class for handling another languages in the lines
    """
    #
    def __init__(self):
        #
        self.cAtf_line = ""
        self.al_oc = ""
        self.al_word = ""
        #
    #
    #
    def testALHasPreSign(self, al_oc):
        """
        params: atf_line, str.
        return: boolean

        Test to see if the another language occurence
        has a preeceding sign
        """
        #
        if "-_" in self.cAtf_line or "-_" in al_oc:
            return True
        else:
            return False
    #
    #
    def test_ALHasFolSign(self, al_oc):
        """
        params: atf_line, str.
        return: boolean

        Test to see if the another language occurence
        has a preeceding sign

        """
        #
        if "_-" in self.cAtf_line or "_-" in al_oc:
            return True
        else:
            return False
    #
    #
    def test_ALSwitch(self, cAtf_alWord):
        """
        params: atf_logogram, str.
        return: boolean

        Tests if the occurence have a
        language switch
        """
        #
        if "%" in cAtf_alWord:
            return True
        else:
            return False


def test_wordHasAnotherLanguage(atf_word):
    """
    params: atf_word, str.
    return: boolean
    """
    #
    find_logogram = re.search("_.*?_", atf_word)
    #
    if find_logogram is None:
        return False
    else:
        return True

"""
Logogram bölgesinden
dil değiştiriciyi al
ondan sonra onun içindeki
işaretleri aldığın dilde
kodla
"""


"""
If logogram has more than one space
divide from the space and check if there is
more than two signs -

if the logograme has space
see if there is a phonetic complement of the logogramme after the _

see if the logogramme has a sign following
or preeceding it.

see 

uppercase = unknown reading.

"""

# Word level Tests

# Sign Level Tests -------------------------------

class cAtfWordTester(object):
    """
    Class for testing the signs in a word
    """
    #
    def __init__(self, catf_word):
        #
        self.cAtf_word = catf_word
    #
    #
    @staticmethod
    def test_String(string1,string2):
        """
        Returns true if string2
        contains string1
        """
        #
        if string1 in string2:
            return True
        else:
            return False
    #
    def test_damaged_sign(self):
        """
        params: atf_word, str.
        return: boolean
        """
        #
        find_damage_sign = re.search("\w+#", self.cAtf_word)
        #
        if find_damage_sign is None:
            return False
        else:
            return True
    #
    #
    def test_determinative_sign(self):
        """
        params: atf_word, str.
        return: boolean
        """
        #
        find_determinative_sign = re.search("\{\w.*?\}",self.cAtf_word)
        #
        if find_determinative_sign is None:
            return False
        else:
            return True
    #
    #
    def test_isNumber(self):
        """
        params: atf_word, str.
        return: boolean
        """
        #
        number_form_1 = re.search("\d+\(\w+.*?\)", self.cAtf_word)
        number_form_2 = re.search("n\(\w+.*?\)", self.cAtf_word)
        number_form_3 = re.search("n\+\d+\(\w+.*?\)", self.cAtf_word)
        #
        if number_form_1 is None and number_form_2 is None and number_form_3 is None:
            return False
        else:
            return True
    #
    def test_isNumberF1(self):
        """
        params: atf_word, str.
        return: boolean
        """
        number_form_1 = re.search("\d+\(\w+.*?\)", self.cAtf_word)
        #
        if number_form_1 is None:
            return False
        else:
            return True
    #
    def test_isNumberF2(self):
        """
        params: atf_word, str.
        return: boolean
        """
        #
        number_form_2 = re.search("n\(\w+.*?\)", self.cAtf_word)
        #
        if number_form_2 is None:
            return False
        else:
            return True
    #
    def test_isNumberF3(self):
        """
        params: atf_word, str.
        return: boolean
        """
        #
        number_form_3 = re.search("n\+\d+\(\w+.*?\)", self.cAtf_word)
        #
        if number_form_3 is None:
            return False
        else:
            return True

    # Punctuation Tests -----------
    #
    def test_isColon(self):
        """
        returns true if the word
        has :
        """
        #
        if ":" == self.cAtf_word or "P2" == self.cAtf_word:
            return True
        else:
            return False
        #
    #
    def test_isDColon(self):
        """
        returns true if the word
        is ::
        """
        #
        if "::" == self.cAtf_word:
            return True
        else:
            return False
    #
    def test_isColonRQ(self):
        """
        returns true if the word
        is :'
        """
        #
        if ":'" == self.cAtf_word or "MZL592~b" == self.cAtf_word:
            return True
        else:
            return False
    #
    def test_isColonDQ(self):
        """
        returns true if the word
        is :"
        """
        #
        if ':"' == self.cAtf_word or "P3" == self.cAtf_word:
            return True
        else:
            return False
    #
    def test_isDoubleColon(self):
        """
        returns true if the word
        is ::
        """
        if "::" == self.cAtf_word:
            return True
        else:
            return False
        #
    #
    def test_isColonPoint(self):
        """
        returns true if the word
        is :.
        """
        #
        if ":." == self.cAtf_word or "P4" == self.cAtf_word:
            return True
        else:
            return False
    #
    def test_isWordDivider(self):
        """
        returns true if the word
        is /
        """
        if "/" == self.cAtf_word or "P1" == self.cAtf_word:
            return True
        else:
            return False
    #
    def test_isWordDivider_Specified(self):
        """
        returns true if the word has
        /(
        """
        #
        return self.test_String("/(", self.cAtf_word)
    #
    def test_isBullet(self):
        """
        returns true if the word is
        *
        """
        #
        if "*" == self.cAtf_word:
            return True
        else:
            return False
    #
    def test_isBulletSpeficied(self):
        """
        checks if the word has the
        structure of *(Grapheme)
        """
        #
        if re.search("^\*\(.*?\)", self.cAtf_word) is not None:
            return True
        else:
            return False
    #


    #
    # Individual Sign Tests ------------
    #
    def test_has_complement(self):
        """
        Returns true if the sign has
        +
        """
        #
        if "+" in self.cAtf_word:
            return True
        else:
            return False
        #
    #
    def test_has_unknownReading(self):
        """
        Returns true if the sign
        is uppercase
        """
        #
        if self.cAtf_word.isupper() is True:
            return True
        else:
            return False
        #
    #
    def test_has_compound(self):
        """
        Returns true if the sign
        has |
        """
        #
        return self.test_String("|", self.cAtf_word)
    #
    def test_has_specification(self):
        """
        Returns true if the sign
        has (
        """
        #
        return self.test_String("(", self.cAtf_word)
    #
    def test_has_query(self):
        """
        Returns true if the sign
        has ?
        """
        #
        return self.test_String("?", self.cAtf_word)
    #
    def test_has_collation(self):
        """
        returns true if the sign
        has *
        """
        #
        return self.test_String("*", self.cAtf_word)
    #
    def test_has_correction(self):
        """
        returns true if the sign
        has !
        """
        #
        return self.test_String("!", self.cAtf_word)
    #
    def test_hasCurved(self):
        """
        returns true if the sign
        has @c
        """
        #
        return self.test_String("@c", self.cAtf_word)
    #
    def test_hasFlat(self):
        """
        returns true if the sign
        has @f
        """
        #
        return self.test_String("@f", self.cAtf_word)
    #
    def test_hasGunu(self):
        """
        returns true if the sign has
        @g
        """
        return self.test_String("@g", self.cAtf_word)
    #
    def test_hasSheshig(self):
        """
        returns true if the sign has
        @s
        """
        #
        return self.test_String("@s", self.cAtf_word)
    #
    def test_hasTenu(self):
        """
        returns true if the sign has
        @t
        """
        #
        return self.test_String("@t", self.cAtf_word)
    #
    def test_hasNutillu(self):
        """
        returns true if the sign has
        @n
        """
        #
        return self.test_String("@n", self.cAtf_word)
    #
    def test_hasZidatenu(self):
        """
        returns true if the sign has
        @z
        """
        #
        return self.test_String("@z", self.cAtf_word)
    #
    def test_hasKabatenu(self):
        """
        returns true if the sign
        has @k
        """
        #
        return self.test_String("@k", self.cAtf_word)
    #
    def test_hasVertReflected(self):
        """
        returns true if the sign
        has @r
        """
        #
        return self.test_String("@r", self.cAtf_word)
    #
    def test_hasHorReflected(self):
        """
        returns true if the sign
        has @h
        """
        #
        return self.test_String("@h", self.cAtf_word)
    #
    def test_hasVariant(self):
        """
        returns true if the sign
        has @v
        """
        #
        return self.test_String("@v", self.cAtf_word)
    #
    def test_hasRotated(self):
        """
        returns true if the
        sign has @\d+
        """
        #
        if re.search("@\d+",self.cAtf_word) is not None:
            return True
        else:
            return False
    #
    # Compound Sign Tests ------------------
    #
    def test_hasBeside(self):
        """
        returns true if the
        sign has .
        """
        #
        return self.test_String(".", self.cAtf_word)
    #
    def test_hasJoining(self):
        """
        returns true if
        the sign has +
        """
        #
        return self.test_String("+", self.cAtf_word)
    #
    def test_hasAbove(self):
        """
        returns true if the sign
        has &
        """
        #
        return self.test_String("&", self.cAtf_word)
    #
    def test_hasCrossing(self):
        """
        returns true if the sign
        has %
        """
        #
        return self.test_String("%", self.cAtf_word)
    #
    def test_hasAllograph(self):
        """
        returns true if the sign
        has ~
        """
        #
        return self.test_String("~", self.cAtf_word)
    #
    def test_hasSpecialAllograph(self):
        """
        returns true if the sign
        has ~v
        """
        #
        return self.test_String("~v", self.cAtf_word)
    #
    def test_hasFormVariant(self):
        """
        returns true if the sign
        has \
        """
        #
        return self.test_String("\\", self.cAtf_word)
    #
    def test_hasContaining(self):
        """
        returns true if the sign
        has x
        """
        #
        return self.test_String("x", self.cAtf_word)
    #
    def test_hasContaining_Group(self):
        """
        returns true if the sign
        has x(
        """
        #
        return self.test_String("x(", self.cAtf_word)
    #

# TODO Take the sign from numbers


# ----------------------------------------------------

class cAtfSignTester(object):
    """
    Class for testing signs in order to buildinga sign dict afterwards
    """
    #
    def __init__(self, cAtf_Sign):
        #
        self.catf_sign = cAtf_Sign
        #
    #
    @staticmethod
    def test_String(string1,string2):
        """
        Returns true if string2
        contains string1
        """
        #
        if string1 in string2:
            return True
        else:
            return False
    #
    def test_isDamaged(self):
        """
        Returns true if the self.catf_sign
        has #
        """
        #
        return self.test_String("#", self.catf_sign)
        #
    #
    def test_isComplement(self):
        """
        Returns true if the self.catf_sign has
        +
        """
        #
        if self.test_String("+", self.catf_sign) and self.test_isCompound():
            return True
        else:
            return False
    #
    def test_isUnknownReading(self):
        """
        Returns true if the self.catf_sign
        is uppercase
        """
        #
        if self.catf_sign.isupper() is True:
            return True
        else:
            return False
        #
    #
    def test_isCompound(self):
        """
        Returns true if the self.catf_sign
        has |
        """
        #
        return self.test_String("|", self.catf_sign)
    #
    def test_isSpecification(self):
        """
        Returns true if the self.catf_sign
        has (
        """
        #
        return self.test_String("(", self.catf_sign)
    #
    def test_is_query(self):
        """
        Returns true if the self.catf_sign
        has ?
        """
        #
        return self.test_String("?", self.catf_sign)
    #
    def test_is_collation(self):
        """
        returns true if the self.catf_sign
        has *
        """
        #
        return self.test_String("*", self.catf_sign)
    #
    def test_is_correction(self):
        """
        returns true if the self.catf_sign
        has !
        """
        #
        return self.test_String("!", self.catf_sign)
    #
    # Modifier Tests ------------------------
    #
    def test_isCurved(self):
        """
        returns true if the self.catf_sign
        has @c
        """
        #
        return self.test_String("@c", self.catf_sign)
    #
    def test_isFlat(self):
        """
        returns true if the self.catf_sign
        has @f
        """
        #
        return self.test_String("@f", self.catf_sign)
    #
    def test_isGunu(self):
        """
        returns true if the self.catf_sign has
        @g
        """
        return self.test_String("@g", self.catf_sign)
    #
    def test_isSheshig(self):
        """
        returns true if the self.catf_sign has
        @s
        """
        #
        return self.test_String("@s", self.catf_sign)
    #
    def test_isTenu(self):
        """
        returns true if the self.catf_sign has
        @t
        """
        #
        return self.test_String("@t", self.catf_sign)
    #
    def test_isNutillu(self):
        """
        returns true if the self.catf_sign has
        @n
        """
        #
        return self.test_String("@n", self.catf_sign)
    #
    def test_isZidatenu(self):
        """
        returns true if the self.catf_sign has
        @z
        """
        #
        return self.test_String("@z", self.catf_sign)
    #
    def test_isKabatenu(self):
        """
        returns true if the self.catf_sign
        has @k
        """
        #
        return self.test_String("@k", self.catf_sign)
    #
    def test_isVertReflected(self):
        """
        returns true if the self.catf_sign
        has @r
        """
        #
        return self.test_String("@r", self.catf_sign)
    #
    def test_isHorReflected(self):
        """
        returns true if the self.catf_sign
        has @h
        """
        #
        return self.test_String("@h", self.catf_sign)
    #
    def test_isVariant(self):
        """
        returns true if the self.catf_sign
        has @v
        """
        #
        return self.test_String("@v", self.catf_sign)
    #
    def test_isRotated(self):
        """
        returns true if the
        self.catf_sign has @\d+
        """
        #
        if re.search("@\d+",self.catf_sign) is not None:
            return True
        else:
            return False
    #
    def test_isModifier(self):
        """
        returns true
        if the self.catf_sign passes all
        the tests related to modifiers
        """
        #
        if self.test_isRotated(self.catf_sign) is True or self.test_isVariant(self.catf_sign) is True or self.test_isHorReflected(self.catf_sign) is True or self.test_isCurved(self.catf_sign) is True or self.test_isFlat(self.catf_sign) is True or self.test_isGunu(self.catf_sign) is True or self.test_isSheshig(self.catf_sign) is True or self.test_isTenu(self.catf_sign) is True or self.test_isNutillu(self.catf_sign) is True or self.test_isZidatenu(self.catf_sign) is True or self.test_isKabatenu(self.catf_sign) is True or self.test_isVertReflected(self.catf_sign) is True:
            return True
        else:
            return False
    # Compound Self.Catf_Sign Tests ------------------
    #
    @staticmethod
    def test_isBinaryScope(operator):
        """
        Tests if the operator has
        binary scope
        the x and the @ will be
        handled individually
        """
        #
        if operator == "&" or operator == "%":
            return True
        else:
            return False
        #
    #
    def test_hasBeside(self):
        """
        returns true if the
        self.catf_sign has .
        """
        #
        return self.test_String(".", self.catf_sign)
    #
    def test_hasJoining(self):
        """
        returns true if
        the self.catf_sign has +
        """
        #
        return self.test_String("+", self.catf_sign)
    #
    def test_hasContaining(self):
        """
        returns true if the self.catf_sign
        has x
        """
        #
        return self.test_String("x", self.catf_sign)
    #
    def test_hasContaining_Group(self):
        """
        returns true if the self.catf_sign
        has x(
        """
        #
        return self.test_String("x(", self.catf_sign)
    #
    def test_hasAbove(self):
        """
        returns true if the self.catf_sign
        has &
        """
        #
        return self.test_String("&", self.catf_sign)
    #
    def test_hasCrossing(self):
        """
        returns true if the self.catf_sign
        has %
        """
        #
        return self.test_String("%", self.catf_sign)
    #
    def test_hasOpposing(self):
        """
        returns true if the seperated strings
        are in uppercase
        """
        #
        test_list = []
        if self.test_String("@",self.catf_sign) is True:
            rep_string = self.catf_sign.replace("@", " ")
            no_number = re.sub("\d+","", rep_string)
            no_whiteSpace = no_number.replace(" ","")
            if no_whiteSpace.isupper() is True:
                return True
            else:
                return False
        else:
            return False
    #
    def test_hasAllograph(self):
        """
        returns true if the self.catf_sign
        has ~
        """
        #
        return self.test_String("~", self.catf_sign)
    #
    def test_hasSpecialAllograph(self):
        """
        returns true if the self.catf_sign
        has ~v
        """
        #
        return self.test_String("~v", self.catf_sign)
    #
    def test_hasFormVariant(self):
        """
        returns true if the self.catf_sign
        has \
        """
        #
        return self.test_String("\\", self.catf_sign)
    #
    def test_hasRepeated(self):
        """
        returns true if the first
        seperated character is digit
        """
        #
        if self.test_String("x", self.catf_sign) is True:
            str_split = self.catf_sign.split("x")
            if str_split[0].isdigit():
                return True
            else:
                return False
        else:
            return False
    #










# -------------------------------------------

class cAtfLineGetter(cAtfLineTester):
    """
    a class for getting text lines
    according to tests
    """
    #
    def __init__(self, atf_line):
        super().__init__(atf_line)
        self.cAtf_line = atf_line
        self.text_id = ""
        self.text_id_alternatives = []
        self.text_lang = ""
        self.content_comment_line = ""
        self.objectSurface_title = ""
        self.structure_comment = ""
        self.text_line = ""
        self.lineNumber = int()
        self.lineWordCount = int()
        self.lineWords = []
        self.lineText = ""
        #
    #
    def get_id_line(self):
        """
        checks the line for
        conforming the id no syntax,
        then gets it.
        """
        #
        atf_line = self.cAtf_line
        if self.test_id_line() == True:
            text_id_search = re.search("&P\d+\s", atf_line)
            text_id_brut = text_id_search.group(0)
            text_id = text_id_brut[:-1] # Cleans the last space
            self.text_id = text_id[1:] # Cleans the &
        else:
            pass
        #
        return self.text_id
    #
    #
    def get_id_alternatives(self):
        """
        Checks the line for id syntax.
        Gets the id alternatives
       separated with the "=".
        """
        #
        atf_line = self.cAtf_line
        #
        if self.test_id_line() == True:
            text_id_alternative_split = atf_line.split("=")
            text_id_alternative_brut = text_id_alternative_split[1:]
            text_id_alternative = [alternative.strip() for alternative in text_id_alternative_brut]
            self.text_id_alternatives = text_id_alternative
        else:
            pass
        #
        return self.text_id_alternatives
    #
    #
    def get_language_line(self):
        """
        Checks the line for
        language protocol syntax
        Gets the indicated language
        """
        #
        atf_line = self.cAtf_line
        #
        if self.test_language_line() == True:
            text_lang_search = re.search("atf: lang.*", atf_line)
            text_lang_brut = text_lang_search.group(0)
            text_lang = text_lang_brut[len("atf: lang "):].strip()
            self.text_lang = text_lang
        else:
            pass
        #
        return self.text_lang
    #
    #
    def get_content_comment(self):
        """
        Checks the line for
        content comment syntax
        ie #.
        Gets the content comment line
        """
        #
        atf_line = self.cAtf_line
        #
        if self.test_line_content() == True:
            content_comment_search = re.search("^#.*", atf_line)
            content_comment = content_comment_search.group(0)
            self.content_comment_line = content_comment
        else:
            pass
        #
        return self.content_comment_line
    #
    #
    def get_object_part_title(self):
        """
        Checks if the line starts with @.
        Gets the line if it does.
        """
        #
        atf_line = self.cAtf_line
        #
        if self.test_object_type_object_part() == True:
            object_title_search = re.search("^@.*", atf_line)
            object_surface_title = object_title_search.group(0)
            self.objectSurface_title = object_surface_title
        #
        else:
            pass
        #
        return self.objectSurface_title
    #
    #
    def get_structure_comment(self):
        """
        Checks if the line starts with $
        Gets the line if it does.
        """
        #
        atf_line = self.cAtf_line
        #
        if self.test_text_structure() == True:
            structure_comment_search = re.search("^\$.*", atf_line)
            structure_comment = structure_comment_search.group(0)
            self.structure_comment = structure_comment
            #
        else:
            pass
        #
        return self.structure_comment
    #
    #
    def get_text_line(self):
        """
        Checks if the line starts with a \d+.
        Gets the line if it does.
        """
        #
        atf_line = self.cAtf_line
        #
        if self.test_text_line() == True:
            text_line_search = re.search("^\d+\.\s.*", atf_line)
            text_line = text_line_search.group(0)
            self.text_line = text_line
            #
        #
        else:
            pass
        #
        return self.text_line
    #
    #
    def get_line_text(self):
        """
        Gets the line text
        excluding the line number.
        """
        #
        if self.test_text_line() == True:
            #
            # Getting rid of the line number
            #
            line_no_search = re.search("^\d+\.\s", self.cAtf_line)
            line_no_brut = line_no_search.group(0)
            text_line = self.cAtf_line[len(line_no_brut):]
            self.lineText = text_line
        else:
            pass
        return self.lineText
    #
    #
    def get_line_number(self):
        """
        return: self.lineNumber, int.
        Checks if the line is text line
        gets the line number if it is.
        """
        #
        if self.test_text_line() == True:
            line_no_search = re.search("^\d+\.\s", self.cAtf_line)
            line_no_brut = line_no_search.group(0)
            line_no_str = line_no_brut[:-2] # Cleans the white space and the dot.
            line_no = int(line_no_str)
            self.lineNumber = line_no
            #
        else:
            self.lineNumber = None
        #
        return self.lineNumber
    #
    #
    def get_line_word_count(self):
        """
        gets the number of words in text line
        assuming that they are
        seperated by whitespace
        """
        #
        text_line_no_number = self.get_line_text()
        text_line_split = text_line_no_number.split(" ")
        #
        # See if there is anything empty
        #
        for text_line in text_line_split:
            if len(text_line) == 0:
                text_line_split.remove(text_line)
                #
                #
            #
        word_count = len(text_line_split)
        self.lineWordCount = word_count
            #
        #
        return self.lineWordCount
    #
    #
    def get_line_words(self):
        """
        params: lineText, str.
        return: lineWords, []
        Gets the whitespace delimited
        words in line
        """
        #
        text_line_no_number = self.get_line_text()
        text_line_split = text_line_no_number.split(" ")
        #
        # See if there is anything empty
        #
        for text_line in text_line_split:
            if len(text_line) == 0:
                text_line_split.remove(text_line)
                #
            #
        #
        line_words = text_line_split
        self.lineWords = line_words
        #
        #
        return self.lineWords
    #



class cAtfLineDictBuilder(cAtfLineGetter):
    """
    class for building the line_dict,
    dictionary.
    """
    #
    def __init__(self, atf_line):
        #
        super().__init__(atf_line)
        #
        self.cAtf_line = atf_line
        self.isLineStructure = False
        self.isLineComment = False
        self.lineDict = {}
        #
    #
    def isLineStruc(self):
        """
        Test if the line is a
        structure comment
        """
        #
        if self.test_text_structure() == True:
            self.isLineStructure = True
            #
        else:
            self.isLineStructure = False
        #
        return self.isLineStructure
    #
    def isLineCom(self):
        """
        test if the line is a
        comment about the content
        """
        #
        if self.test_line_content() == True:
            self.isLineComment = True
        else:
            self.isLineComment = False
        #
        return self.isLineComment
    #
    #
    def lineDictBuild(self):
        """
        builds the line dict
        based on preeceding
        methods
        """
        #
        self.lineDict["isLineStructure"] = self.isLineStruc()
        self.lineDict["isLineContent"] = self.isLineCom()
        self.lineDict["lineNumber"] = self.get_line_number()
        self.lineDict["lineWordCount"] = self.get_line_word_count()
        self.lineDict["lineText"] = self.get_line_text()
        self.lineDict["lineWords"] = list(set(self.get_line_words()))
        # Removed duplicates, for efficiency.
        self.lineDict["lineWordPos"] = list(enumerate(self.get_line_words()))
        if len(self.lineDict["lineWords"]) == 0 and self.lineDict["lineNumber"] is None:
            return None
        else:
            pass
        #
        return self.lineDict
    #


class cAtfALHandler(cAtfALTester):
    """
    Handle Another Language occurances.
    """
    #
    def __init__(self, cAtf_part):
        super().__init__()
        #
        self.cAtf_part = cAtf_part
        self.lineDict_list = []
        self.cAtf_part_lines = []
        self.alRef_list = []
        self.alGroup_list = []
        self.mulAlOc_group_list = []
        self.singAlOc_group_list = []
        self.mulAlOc_line_list = []
        self.mulAlOc_lineDict_list = []
        self.mulAlOcS = []
        self.singAlOcS = []
        self.alOc_list = []
        self.AlOcS = []
        self.alLanguage = ""
        self.textLang = ""
        #
    #
    #
    def set_ALOC_lang(self, lang):
        """
        Sets the value of self.alLanguage
        """
        #
        self.alLanguage = lang
        #
        return self.alLanguage
    #
    def set_textLang(self, lang):
        """
        Sets the value of self.textLang
        """
        #
        self.textLang = lang
        #
        return self.textLang
    #
    def splitPartLines(self):
        """
        params: self.cAtf_part, str.
        return: self.cAtf_part_lines, []
        splits the part into lines
        """
        #
        self.cAtf_part_lines = self.cAtf_part.splitlines()
        #
        return self.cAtf_part_lines
    #
    @staticmethod
    def lineDictBuild(cAtf_line):
        """
        Uses the lineDictBuilder class
        method
        """
        #
        line_class = cAtfLineDictBuilder(cAtf_line)
        line_dict = line_class.lineDictBuild()
        #
        return line_dict
    #
    #
    def get_lineDict_list(self):
        """
        params: self.cAtf_part_lines, []
        return: self.lineDict_list, []

        gets the lines in dict form
        """
        #
        for cAtf_line in self.cAtf_part_lines:
            lineDict = self.lineDictBuild(cAtf_line)
            if lineDict is not None:
                self.lineDict_list.append(lineDict)
        #
        return self.lineDict_list
    #
    @staticmethod
    def test_twoTimesUnScore(lineWord):
        """
        Tests if a word has the underscore
        two times or not.
        """
        #
        unscoCount = lineWord.count("_")
        if unscoCount == 2:
            return True
        elif unscoCount == 1:
            return False
        elif unscoCount < 1:
            return None
        else:
            pass
        #
        return None
    #
    def get_ALRefs_lineLevel(self):
        """
        Searches whether words of a line
        contain a another language switch
        If the word contains the underscore 2 times
        it is added 2 times for facilitating grouping
        after.
        """
        #
        lineDict_list_sorted = sorted(self.lineDict_list, key=lambda lineDict:lineDict["lineNumber"])
        for lineDict in lineDict_list_sorted:
            lw_list = list(lineDict["lineWordPos"])
            line_word_list_sorted = sorted(lw_list, key=lambda wpTuple:wpTuple[0])
            for WordP, lineWord in line_word_list_sorted:
                if self.test_twoTimesUnScore(lineWord) is True:
                    self.alRef_list.append((WordP, lineWord, lineDict["lineNumber"]))
                    self.alRef_list.append((WordP, lineWord, lineDict["lineNumber"]))
                elif self.test_twoTimesUnScore(lineWord) is False:
                    # (1, WORD, lineNO)
                    self.alRef_list.append((WordP, lineWord, lineDict["lineNumber"]))
                    #
                #
    @staticmethod
    def grouper(iterable, n, fillvalue=None):
        "Collect data into fixed-length chunks or blocks"
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        #
        return itertools.zip_longest(*args, fillvalue=fillvalue)
        #
    def group_ALRefs(self):
        """
        Groups the AL references for
        marking the AL occurances
        """
        #
        al_ref_groups = self.grouper(self.alRef_list, 2)
        # There should be no need for a fill value, but ...
        # I am hesitating...
        self.alGroup_list = list(al_ref_groups)
        #
        return self.alGroup_list
    #
    @staticmethod
    def test_multilineALGroup(ALGroup):
        """
        params: ALGroup, ((()),(()))
        return: boolean
        Tests if the AL references
        stocked in the al group
        points to a AL occurance
        that spreads into multiple
        lines
        """
        #((11, '_re-e2-um', 1), (11, 're-e2-um_', 2))
        start_point = ALGroup[0]
        end_point = ALGroup[1]
        # (1, WORD, lineNO), (1, WORD, lineNO)
        #
        if start_point[2] != end_point[2]:
            return True
        else:
            return False
        #
        #
    @staticmethod
    def test_singALGroup(ALGroup):
        """
        params: ALGroup, ((()),(()))
        return: boolean
        Tests if the AL references
        stocked in the al group
        points to a AL occurance
        that is confined to 1 line
        """
        #
        # ((11, '_re-e2-um_', 1), (11, '_re-e2-um_', 1))
        start_point = ALGroup[0]
        end_point = ALGroup[1]
        # (1, WORD, lineNO), (1, WORD, lineNO)
        #
        if start_point[2] == end_point[2]:
            return True
        else:
            return False
    #
    def populate_mulALOC_refs(self):
        """
        Populates the multiline
        AL occurance reference list.
        """
        #
        self.mulAlOc_group_list = []
        for alGroup in self.alGroup_list:
            if self.test_multilineALGroup(alGroup) is True:
                self.mulAlOc_group_list.append(alGroup)
                #
            else:
                pass
        #
        return self.mulAlOc_group_list
    #
    #
    def populate_singALOC_refs(self):
        """
        Populates the single line
        AL occurance reference list.
        """
        #
        self.singAlOc_group_list = []
        for alGroup in self.alGroup_list:
            if self.test_singALGroup(alGroup) is True:
                self.singAlOc_group_list.append(alGroup)
                #
            #
        return self.singAlOc_group_list
    #
    #
    @staticmethod
    def get_mulAlOc_lines(alGroup, lineDictList):
        """
        Gets the related lines from the lineDictList, by
        using the alGroup elements as point of reference.
        """
        #
        start_point = alGroup[0]
        end_point = alGroup[1]
        #
        mulAlOc_line_range = range(start_point[2],end_point[2]+1)
        # (1, WORD, lineNO), (1, WORD, lineNO)
        # +1 compensates the function's exclusion of the final element
        mulAlOc_group_line_dict_list = []
        #
        for lineDict in lineDictList:
            if lineDict["lineNumber"] in mulAlOc_line_range:
                mulAlOc_group_line_dict_list.append(lineDict)
                #
        #
        return mulAlOc_group_line_dict_list
    #
    def get_mulAlOc_lineDict_list(self):
        """
        Gets the related lineDicts for
        AL occurances that spread to multiple lines
        """
        #
        self.mulAlOc_lineDict_list = []
        #
        for mulAlOc in self.mulAlOc_group_list:
            line_list = self.get_mulAlOc_lines(mulAlOc,self.lineDict_list)
            self.mulAlOc_lineDict_list.append(line_list)
            #
        #
        return self.mulAlOc_lineDict_list
    #
    @staticmethod
    def get_FW_mulAlOc(mulAlOc_group):
        """
        Gets the First Word and its position of the
        AL Occurance that spreads to multiple
        lines.
        """
        #
        first_item_dict = {}
        mulAlOc_group_sort = sorted(mulAlOc_group, key=lambda lineDict:lineDict["lineNumber"])
        #
        mulAlOc_first_lineDict = mulAlOc_group_sort[0]
        fLineDict_words = mulAlOc_first_lineDict["lineWordPos"]
        #
        for wordPos, flineWord in fLineDict_words:
            if "_" in flineWord:
                first_item_dict[flineWord] = wordPos
        #
        first_item_sort = sorted(tuple(first_item_dict.items()), key=lambda wordWP:wordWP[1])
        first_item = (first_item_sort[-1],mulAlOc_first_lineDict["lineNumber"])
        #
        return first_item
    #
    @staticmethod
    def get_LW_mulAlOc(mulAlOc_group):
        """
        Gets the Last Word and its position of
        the AL Occurance that spreads to multiple
        lines
        """
        #
        last_item_dict = {}
        mulAlOc_group_sort =  sorted(mulAlOc_group, key=lambda lineDict:lineDict["lineNumber"])
        mulAlOc_last_lineDict = mulAlOc_group_sort[-1]
        #
        laLineDict_words = mulAlOc_last_lineDict["lineWords"]
        #
        for lalineWord in laLineDict_words:
            if "_" in lalineWord:
                last_item_dict[lalineWord] = laLineDict_words.index(lalineWord)
        #
        last_item_sort = sorted(tuple(last_item_dict.items()), key=lambda wordWP:wordWP[1])
        last_item = (last_item_sort[0],mulAlOc_last_lineDict["lineNumber"])
        #
        return last_item
    #
    def get_ALOC_lang(self,alOc):
        """
        Gets the AL occurance language
        if it has one specified with
        %,
        if not, we get the specified AL language
        in the constructor
        """
        alWord = alOc[0]
        #
        if self.test_ALSwitch(alWord) is True:
            alword_find = re.search("%\w+",alWord)
            alword_get = alword_find.group(0)
        else:
            alword_get = self.alLanguage
        #
        return alword_get
    #
    def mk_mulAlOc(self, first_item, last_item, mulAlOc_group):
        """
        params:
        first_item, ()
        last_item, ()
        mulAlOc_group, [{},{}, ... ]

        Creates multiline AL Occurance from the parameters.
        alWord_word, str. Another Language word in AL_occurance
        alWord_LineNumber, int. The line number for the al_word
        alWord_AlOc_Position, dict. Relative position of the alWord inside the AL_occurance.
        alWord_AlOc, str. Al_occurance in which the al_word is observed
        alWord_AlOc_LineNumber, list. Line number(s) in which the al_oc is observed
        alWord_LinePosition, dict. Relative position of the alWord inside the Line.

        """
        #
        alWord_dict_list = []
        #
        alOc_words = []
        #
        for lineDict in mulAlOc_group:
            lineNo = lineDict["lineNumber"]
            lineWordPos = lineDict["lineWordPos"]
            lineWCount = lineDict["lineWordCount"]
            #
            for wordPos, lineWord in lineWordPos:
                #
                if lineNo == first_item[1] and wordPos >= first_item[0][1]:
                    alOc_words.append((lineWord,wordPos,lineNo,lineWCount))
                elif first_item[1] < lineNo < last_item[1]:
                    alOc_words.append((lineWord,wordPos,lineNo, lineWCount))
                elif lineNo == last_item[1] and wordPos <= last_item[0][1]:
                    alOc_words.append((lineWord,wordPos,lineNo, lineWCount))
                else:
                    pass
            #
        #
        alOc_words_sorted = sorted(alOc_words, key=lambda al:(al[2],al[1]))
        alOc_word_list = [al[0] for al in alOc_words_sorted]
        alOc_line_list = [al[2] for al in alOc_words_sorted]
        alOc_text = " ".join(alOc_word_list)
        alOc_wordPos = enumerate(alOc_words_sorted)
        #
        for wordP, alOc_tuple in alOc_wordPos:
            alWord_dict = {}
            alWord_dict["alWord_word"] = alOc_tuple[0]
            alWord_dict["alWord_LineNumber"] = alOc_tuple[2]
            alWord_dict["alWord_AlOc"] = alOc_text
            alWord_dict["alWord_language"] = self.get_ALOC_lang(alOc_word_list)
            alWord_dict["alWord_textLanguage"] = self.textLang
            alWord_dict["alWord_alOc_LineNumber"] = alOc_line_list
            alOc_pos_dict = {}
            alOc_pos_dict["totalWords_AlOc"] = len(alOc_word_list)
            alOc_pos_dict["alWord_Position"] = wordP
            alWord_dict["alWord_AlOc_Position"] = alOc_pos_dict
            alOc_line_dict = {}
            alOc_line_dict["totalWords_Line"] = alOc_tuple[3]
            alOc_line_dict["alWord_Position"] = alOc_tuple[1]
            alWord_dict["alWord_LinePosition"] = alOc_line_dict
            alWord_dict_list.append(alWord_dict)
        #
        return alWord_dict_list
    #
    #
    def get_mulAlOcS(self):
        """
        Gets the AL Occurances that spread into multiple lines
        as lists of another language word dictionary
        """
        #
        self.mulAlOcS = []
        #
        for mulAlOc_group in self.get_mulAlOc_lineDict_list():
            first_point = self.get_FW_mulAlOc(mulAlOc_group)
            last_point = self.get_LW_mulAlOc(mulAlOc_group)
            mulAlOc = self.mk_mulAlOc(first_point, last_point, mulAlOc_group)
            self.mulAlOcS.append(mulAlOc)
            #
        #
        return self.mulAlOcS
    #
    @staticmethod
    def get_AlRefs_WordLevel(lineWP):
        """
        params: lineWP, ()
        Gets the starting point and
        end point of the AL Occurance observed
        in a single line

        """
        # lineWP == (WordPOS, WORD, LineNumber )
        #
        alRef_WP_list = []
        #
        if "_" in lineWP[1]:
            alRef_WP_list.append((lineWP[0], lineWP[1]))
            # (WORDPOS, WORD)
        #
        return alRef_WP_list
    #
    def group_ALRef_sing_Wordlevel(self, alRef_WP_list):
        """
        groups the AL occurance references
        observed in a single line
        """
        #
        alRef_WP_groups = self.grouper(alRef_WP_list,2)
        #
        return alRef_WP_groups
    #
    def mk_singAlOc(self, lineDict_list,alRef_WP_group):
        """
        params: lineDict, {}
        alRef_WP_group, ()
        Creates the AL occurance from the lineDict,
        by using the values in the alRef_WP_groups
        """
        #
        alWord_dict_list = []
        #
        alRef_WP_group_sort = sorted(alRef_WP_group, key=lambda alRef:alRef[0])
        alRef_WP_range = range(alRef_WP_group_sort[0][0], alRef_WP_group_sort[1][0]+1)
        #
        lineDict = list(filter(lambda Ldicts: Ldicts.get("lineNumber") == alRef_WP_group[0][2], lineDict_list))[0]
        # Gets the lineDict from the lineDict list for the relative
        # al occurance
        #
        alOc_words = []
        #
        lineWordPos = lineDict["lineWordPos"]
        #
        for WP, word in lineWordPos:
            if WP in alRef_WP_range:
                alOc_words.append((WP, word))
            #
        #
        alOc_words_sorted = sorted(alOc_words, key=lambda alWords:alWords[0])
        alOc_word_list = [al[1] for al in alOc_words_sorted]
        alOc_text = " ".join(alOc_word_list)
        alOc_wordPos = enumerate(alOc_words_sorted)
        #
        for WP, alWordTuple in alOc_wordPos:
            alWord_dict = {}
            alWord_dict["alWord_word"] = alWordTuple[1]
            alWord_dict["alWord_textLanguage"] = self.textLang
            alWord_dict["alWord_language"] = self.get_ALOC_lang(alOc_word_list)
            alWord_dict["alWord_LineNumber"] = lineDict["lineNumber"]
            alWord_dict["alWord_AlOc"] = alOc_text
            alWord_dict["alWord_alOc_LineNumber"] = lineDict["lineNumber"]
            alOc_pos_dict = {}
            alOc_pos_dict["totalWords_AlOc"] = len(alOc_word_list)
            alOc_pos_dict["alWord_Position"] = WP
            alWord_dict["alWord_AlOc_Position"] = alOc_pos_dict
            alOc_line_dict = {}
            alOc_line_dict["totalWords_Line"] = lineDict["lineWordCount"]
            alOc_line_dict["alWord_Position"] = alWordTuple[0]
            alWord_dict["alWord_LinePosition"] = alOc_line_dict
            alWord_dict_list.append(alWord_dict)
        #
        return alWord_dict_list
    #
    def get_singALOcS(self):
        """
        Gets AL Occurances confined to a single
        line as list of AL word dictionary.
        """
        #
        self.singAlOcS = []
        #
        for singAlOc_group in self.singAlOc_group_list:
            # singAlOc_group == ((10, '_kur_', 62), (10, '_kur_', 62))
            # (WORDPOS, WORD)
            singAlOc = self.mk_singAlOc(self.lineDict_list,singAlOc_group)
            self.singAlOcS.append(singAlOc)
        #
        return self.singAlOcS
    #
    def get_ALOcS(self):
        """
        General Method for regrouping
        The methods above.
        """
        #
        self.splitPartLines()
        self.get_lineDict_list()
        self.get_ALRefs_lineLevel()
        self.group_ALRefs()
        self.populate_mulALOC_refs()
        self.populate_singALOC_refs()
        self.get_mulAlOc_lineDict_list()
        self.get_mulAlOcS()
        self.get_singALOcS()
        #
        self.alOc_list = self.mulAlOcS + self.singAlOcS
        flatten_alOc_list = list(itertools.chain.from_iterable(self.alOc_list))
        sort_aloc_list = sorted(flatten_alOc_list, key=lambda alword_dict:(alword_dict["alWord_LineNumber"],alword_dict["alWord_LinePosition"]["alWord_Position"]))
        self.AlOcS = []
        for key, group in itertools.groupby(sort_aloc_list, key=lambda alWord_dict:alWord_dict["alWord_AlOc"]):
            self.AlOcS.append(list(group))
            #
        #
        return self.AlOcS


class cAtfWordDictBuilder(cAtfWordTester):
    """
    Class for building Word dictionaries
    of a normal text line
    """
    #
    def __init__(self,cAtf_Word):
        super().__init__(cAtf_Word)
        self.wordPos_list = []
        self.word = cAtf_Word
        self.lineDict_list = []
        self.det_signList = []
        self.detMarkList = []
        self.detRef_general_list = []
        self.detRef_Group_list = []
        self.signList = []
        self.signList_pos = []
        self.textLang = ""
        self.wordLang = ""
        self.detLang = ""
        self.clean_word = ""
        self.detDict_list = []
        self.wordDict = {}
    #
    #
    def set_textLang(self, lang):
        """
        Text language attribute
        """
        #
        self.textLang = lang
        #
        return self.textLang
    #
    def set_wordLang(self, value):
        """
        Word Language property
        """
        #
        self.wordLang = value
        #
        return self.wordLang
    #
    def set_detLang(self,value):
        """
        Set Determinative Language
        """
        #
        self.detLang = value
        #
        return self.detLang
    #
    @staticmethod
    def set_sign_seperator_curvR(cAtf_Word):
        """
        Sets the sign seperator -
        to the entities with
        parantheses
        """
        #
        if "}" in cAtf_Word and "}-" in cAtf_Word and "}#" in cAtf_Word:
            rep_string = cAtf_Word.replace("}#","#}")
            rep_word = rep_string.replace("}-","}")
            curv_par_sep = rep_word.split("}")
            curv_par = "}-".join(curv_par_sep)
        elif "}" in cAtf_Word and "}-" not in cAtf_Word and "}#" in cAtf_Word:
            rep_word = cAtf_Word.replace("}#","#}")
            curv_par = rep_word.replace("}","}-")
        elif "}#" in cAtf_Word:
            curv_par = cAtf_Word.replace("}#","#}")
        else:
            curv_par = cAtf_Word

        #
        return curv_par
    #
    @staticmethod
    def set_sign_seperator_curvL(cAtf_Word):
        """
        Sets the sign seperator -
        to the entities with
        parantheses
        """
        #
        if "{" in cAtf_Word and "-{" in cAtf_Word:
            rep_word = cAtf_Word.replace("-{","{")
            curv_par_sep = rep_word.split("{")
            curv_par = "-{".join(curv_par_sep)
        elif "{" in cAtf_Word and "-{" not in cAtf_Word:
            curv_par = cAtf_Word.replace("{","-{")
        else:
            curv_par = cAtf_Word

        return curv_par
    #
    @staticmethod
    def set_sign_seperator_corBL(cAtf_Word):
        """
        Sets the sign seperator -
        to the entities with
        parantheses
        """
        #
        if "[" in cAtf_Word and "-[" in cAtf_Word:
            rep_word = cAtf_Word.replace("-[","[")
            corn_par_sep = rep_word.split("[")
            corn_par = "-[".join(corn_par_sep)
        elif "[" in cAtf_Word and "-[" not in cAtf_Word:
            corn_par = cAtf_Word.replace("[","-[")
        else:
            corn_par = cAtf_Word
        #
        return corn_par
    #
    @staticmethod
    def set_sign_seperator_corBR(cAtf_Word):
        """
        Sets the sign seperator -
        to the entities with
        parantheses
        """
        #
        if "]" in cAtf_Word and "]-" in cAtf_Word:
            rep_word = cAtf_Word.replace("]-","]")
            corn_par_sep = rep_word.split("]")
            corn_par = "]-".join(corn_par_sep)
        elif "]" in cAtf_Word and "]-" not in cAtf_Word:
            corn_par = cAtf_Word.replace("]","]-")
        else:
            corn_par = cAtf_Word
        #
        return corn_par
    #
    @staticmethod
    def cleanWord(cWord):
        """
        Cleans the excessive
        sign seperators that might
        have been generated by the
        set_sign_seperators method
        """
        #
        first_el = cWord[0]
        last_el = cWord[-1]
        #
        if "-" == first_el:
            cWord = cWord[1:]
        elif "-" == last_el:
            cWord = cWord[:-1]
        else:
            pass
        #
        return cWord
    #
    #
    def set_sign_seperators(self):
        """
        Uses the previous sign
        seperator methods to add
        sign seperator - to right
        places
        """
        #
        cvl_word = self.set_sign_seperator_curvL(self.cAtf_word)
        cvr_word = self.set_sign_seperator_curvR(cvl_word)
        crl_word = self.set_sign_seperator_corBL(cvr_word)
        crr_word = self.set_sign_seperator_corBR(crl_word)
        self.clean_word = self.cleanWord(crr_word)
        #
        return self.clean_word
    #
    @staticmethod
    def seperate_signs(clean_word):
        """
        Seperates the signs and assigns
        them an index number.
        """
        #
        sign_list_brut = clean_word.split("-")
        sign_list = [sign.strip() for sign in sign_list_brut if sign.strip()]
        sign_list = sign_list
        #
        return sign_list
    #
    def get_detRefs(self):
        """
        Gets the starting point and the end point
        of determinatives
        """
        #
        signList_unsort = self.seperate_signs(self.clean_word)
        self.signList = signList_unsort
        signList_pos = list(enumerate(signList_unsort))
        self.signList_pos = sorted(signList_pos, key=lambda signPos:signPos[0])
        # (0,'lu'),(1, 'mesz'), etc.
        #
        self.detRef_general_list = []
        #
        for signPos, sign in self.signList_pos:
            if "{" in sign and "}" in sign:
                self.detRef_general_list.append((signPos,sign))
                self.detRef_general_list.append((signPos,sign))
            elif "{" in sign or "}" in sign:
                self.detRef_general_list.append((signPos,sign))
                #
            else:
                pass
            #
        #
        return self.detRef_general_list
    #
    @staticmethod
    def grouper(iterable, n, fillvalue=None):
        "Collect data into fixed-length chunks or blocks"
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        #
        return itertools.zip_longest(*args, fillvalue=fillvalue)
        #
    def group_detRefs(self):
        """
        Groups the AL references for
        marking the AL occurances
        """
        #
        det_ref_groups = self.grouper(self.detRef_general_list, 2)
        #
        self.detRef_Group_list = list(det_ref_groups)
        # (signPos,sign), (signPos,sign)
        #
        return self.detRef_Group_list
    #
    @staticmethod
    def detRanger(detRef_Group):
        """
        Gives the range of sign positions
        included in the determinative
        """
        #
        first_sign = detRef_Group[0]
        last_sign = detRef_Group[1]
        #
        detRange = range(first_sign[0], last_sign[0]+1)
        #
        return detRange
    #
    def get_detSigns(self):
        """
        gets the signs of the determinatives
        """
        #
        for detRef_group in self.detRef_Group_list:
            detSign_list = []
            detRange = self.detRanger(detRef_group)
            for SP, sign in self.signList_pos:
            #(SignPos, Sign),(SignPos, Sign), etc.
                if SP in detRange:
                    detSign_list.append((SP, sign))
            self.det_signList.append(tuple(detSign_list))
        #
        #
        #self.det_signList.append(tuple(detSign_list))
        #
        return self.det_signList
    #
    def uniqDetSigns(self):
        """
        Filter duplicates from det_signList
        """
        #
        detSy = set()
        det_list = []
        #
        for detl in self.det_signList:
            if detl not in detSy:
                detSy.add(detl)
                det_list.append(detl)
        #
        self.det_signList = det_list
        #
        return self.det_signList
    #
    def mrk_dets(self):# detSignlist element of self.det_signList
        """
        params: detSignlist, [(signPos, sign),(), ...]
        Marks the determinatives as
        prepos, postpos, inpos
        """
        #
        mark_set = set()
        #
        signList = sorted(self.signList_pos, key=lambda x:x[0])
        #
        for detSignlist in self.det_signList:
            detList = sorted(detSignlist, key=lambda x:x[0])
            # detSignlist == [(signPos, sign),(), ...]
            # sort according to sign position
            # sort according to sign position
            if detList[0][0] > signList[0][0] and detList[-1][0] < signList[-1][0]:
                detList.append("inpos")
                mark_set.add(tuple(detList))
            elif detList[0][0] == 0:
                detList.append("prepos")
                mark_set.add(tuple(detList))
            elif detList[-1][0] == signList[-1][0]:
                detList.append("postpos")
                mark_set.add(tuple(detList))
            #
        self.detMarkList = list(mark_set)
        #
        return self.detMarkList
    #
    @staticmethod
    def mk_detDict(detMark, sign_list):
        """
        params: detMark, ((),(),(), ...,"")
        Constructs the determinatives dictionary.
        """
        #
        # detMark == [(signPos, sign),(signPos, sign),MARK]
        det_signList = [detm for detm in detMark if isinstance(detm, tuple)]
        detList_sort = sorted(det_signList, key=lambda x:x[0])
        det_mark_str = detMark[-1]
        totalSigns = len(sign_list)
        detSigns = [det[1] for det in detList_sort]
        detText = "-".join(detSigns)
        detSignPos = list(enumerate(detList_sort))
        detPos_list = [det[0] for det in detList_sort]
        detPos = (detPos_list[0],detPos_list[-1])
        detLength = len(detSigns)
        #
        detEntity_list = []
        #
        for detSign in detSignPos:
            # detSign == (0,(3,an)),(1,(4,mesz)), etc
            detSign_dict = {}
            detSign_dict["detSign_det"] = detText
            detSign_dict["detSign_det_WordPos"] = detPos
            detSign_dict["detSign_detMark"] = det_mark_str
            detSign_dict["detSign_detSign"] = detSign[1][1]
            detSign_word_pos = {}
            detSign_word_pos["totalSigns_word"] = totalSigns
            detSign_word_pos["detSign_position"] = detSign[1][0]
            detSign_dict["detSign_WordPosition"] = detSign_word_pos
            detSign_sign_pos = {}
            detSign_sign_pos["totalSigns_determinative"] = detLength
            detSign_sign_pos["detSign_position"] = detSign[0]
            detSign_dict["detSign_DetPosition"] = detSign_sign_pos
            detEntity_list.append(detSign_dict)
        #
        detEntity_tuple = tuple(detEntity_list)
        #
        return detEntity_tuple
    #
    def get_detDictS(self):
        """
        Populates the determinative list
        in the form of list of list of dicts.
        Dicts represent a sign of a determinative
        list of dicts represent the determinative
        list of list of dicts represent the
        determinatives of the word.
        """
        #
        self.get_detRefs()
        self.group_detRefs()
        signlist = self.signList_pos
        #
        self.get_detSigns()
        self.uniqDetSigns()
            #detSignlist == [[(signPos, sign),(), ...], [(signPos, sign),(), ...] ]
            # detsign == [(signPos, sign),(), ...]
        detMarkList = self.mrk_dets()
            #
        for detMark in detMarkList:
            # detMark == [(signPos, sign),(signPos, sign),MARK]
            detDicts = self.mk_detDict(detMark, signlist)
            self.detDict_list.append(detDicts)
        #
        return self.detDict_list
    #
    def set_numberDict(self):
        """
        Sets the number dict if the word is a number
        """
        #
        numberDict = {}
        #
        if self.test_isNumberF1() is True:
            number_repetCount = re.search("\d+\(", self.cAtf_word)
            numberDict["number_repetitionCount"] = int(number_repetCount.group(0)[:-1])
            # -1 for excluding the (
            number_grapheme = re.search("\(.*?\)", self.cAtf_word)
            numberDict["number_grapheme"] = number_grapheme.group(0)[1:-1]
            # 1, -1 for excluding the ()
        elif self.test_isNumberF2() is True:
            number_repetCount = re.search(".*\(", self.cAtf_word)
            numberDict["number_repetitionCount"] = number_repetCount.group(0)[:-1]
            number_grapheme = re.search("\(.*?\)", self.cAtf_word)
            numberDict["number_grapheme"] = number_grapheme.group(0)[1:-1]
        elif self.test_isNumberF3() is True:
            number_repetCount = re.search(".*\(", self.cAtf_word)
            numberDict["number_repetitionCount"] = number_repetCount.group(0)[:-1]
            number_grapheme = re.search("\(.*?\)", self.cAtf_word)
            numberDict["number_grapheme"] = number_grapheme.group(0)[1:-1]
        else:
            pass
        #
        return numberDict
    #
    def set_punctDict(self):
        """
        Sets the punctuation dictionary
        if there is any qualification
        of the grapheme
        """
        #
        punctDict = {}
        #
        if self.test_isWordDivider_Specified() is True:
            puncElement = re.search(".*\(", self.cAtf_word)
            punctDict["punctuation_punctElement"] = puncElement.group(0)[:-1]
            #
            puncGrapheme = re.search("\(.*?\)", self.cAtf_word)
            punctDict["punctuation_punctGrapheme"] = puncGrapheme.group(0)[1:-1]
            #
        elif self.test_isBulletSpeficied() is True:
            puncElement = re.search(".*\(", self.cAtf_word)
            punctDict["punctuation_punctElement"] = puncElement.group(0)[:-1]
            #
            puncGrapheme = re.search("\(.*?\)", self.cAtf_word)
            punctDict["punctuation_punctGrapheme"] = puncGrapheme.group(0)[1:-1]
        #
        else:
            pass
        #
        return punctDict
    #
    def wordDictBuild(self):
        """
        Builds the wordDict
        """
        #
        self.set_sign_seperators()
        self.get_detRefs()
        self.detDict_list = []
        self.get_detDictS()
        #
        self.wordDict = {}
        self.wordDict["word_wordSignCount"] = len(self.signList)
        self.wordDict["word_word"] = self.cAtf_word
        self.wordDict["word_determinatives"] = self.detDict_list
        self.wordDict["word_wordSignsPos"] = self.signList_pos
        self.wordDict["word_Signs"] = list(set(self.signList))
        # Removed duplicates for efficiency
        self.wordDict["word_hasDamage"] = self.test_damaged_sign()
        self.wordDict["word_wordLang"] = self.wordLang
        self.wordDict["word_isNumber"] = self.test_isNumber()
        self.wordDict["word_numberDict"] = self.set_numberDict()
        self.wordDict["word_hasComplement"] = self.test_has_complement()
        self.wordDict["word_hasUnknownReading"] = self.test_has_unknownReading()
        self.wordDict["word_hasCompound"] = self.test_has_compound()
        self.wordDict["word_hasSpecification"] = self.test_has_specification()
        self.wordDict["word_hasQuery"] = self.test_has_query()
        self.wordDict["word_hasCollation"] = self.test_has_collation()
        self.wordDict["word_hasCorrection"] = self.test_has_correction()
        self.wordDict["word_isColon"] = self.test_isColon()
        self.wordDict["word_isDColon"] = self.test_isDColon()
        self.wordDict["word_isColonRQ"] = self.test_isColonRQ()
        self.wordDict["word_isColonDQ"] = self.test_isColonDQ()
        self.wordDict["word_isWordDivider"] = self.test_isWordDivider()
        self.wordDict["word_isBullet"] = self.test_isBullet()
        self.wordDict["word_isBulletSpecified"] = self.test_isBulletSpeficied()
        self.wordDict["word_punctuationDict"] = self.set_punctDict()
        self.wordDict["word_isSpecifiedWordDivider"] = self.test_isWordDivider_Specified()
        self.wordDict["word_hasComplement"] = self.test_has_complement()
        self.wordDict["word_hasUnknownReading"] = self.test_has_unknownReading()
        self.wordDict["word_hasCurved"] = self.test_hasCurved()
        self.wordDict["word_hasFlat"] = self.test_hasFlat()
        self.wordDict["word_hasGunu"] = self.test_hasGunu()
        self.wordDict["word_hasSheshig"] = self.test_hasSheshig()
        self.wordDict["word_hasTenu"] = self.test_hasTenu()
        self.wordDict["word_hasNutillu"] = self.test_hasNutillu()
        self.wordDict["word_hasZidatenu"] = self.test_hasZidatenu()
        self.wordDict["word_hasKabatenu"] = self.test_hasKabatenu()
        self.wordDict["word_hasVertReflected"] = self.test_hasVertReflected()
        self.wordDict["word_hasHorReflected"] = self.test_hasHorReflected()
        self.wordDict["word_hasVariant"] = self.test_hasVariant()
        self.wordDict["word_hasRotated"] = self.test_hasRotated()
        self.wordDict["word_hasBeside"] = self.test_hasBeside()
        self.wordDict["word_hasJoining"] = self.test_hasJoining()
        self.wordDict["word_hasAbove"] = self.test_hasAbove()
        self.wordDict["word_hasCrossing"] = self.test_hasCrossing()
        self.wordDict["word_hasAllograph"] = self.test_hasAllograph()
        self.wordDict["word_hasSpecialAllograph"] = self.test_hasSpecialAllograph()
        self.wordDict["word_hasFormVariant"] = self.test_hasFormVariant()
        self.wordDict["word_hasContaining"] = self.test_hasContaining()
        self.wordDict["word_hasContainingGroup"] = self.test_hasContaining_Group()
        #
        return self.wordDict

# ----------------------------------


class cAtfSignDictBuilder(cAtfSignTester):
    """
    Class regrouping methods for building a signDict
    """
    #
    # Operator types for Compound Signs ----------------------
    operator_dict = {
        "beside":".",
        "joining":"+",
        "containing":"x", # This is also used for indicating repetitions.
        # Thus needs to be handled DONE # Binary scope
        "above":"&", # Binary scope
        "crossing":"%", # Binary scope
        "opposing":"@", # This needs to be handled, it is also used in
        # modifiers and part titles. modifiers DONE
        # binary scope
    }
    modifier_dict = {
        "curved":"@c",
        "flat":"@f",
        "gunu":"@g", # 4 extra wedges
        "sheshig":"@s", # added sze sign
        "tenu":"@t", # slanting
        "nutillu":"@n", # unfinished
        "zidatenu":"@z", # slanting right
        "kabatenu":"@k", # slanting left
        "verticallyReflected":"@r",
        "horizontallyReflected":"@h",
        "variant":"@v"
        # Rotations need to be handled seperately DONE
    }
    #
    def __init__(self, catf_sign):
        super().__init__(catf_sign)
        self.catf_sign = catf_sign
        self.signDict = {}
        self.compoundSign = ""
        self.prnthsPosition_list = []
        self.sign_dict_list = []
        self.signRelation_dict_list = []
        #
    #
    #
    """
    TODO Specifications are treated as
    words when they are delimited by space
    signs when they are delimited by -
    Sayılarla ilgili bir karar vermem lazım.
    Karmaşık işaretlerden de oluşuyor olabilirler.
    """
    #
    def get_compoundSign(self):
        """
        Gets the compound sign.
        """
        #
        if self.test_isCompound() is True:
            compound_sign_search = re.search("\|.*?\|", self.catf_sign)
            self.signDict["sign_isDamaged"] = self.test_isDamaged()
            # This test is done here because
            # C-ATF treates compound signs as atoms
            # If one would like to extend this extractor to
            # O-ATF then this has to moved to elsewhere.
            compound_sign = compound_sign_search.group(0)
            self.compoundSign = compound_sign[1:-1]
            # 1 - -1 for getting rid of | on both sides
        else:
            pass
        #
        return self.compoundSign
    #
    @staticmethod
    def get_nestElements(nestedString):
        """
        Generates the paranthese content
        with its associated level
        if the compound sign is nested.

        Code adapted from SO:
        author: Gareth Rees
        date Published: 2010-11-26-12-32
        date Retrieved: 2017-04-23-19-54
        url: http://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level
        """
        #
        paren_stack = []
        for i, char in enumerate(nestedString):
            # Ex. CompoundSign == |AN.(ANxAN)&((AN.AN)%AN)|
            if char == "(":
                paren_stack.append(i)
                # Adds the position of (
            elif char == ")" and paren_stack:
                # Comes the next )
                start = paren_stack.pop()
                # Gives the last added ( position
                # The logic is that the last added ( would correspond to
                # the first ) and by using pop we ensure
                # that the second ) doesn't mismatch with the ( of
                # the previous right paranthese.
                yield (len(paren_stack),list(range(start, i+1)), nestedString[start+1:i])
                # the last expression inside the [] excludes the i and
                # adds one to the position of the ( so that we have the
                # content.
                # **WARNING** Range values includes parantheses
        #
    def get_OpPositions(self, compoundSign):
        """
        gets the operator positions from the
        compound sign.
        """
        #
        opPosition_list = []
        #
        for charPos, char in enumerate(compoundSign):
            if char in self.operator_dict.values():
                opPosition_list.append((charPos, char))
            #
        #
        return opPosition_list
    #
    @staticmethod
    def get_nestLevelDict(nestList):
        """
        Maps the output of the generator
        expression to a dictionary
        for facilitating later use.
        """
        #
        nestLevel_dict_list = []
        #
        for nestL in nestList:
            nestLDict = {}
            nestLDict["nest_level"] = nestL[0]
            nestLDict["nest_range"] = nestL[1]
            nestLDict["nest_content"] = nestL[2]
            nestLevel_dict_list.append(nestLDict)
        #
        return nestLevel_dict_list
    #
    @staticmethod
    def get_nestDict(nestList):
        """
        Creates a dictionary based on nest levels.
        """
        #
        nestDict = {}
        #
        sort_nestList = sorted(nestList, key=lambda x:x[0]) #
        #
        for nestEl in sort_nestList:
            nestDict.setdefault(nestEl[0], []).append(nestEl[1:])
        #
        return nestDict
    #
    @staticmethod
    def nestDict_LevelRangeCreator(nestDict):
        """
        Regroups the range list of nest elements
        for each level and appends it to the end
        of the value associated with the nest level
        """
        #
        nestDict_Ranges = {}
        for key, nestEl in nestDict.items():
            nestLevel_range_list = []
            for nestTuple in nestEl:
                nestLevel_range_list.extend(nestTuple[0])
                # nestTuple[0] should correspond to list of char positions
            #
            nestDict_Ranges[key] = nestEl
            nestDict_Ranges[key].append(nestLevel_range_list)
        #
        return nestDict_Ranges
    #
    # "|(AN.((IR2%IR3).((AN&AN)+(IR3xAN))).((AN.IR3)xNITA))|" Test sign
    #
    @staticmethod
    def get_OpDict_list(nestDict_Ranges, opPosition_list):
        """
        Gets the operator levels plus one position before and after the
        operator position. Maps all of this to a dictionary.
        Appends the dictionary to a list
        """
        #
        opDictList = []
        #
        for opPosition in opPosition_list:
            for level, nestEl in nestDict_Ranges.items():
                nestRangeList = nestEl[-1]
                if opPosition[0] in nestRangeList:
                    posPlace = nestRangeList.index(opPosition[0])
                    posDict = {}
                    posDict["operatorPosition_nestlevel"] = level
                    posDict["operatorPosition_after"] = nestRangeList[posPlace+1:posPlace+4]
                    # This for checking modifier types afterwards
                    # Especially the rotation.
                    posDict["operatorPosition_before"] = nestRangeList[posPlace-1]
                    # Might come in handy for checking 'repeated' operator
                    posDict["operatorPosition_position"] = opPosition[0]
                    posDict["operatorPosition_operator"] = opPosition[1]
                    opDictList.append(posDict)
                #
        #
        return opDictList
        #
    @staticmethod
    def get_OpLevelPosition(opDictList):
        """
        Eliminates the duplicate occurances
        for the operators. Only the
        highest level in which the
        operator occured is retained.
        Function groups the operators
        according to their positions
        then makes a list with the highest levels
        within the group.
        """
        #
        opdictsSorted = sorted(opDictList, key=lambda opDict:opDict["operatorPosition_position"]) # Sort list according to operator positions
        opDictsGrouped = [list(group) for key, group in itertools.groupby(opdictsSorted, key=lambda x:x["operatorPosition_position"])]
        # Group elements according to operator positions
        opDictGroupsSort = [sorted(groupList, key=lambda opDict:opDict["operatorPosition_nestlevel"]) for groupList in opDictsGrouped]
        # Sort group list according to the nest level
        operatorPos_level_list = [sorted_group[-1] for sorted_group in opDictGroupsSort]
        #
        return operatorPos_level_list
    #
    def get_SignRelationBS(self,
                           operatorPos_level_list,
                           nestLevel_dict_list,
                           compoundSign):
        """
        Gets the sign or sign groups that
        are associated with each other through
        a binary scoped operator
        """
        #
        signRelation_dict_list = []
        #
        for operatorPos_level in operatorPos_level_list:
            operatorNestLevel = operatorPos_level["operatorPosition_nestlevel"]
            operatorPos = operatorPos_level["operatorPosition_position"]
            operator = operatorPos_level["operatorPosition_operator"]
            for nestLevel_dict in nestLevel_dict_list:
                nestRange = nestLevel_dict["nest_range"]
                nestLevel = nestLevel_dict["nest_level"]
                nestContent = nestLevel_dict["nest_content"]
                if self.test_isBinaryScope(operator) is True:
                    # x and @ will be handled individually
                    # we test only for % and &
                    if operatorPos in nestRange and operatorNestLevel == nestLevel:
                        opPosinRange = nestRange.index(operatorPos)
                        opPrecedents = nestRange[1:opPosinRange]
                        # 1 for excluding the (
                        opFollowers = nestRange[opPosinRange+1:-1]
                        # -1 for excluding )
                        opPrecLength = len(opPrecedents)
                        opPrecChars = nestContent[:opPrecLength]
                        opFolChars = nestContent[opPrecLength+1:]
                        # +1 for excluding the operator
                        signRelation_dict = {}
                        signRelation_dict["SR_operator"] = operator
                        signRelation_dict["SR_operator_antec"] = opPrecChars
                        signRelation_dict["SR_operator_subsq"] = opFolChars
                        signRelation_dict["SR_nest_level"] = nestLevel
                        signRelation_dict["SR_nest_content"] = nestContent
                        signRelation_dict["SR_compoundSign"] = compoundSign
                        signRelation_dict["SR_nest_range"] = [nestRange[0], nestRange[-1]]
                        if "(" in opPrecChars and ")" in opPrecChars and ")" in opFolChars and "(" in opFolChars:
                            signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Group", "operator_subsequent":"Group"}
                        elif "(" in opPrecChars and ")" in opPrecChars and ")" not in opFolChars and not "(" in opFolChars:
                            signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Group", "operator_subsequent":"Sign"}
                        elif "(" not in opPrecChars and ")" not in opPrecChars and ")" in opFolChars and "(" in opFolChars:
                            signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Sign", "operator_subsequent":"Group"}
                        elif "(" not in opPrecChars and ")" not in opPrecChars and ")" not in opFolChars and "(" not in opFolChars:
                            signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Sign", "operator_subsequent":"Sign"}
                        signRelation_dict["SR_operator_position"] = operatorPos
                        if operator == "%":
                            signRelation_dict["SR_operator_type"] = "crossing"
                        elif operator == "&":
                            signRelation_dict["SR_operator_type"] = "above"
                        signRelation_dict["SR_operator_antec_range"] = [opPrecedents[0],opPrecedents[-1]]
                        signRelation_dict["SR_operator_subseq_range"] = [opFollowers[0],opFollowers[-1]]
                        self.signRelation_dict_list.append(signRelation_dict)
        #
        return self.signRelation_dict_list
    #
    def get_SignRelationSpeCases(self,operatorPos_level_list, nestLevel_dict_list, compoundSign):
        """
        Gets the sign or sign groups that
        are associated with each other through
        x and @ operators
        """
        #
        signRelation_dict_list = []
        #
        for operatorPos_level in operatorPos_level_list:
            operatorNestLevel = operatorPos_level["operatorPosition_nestlevel"]
            operatorPos = operatorPos_level["operatorPosition_position"]
            operator = operatorPos_level["operatorPosition_operator"]
            for nestLevel_dict in nestLevel_dict_list:
                nestRange = nestLevel_dict["nest_range"]
                nestLevel = nestLevel_dict["nest_level"]
                nestContent = nestLevel_dict["nest_content"]
                if operatorPos in nestRange and operatorNestLevel == nestLevel:
                    opPosinRange = nestRange.index(operatorPos)
                    opPrecedents = nestRange[1:opPosinRange]
                    # 1 for excluding the (
                    opFollowers = nestRange[opPosinRange+1:-1]
                    # -1 for excluding )
                    opPrecLength = len(opPrecedents)
                    opPrecChars = nestContent[:opPrecLength]
                    opFolChars = nestContent[opPrecLength+1:]
                    # +1 for excluding the operator
                    signRelation_dict = {}
                    signRelation_dict["SR_operator"] = operator
                    signRelation_dict["SR_operator_antec"] = opPrecChars
                    signRelation_dict["SR_operator_subsq"] = opFolChars
                    signRelation_dict["SR_nest_level"] = nestLevel
                    signRelation_dict["SR_nest_content"] = nestContent
                    signRelation_dict["SR_compoundSign"] = compoundSign
                    signRelation_dict["SR_nest_range"] = [nestRange[0],nestRange[-1]]
                    if "(" in opPrecChars and ")" in opPrecChars and ")" in opFolChars and "(" in opFolChars:
                        signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Group", "operator_subsequent":"Group"}
                    elif "(" in opPrecChars and ")" in opPrecChars and ")" not in opFolChars and not "(" in opFolChars:
                        signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Group", "operator_subsequent":"Sign"}
                    elif "(" not in opPrecChars and ")" not in opPrecChars and ")" in opFolChars and "(" in opFolChars:
                        signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Sign", "operator_subsequent":"Group"}
                    elif "(" not in opPrecChars and ")" not in opPrecChars and ")" not in opFolChars and "(" not in opFolChars:
                        signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Sign", "operator_subsequent":"Sign"}
                    signRelation_dict["SR_operator_position"] = operatorPos
                    signRelation_dict["SR_operator_antec_range"] = [opPrecedents[0], opPrecedents[-1]]
                    signRelation_dict["SR_operator_subseq_range"] = [opFollowers[0], opFollowers[-1]]
                    if operator == ".":
                        signRelation_dict["SR_operator_type"] = "beside"
                    elif operator == "+":
                        signRelation_dict["SR_operator_type"] = "joining"
                    elif operator == "x" and opPrecChars.isdigit():
                        signRelation_dict["SR_operator_type"] = "repeated"
                    elif operator == "x" and not opPrecChars.isdigit():

                        signRelation_dict["SR_operator_type"] = "containing"
                    elif operator == "@":
                        if re.search("^\d+", opFolChars) is not None:
                        # This means that the @ sign is
                        # a modifier here so we restart looping
                            continue
                        else:
                            opFolCharsOper = nestContent[opPrecLength:opPrecLength+3]
                            # Includes the operator @
                            if "@c" in opFolCharsOper or "@f" in opFolCharsOper or "@g" in opFolCharsOper or "@s" in opFolCharsOper or "@s" in opFolCharsOper or "@t" in opFolCharsOper or "@n" in opFolCharsOper or "@z" in opFolCharsOper or "@k" in opFolCharsOper or "@r" in opFolCharsOper or "@h" in opFolCharsOper or "@v" in opFolCharsOper:
                                # This means that @ sign is
                                # a modifier so we restart looping
                                continue
                            else:
                                signRelation_dict["SR_operator_type"] = "opposing"
                    #
                    self.signRelation_dict_list.append(signRelation_dict)
                #
        #
        return self.signRelation_dict_list
    #
    def get_unNestedCompSigns(self, compoundSign, opPosition_list):
        """
        gets the signs of compound sign
        that is not nested.
        """
        #
        signRelation_dict_list = []
        #
        for opPos in opPosition_list:
            opP = opPos[0]
            opChar = opPos[1]
            opAnte = compoundSign[:opP]
            opSubseq = compoundSign[opP:]
            signRelation_dict = {}
            signRelation_dict["SR_operator"] = opChar
            signRelation_dict["SR_operator_antec"] = opAnte
            signRelation_dict["SR_operator_subsq"] = opSubseq[1:]
            # 1 for excluding the operator in mapping
            signRelation_dict["SR_compoundSign"] = compoundSign
            signRelation_dict["SR_nest_level"] = 0
            signRelation_dict["SR_nest_content"] = compoundSign
            compoundSignRange = list(range(0,len(compoundSign)))

            signRelation_dict["SR_nest_range"] = [compoundSignRange[0], compoundSignRange[-1]]
            signRelation_dict["SR_operator_position"] = opP
            signRelation_dict["SR_relation_type"] = {"operator_antecedent":"Sign", "operator_subsequent":"Sign"}
            if opChar == "%":
                signRelation_dict["SR_operator_type"] = "crossing"
            elif opChar == "&":
                signRelation_dict["SR_operator_type"] = "above"
            elif opChar == ".":
                signRelation_dict["SR_operator_type"] = "beside"
            elif opChar == "+":
                signRelation_dict["SR_operator_type"] = "joining"
            elif opChar == "x" and opAnte.isdigit():
                signRelation_dict["SR_operator_type"] = "repeated"
            elif opChar == "x" and not opAnte.isdigit():
                signRelation_dict["SR_operator_type"] = "containing"
            elif operator == "@":
                if re.search("^\d+",opSubseq[1:]) is not None:
                    # Starts from 1 because opSubseq[0]== operator
                # This means that the @ sign is
                # a modifier here so we restart looping
                    continue
                else:
                    opFolCharsOper = opSubseq[0:2]
                    # Includes the operator @
                    if "@c" in opFolCharsOper or "@f" in opFolCharsOper or "@g" in opFolCharsOper or "@s" in opFolCharsOper or "@s" in opFolCharsOper or "@t" in opFolCharsOper or "@n" in opFolCharsOper or "@z" in opFolCharsOper or "@k" in opFolCharsOper or "@r" in opFolCharsOper or "@h" in opFolCharsOper or "@v" in opFolCharsOper:
                        # This means that @ sign is
                        # a modifier so we restart looping
                        continue
                    else:
                        signRelation_dict["SR_operator_type"] = "opposing"
            signRelation_dict["SR_operator_antec_range"] = [0, opP-1]
            # -1 for stimulating the
            # the range behaviour, as in
            # range(0, opP)
            signRelation_dict["SR_operator_subseq_range"] = [opP, len(compoundSign) - 1]
            # -1 again for stimulating the range behaviour
            #
            self.signRelation_dict_list.append(signRelation_dict)
        #
        return self.signRelation_dict_list
    #
    @staticmethod
    def get_signsSR(signRelDict):
        """
        Gets signs from the sign dict.
        """
        #
        compoundSign_signList = []
        if signRelDict["SR_relation_type"]["operator_antecedent"] == "Sign" and signRelDict["SR_relation_type"]["operator_subsequent"] == "Sign":
            compoundSign_signList.append(signRelDict["SR_operator_antec"])
            compoundSign_signList.append(signRelDict["SR_operator_subsq"])
            compoundSign_signList.append(signRelDict)
            #
        elif signRelDict["SR_relation_type"]["operator_antecedent"] == "Group" and signRelDict["SR_relation_type"]["operator_subsequent"] == "Sign":
            compoundSign_signList.append(signRelDict["SR_operator_subsq"])
            compoundSign_signList.append(signRelDict)
            #
        elif signRelDict["SR_relation_type"]["operator_antecedent"] == "Sign" and signRelDict["SR_relation_type"]["operator_subsequent"] == "Group":
            compoundSign_signList.append(signRelDict)
        #
        return compoundSign_signList
    #
    def get_signComplement(self):
        """
        Gets the signs from a sign
        that has a complement
        """
        #
        complement_sign_list = []

        if self.test_isComplement(self.catf_sign) is True:
            compSplit = self.catf_sign.split("+")
            complement_sign = compSplit[1]
            complement_sign_list.append(complement_sign)
        #
        return complement_sign_list
    #
    @staticmethod
    def char_convert(sign):
        """
        Convert CDLI C-ATF characters
        to unicode
        """
        #
        text_sz = sign.replace("sz","\u0161") # sz -> š
        text_SZ = text_sz.replace("SZ", "\u0160") # SZ -> Š
        text_sPo = text_SZ.replace("s,", "\u1e63") # s, -> ṣ
        text_SPo = text_sPo.replace("S,", "\u1e62") # S, -> Ṣ
        text_tch = text_SPo.replace("t,", "\u1e6d") # t, -> ṭ
        text_TCH = text_tch.replace("T,", "\u1e6c") # T, -> Ṭ
        text_s = text_TCH.replace("s'", "\u015b") # s' -> ś
        text_S = text_s.replace("S'","\u015a") # S' -> Ś
        text_ayn = text_S.replace("'", "\u02be") # ' -> ʾ
        text_sub0 = text_ayn.replace("0","\u2080")# Subscript numbers
        text_sub1 = text_sub0.replace("1","\u2081")
        text_sub2 = text_sub1.replace("2","\u2082")
        text_sub3 = text_sub2.replace("3","\u2083")
        text_sub4 = text_sub3.replace("4","\u2084")
        text_sub5 = text_sub4.replace("5","\u2085")
        text_sub6 = text_sub5.replace("6","\u2086")
        text_sub7 = text_sub6.replace("7","\u2087")
        text_sub8 = text_sub7.replace("8","\u2088")
        text_sub9 = text_sub8.replace("9","\u2089")
        text_subx = text_sub9.replace("x²","\u208a") # subscript x
        text_subX = text_subx.replace("X²","\u208a")
        text_h = text_subX.replace("h,", "\u1e2b") # h, -> ḫ
        text_H = text_h.replace("H,", "\u1e2a") # H, -> Ḫ
        text_j = text_H.replace("j","\u014b") # j -> ŋ
        text_J = text_j.replace("J","\u014a") # J -> Ŋ
        #
        return text_J
    #
    @staticmethod
    def signDictBuild(sign):
        """
        params:
        sign, str.
        C(ompound/complement) S(ign), boolean

        Returns the sign dict
        with all the features.
        """
        #
        signDict = {}
        tester_class = cAtfSignTester(sign)
        signDict["sign_sign"] = sign
        signDict["sign_isComplement"] = tester_class.test_isComplement()
        signDict["sign_isQuery"] = tester_class.test_is_query()
        signDict["sign_isCorrection"] = tester_class.test_is_correction()
        signDict["sign_isCollation"] = tester_class.test_is_collation()
        signDict["sign_isCurved"] = tester_class.test_isCurved()
        signDict["sign_isFlat"] = tester_class.test_isFlat()
        signDict["sign_isGunu"] = tester_class.test_isGunu()
        signDict["sign_isSheshig"] = tester_class.test_isSheshig()
        signDict["sign_isTenu"] = tester_class.test_isTenu()
        signDict["sign_isNutillu"] = tester_class.test_isNutillu()
        signDict["sign_isZidatenu"] = tester_class.test_isZidatenu()
        signDict["sign_isKabatenu"] = tester_class.test_isKabatenu()
        signDict["sign_isVertReflected"] = tester_class.test_isVertReflected()
        signDict["sign_hasAllograph"] = tester_class.test_hasAllograph()
        signDict["sign_hasSpecialAllograph"] = tester_class.test_hasSpecialAllograph()
        signDict["sign_isHorReflected"] = tester_class.test_isHorReflected()
        signDict["sign_isVariant"] = tester_class.test_isVariant()
        signDict["sign_isRotated"] = tester_class.test_isRotated()
        #signDict["sign_isPartOfCompound"] = test_isCompound()
        #signDict["sign_nestLevel"] = 0 Compound değilse
        #signDict["sign_isUnknownReading"] = test_isUnknownReading() # Compound değilse
        #signDict["sign_relatedSigns"] = {} # Buraya compound
        # işaretleri oluşturan liste eklenecek
        return signDict
    #
    def buildSignDict(self):
        """
        Wraps the methods defined throughout the class.
        """
        #
        sign_dict_list = []
        #
        if self.test_isCompound() is True and self.test_isSpecification() is True:
            # Basically it is a nested compound sign
            compoundSign = self.get_compoundSign()
            nestedElements = self.get_nestElements(compoundSign)
            opPositonList = self.get_OpPositions(compoundSign)
            nestList = list(nestedElements)
            nestLevelDictList = self.get_nestLevelDict(nestList)
            nest_dict = self.get_nestDict(nestList)
            nest_dict_levelRange = self.nestDict_LevelRangeCreator(nest_dict)
            opDict_list = self.get_OpDict_list(
                nest_dict_levelRange,
                opPositonList
            )
            opLvlPosition = self.get_OpLevelPosition(opDict_list)
            SR_dictList_BS = self.get_SignRelationBS(
                opLvlPosition,
                nestLevelDictList,
                compoundSign
            )
            SR_dictList_SCases = self.get_SignRelationSpeCases(
                opLvlPosition,
                nestLevelDictList,
                compoundSign
            )
            SR_dictList = SR_dictList_SCases + SR_dictList_BS
            compoundSign_SR_lists_brut = [self.get_signsSR(SignDict) for SignDict in SR_dictList]
            # There are empty list in the brut file
            # Created by the group - group associations
            compoundSign_SR_lists = list(filter(None, compoundSign_SR_lists_brut))
            # They are filtered now.
            for compoundSignList in compoundSign_SR_lists:
                SR_dict = compoundSignList[-1]
                for signElement in compoundSignList:
                    if not isinstance(signElement, dict):
                        self.signDict = self.signDictBuild(signElement)
                        self.signDict["sign_isPartOfCompound"] = True
                        self.signDict["sign_isUnknownReading"] = False
                        self.signDict["sign_relatedSigns"] = SR_dict
                        self.signDict["sign_nestLevel"] = SR_dict["SR_nest_level"]
                        self.signDict["sign_compoundSign"] = SR_dict["SR_compoundSign"]
                        sign_dict_list.append(self.signDict)
        # Compound Nested DONE
        #
        elif self.test_isCompound() is True and self.test_isSpecification() is False:
            # Compound Not Nested
            compoundSign = self.get_compoundSign()
            opPositonList = self.get_OpPositions(compoundSign)
            unNestedList = self.get_unNestedCompSigns(
                compoundSign, opPositonList
            )
            compoundSign_SR_lists = [self.get_signsSR(SignDict) for SignDict in unNestedList]
            for compoundSignList in compoundSign_SR_lists:
                SR_dict = compoundSignList.pop()
                for signElement in compoundSignList:
                    self.signDict = self.signDictBuild(signElement)
                    self.signDict["sign_isPartOfCompound"] = True
                    self.signDict["sign_isUnknownReading"] = False
                    self.signDict["sign_relatedSigns"] = SR_dict
                    self.signDict["sign_nestLevel"] = SR_dict["SR_nest_level"]
                    self.signDict["sign_compoundSign"] = SR_dict["SR_compoundSign"]
                    sign_dict_list.append(self.signDict)
                    #
        # Compound not Nested DONE
        #
        elif self.test_isCompound() is False and self.test_isComplement() is True:
            # Not a Compound Sign but is a complement
            complementSignList = self.get_signComplement(sign)
            for complementSign in complementSignList:
                self.signDict = self.signDictBuild(complementSign)
                self.signDict["sign_isPartOfCompound"] = False
                self.signDict["sign_isUnknownReading"] = self.test_isUnknownReading(sign)
                self.signDict["sign_relatedSigns"] = {} # TODO get Related Sign for Complement Signs
                self.signDict["sign_nestLevel"] = 0
                self.signDict["sign_compoundSign"] = ""
                sign_dict_list.append(self.signDict)
        # Complement sign DONE
        #
        elif self.test_isComplement() is False and self.test_isCompound() is False:
            self.signDict = self.signDictBuild(self.catf_sign)
            self.signDict["sign_isPartOfCompound"] = False
            self.signDict["sign_isUnknownReading"] = self.test_isUnknownReading()
            self.signDict["sign_isDamaged"] = self.test_isDamaged()
            self.signDict["sign_relatedSigns"] = {} # TODO get Related Sign
            self.signDict["sign_nestLevel"] = 0
            self.signDict["sign_compoundSign"] = ""
            sign_dict_list.append(self.signDict)
        #
        return sign_dict_list
    #
    # Algorithm DONE
    # Tests! DONE



class cAtfTextBuilder(object):
    """
    Builds the brut text as a feature
    dictionary, by calling the methods
    from the classes above.
    """
    #
    def __init__(self, text):
        #
        self.text_brut = text
        self.atf_section = ""
        self.textLang = ""
        self.wordLang = ""
        self.alLanguage = ""
        self.detLang = ""
        self.object_parts_list = []
        self.objectIdPart = []
        self.catf_text_dict = {}
        self.objectPartLines_list = []
        self.objectTextParts = []
        self.textPart_dict_list = []
        self.textPartsHierarchy = []
    #
    # Section Methods
    #
    def get_atf_section(self):
        """
        params: atf_file, str.
        return: atf_section, str.

        Takes a text given as the text output
        of the cdli splits the atf section
        for later use.
        """
        #
        find_atf_section = re.search("&P\d+.*", self.text_brut, re.DOTALL)
        #
        self.atf_section = find_atf_section.group(0)
        #
        return self.atf_section
    #
    def get_object_parts(self):
        """
        params: atf_section, str.
        return: object_part_list, []
        """
        #
        try:
            if "\n" not in self.atf_section:
                raise ValueError("Newline character doesn't match to expected unix input type")
            else:
                pass
        except ValueError as newlineError:
            print(newlineError)
            print("\n\n check if you have indeed specified \\n as \n the newline character while opening the text.")
            return
        else:
            pass
        object_part_split = self.atf_section.split("\n@")
        object_part_id_part = object_part_split[0]
        object_part_parts = object_part_split[1:]
        self.object_parts_list = ["@" + part for part in object_part_parts]
        self.object_parts_list.insert(0,object_part_id_part)
        #
        return self.object_parts_list
    #
    def splitLinesOParts(self):
        """
        Splits the object part
        into lines
        """
        #
        self.objectPartLines_list = [objectPart.splitlines() for objectPart in self.object_parts_list]
        #
        return self.objectPartLines_list
    #
    def get_ObjectIdPart(self):
        """
        Gets the part in which
        the id of the text occurs

        # In objectPartLines_list:
        # [0] is the id part, [1] is the type part
        # [2] is the text parts

        """
        #
        self.objectIdPart = self.objectPartLines_list[0]
        #
        return self.objectIdPart
    #
    def get_text_id(self):
        """
        Gets the text id from the
        object id part
        """
        #
        for line in self.objectIdPart:
            c_atf_line = cAtfLineGetter(line)
            if len(c_atf_line.get_id_line()) != 0:
               self.catf_text_dict["text_id"] = c_atf_line.get_id_line()
            elif len(c_atf_line.get_id_alternatives()) != 0:
                self.catf_text_dict["text_id_alternatives"] = c_atf_line.get_id_alternatives()
            elif len(c_atf_line.get_language_line()) != 0:
                self.catf_text_dict["text_language"] = c_atf_line.get_language_line()
        #
        return self.catf_text_dict
    #
    def set_textLang(self):
        """
        sets the text language for
        passing it to the other
        sections
        """
        #
        self.textLang = self.catf_text_dict["text_language"]
        #
        return self.textLang
    #
    def get_objectTypePart(self):
        """
        Gets the parts of
        the text indicated by @

        # In objectPartLines_list:
        # [0] is the id part, [1] is the type part
        # [2] is the text parts

        """
        #
        self.objectTypePart = self.objectPartLines_list[1][0].strip()
        # [1] corresponds to the list which contains only the type string
        # Hence [0].strip()
        #
        return self.objectTypePart
    #
    def get_textParts(self):
        """
        Gets the list of text parts
        from the object part list

        This should correspond to [2:]
        """
        #
        self.objectTextParts = self.objectPartLines_list[2:]
        #
        return self.objectTextParts
    #
    @staticmethod
    def get_single_lines(textParts):
        """
        Gets the list with single elements
        it is used for isolating
        structures like
        @surface a
        @scene 1
        Which usually preceedes
        textual content.
        """
        #
        single_line_list = []
        #
        for i in range(len(textParts)):
            if len(textParts[i]) == 1 and textParts[i][0].startswith("@",0,2):
                single_line_list.append(i)
        #
        single_line_list.append(len(textParts))
        #
        return single_line_list
    #
    @staticmethod
    def set_textRange_list(single_line_list):
        """
        Takes the single line list
        and sets the text range, that is,
        divisions with textual content,
        like
        @column 1,\n 1. an-il etc.
        Which are represented in
        between the elements of the single line list.
        We take thus the elements of the single line list
        as the markers of the beginning and end of the division with
        textual content.
        """
        #
        range_list = []
        #
        for no in range(len(single_line_list)):
            # [0, 3, 6, 7,9] -> no == index of the elements
            if no + 1 < len(single_line_list):
                if single_line_list[no+1] - single_line_list[no] > 1:
                    # Ex. 3 - 1 or 9 - 7
                    char_range = list(range(single_line_list[no], single_line_list[no+1]))
                    # [0, 3, 6, 7,9] -> range(0,3), range(3,6), range(7,9)
                    char_range.append(single_line_list[no+1])
                    # The last element will be searched in the next range.
                    # afterwards
                    range_list.append(char_range)
        #
        return range_list
    #
    @staticmethod
    def get_partHierarchy(range_list):
        """
        Sets additional ranges for marking the hierarchy.
        For example, in previous method, the part which is
        attributed to the lines 6-9 was not included.
        We are going to include that now. And sort the
        list so that the part hierarchies become apparent.
        In a document which has single line list of
        [0, 3, 6, 7,9]
        The part 6-9 clearly is a superior division and
        7-9 is a subdivision of the superior division.
        """
        #
        new_range_list = []
        #
        for no in range(len(range_list)):
            if no + 1 < len(range_list):
                char_range_list = range_list[no]
                # Ex.[0,1,2,3] in [[0, 1, 2, 3], [3, 4, 5, 6], [7, 8, 9]]
                char_range_2_list = range_list[no+1]
                # Ex. [3, 4, 5, 6] in same.
                lastCharacter = char_range_list.pop()
                # Ex. 3 in [0,1,2,3]
                #
                if lastCharacter not in char_range_2_list:
                    # Ex. 6 not in [7, 8, 9]
                    new_range_list.append(char_range_2_list)
                    lastCharacter_2 = char_range_2_list.pop()
                    # Ex. 9 in [7, 8, 9]
                    newRange = list(range(lastCharacter,lastCharacter_2))
                    new_range_list.append(newRange)
                    # newRange == [6,7,8]
                else:
                    new_range_list.append(char_range_list)
                    new_range_list.append(char_range_2_list)
        #
        new_sorted_range = sorted(new_range_list, key=lambda x:x[0])
        # Ex. [[0, 1, 2], [3, 4, 5], [6, 7, 8], [7, 8]]
        #
        return new_sorted_range
    #
    def set_partHierarchy(self):
        """
        Wraps the staticmethods
        and sets the part hierarchy
        that is going to be used later on
        with partdicts
        """
        #
        singlelines = self.get_single_lines(self.objectTextParts)
        textRange_list = self.set_textRange_list(singlelines)
        self.textPartsHierarchy = self.get_partHierarchy(textRange_list)
        #
        return self.textPartsHierarchy
    #
    def set_text_PartInfo(self):
        """
        Sets what we have so far
        to the text dictionary
        """
        #
        self.catf_text_dict["text_objectType"] = self.objectTypePart
        self.catf_text_dict["text_textPartCount"] = len(self.objectTextParts)
        #[2:] because [0] is the id part and [1] is the type part
        #
        return self.catf_text_dict
    #
    @staticmethod
    def textPartString(textPart):
        """
        params: textPart, []
        return: textPart_str, ''

        Regroups the lines
        belonging to the part in
        string form for handling
        Another Language Occurances
        """
        #
        partLines = textPart[1:]
        # Since [0] is the part title indicated with @
        # the rest should be text lines, comments, etc.
        textPart_str = "\n".join(partLines)
        #
        return textPart_str
    #
    def get_ALs(self, textPart_str):
        """
        Passes the textPart_str to AL
        handler for getting Another Language
        occurances
        """
        #
        alClass = cAtfALHandler(textPart_str)
        alClass.set_textLang(self.textLang)
        alClass.alLanguage = self.alLanguage
        alOcS = alClass.get_ALOcS()
        #
        return alOcS
    #
    @staticmethod
    def lineDicts(textPartLine):
        """
        Converts the text part line
        to a line dict
        """
        #
        lineClass = cAtfLineDictBuilder(textPartLine)
        lineDict = lineClass.lineDictBuild()
        #
        return lineDict
    #
    def worDictBuilder(self,lineWord):
        """
        Converts the words inside
        a line dict to a
        wordDict by using cAtfWordDictBuilder
        """
        #
        wordClass = cAtfWordDictBuilder(lineWord)
        wordClass.set_textLang(self.textLang)
        wordClass.set_wordLang(self.wordLang)
        wordClass.set_detLang(self.detLang)
        #
        word_dict = wordClass.wordDictBuild()
        #
        return word_dict
    #
    @staticmethod
    def signDictBuilder(WordSign):
        """
        Converts the signs inside
        a word dict to
        a signDict by using
        cAtfSignDictBuilder
        """
        #
        signClass = cAtfSignDictBuilder(WordSign)
        sign_dict = signClass.buildSignDict()
        sign_relations_dict_list = signClass.signRelation_dict_list
        #
        return (sign_dict,sign_relations_dict_list)
    #
    def get_SignDicts(self, wordDict):
        """
        Builds sign dicts for the signs
        in a word dict.
        """
        signs = wordDict["word_Signs"]
        signSignRel_tuple_list = [self.signDictBuilder(sign) for sign in signs]
        sign_dict_list = [signSignRelTuple[0] for signSignRelTuple in signSignRel_tuple_list]
        #
        sign_relations_dict_list = [signSignRelTuple[1] for signSignRelTuple in signSignRel_tuple_list]
        # sign relations dict list includes group - group relations
        wordDict["word_Signs"] = sign_dict_list
        wordDict["word_signRelations"] = sign_relations_dict_list
        #
        return wordDict
    #
    def get_WordDicts(self, lineDict):
        """
        Builds word dicts for words
        in a line dict
        """
        #
        words = lineDict["lineWords"]
        wordDict_list = [self.worDictBuilder(word) for word in words]
        lineDict["lineWords"] = wordDict_list
        #
        return lineDict
    #
    def set_partDict(self, textPart):
        """
        Creates the part dictionary
        from the textpart which is an
        element of the objectpart list
        """
        #
        part_dict = {}
        #
        part_dict["part_partTitle"] = textPart[0].strip()
        part_string = self.textPartString(textPart)
        part_dict["part_partString"] = part_string
        partlines = textPart[1:]
        alOccurances = self.get_ALs(part_string)
        # pass text language to al occurances TODO
        part_dict["part_AL_occurances"] = alOccurances
        # and the Adventure of Iteration starts ...
        partLine_dict_list = []
        for line in partlines:
            line_dict = self.lineDicts(line)
            lineWord_dict = self.get_WordDicts(line_dict)
            lineWordDict_list = lineWord_dict["lineWords"]
            linewordsign_dict_list = []
            for lineWordDict in lineWordDict_list:
                wordSigndict = self.get_SignDicts(lineWordDict)
                linewordsign_dict_list.append(wordSigndict)
            lineWord_dict["lineWords"] = linewordsign_dict_list
            partLine_dict_list.append(lineWord_dict)
        #
                #
        #
        part_dict["part_partLines"] = partLine_dict_list
        #
        return part_dict
    #
    def buildTextDict_FP(self):
        """
        Wraps the methods above for
        building the text dictionary
        With one pass.
        The final dictionary doesn't
        include the relative positioning of
        signs, words, and lines
        """
        #
        self.get_atf_section()
        self.get_object_parts()
        # Text is splited into parts
        self.splitLinesOParts()
        # Each object part is splited into lines
        self.get_ObjectIdPart()
        # The part in which one observes the object id
        # is seperated
        self.get_text_id()
        # From the object id part
        # the text id is taken
        self.get_objectTypePart()
        # From the object part list
        # object type part is taken
        self.get_textParts()
        # from the object parts that
        # has been divided into lines
        # textparts are taken
        self.set_text_PartInfo()
        # The type information
        # and partCount is added to
        # text dictionary
        self.textPart_dict_list = [self.set_partDict(textpart) for textpart in self.objectTextParts]
        # part dict is created for each text part.
        self.catf_text_dict["text_textParts"] = self.textPart_dict_list
        #
        return self.catf_text_dict
    #
    @staticmethod
    def set_lineStack(lineDict):
        """
        params: lineDict, {}
        return: lineStack, []
        Creates a lineStack list
        for signs from the word dict
        """
        #
        lineWordPos_list = lineDict["lineWordPos"]
        lineWord_list = lineDict["lineWords"]
        lineStack_list = []
        #
        lineStack = []
        for wordP, word in lineWordPos_list:
            for wordDict in lineWord_list:
                signPos_list = wordDict["word_wordSignsPos"]
                word_str = wordDict["word_word"]
                if word == word_str:
                    for signPos, sign in signPos_list:
                        signCount = [wordP, signPos, sign]
                        lineStack.append(signCount)
        #
        return lineStack
    #
    @staticmethod
    def lineStackDicter(lineStack):
        """
        Builds a dictionary from lineStack
        to be mapped to a key in lineDict
        """
        #
        lineStackEnum = list(enumerate(lineStack))
        lineStackDict_list = []
        #
        for linEnum in lineStackEnum:
            lineStackDict = {}
            linePos = linEnum[0]
            lineEls = linEnum[1]
            lineStackDict["line_RelSignPosition"] = linePos
            # Sign position with respect to line
            lineStackDict["line_wordPosition"] = lineEls[0]
            # Position of the word with respect to line
            lineStackDict["line_signWordPosition"] = lineEls[1]
            # Position of the sign with respect to *word*
            lineStackDict["line_sign"] = lineEls[2]
            # The sign, like an, ir, ANSZE, etc.
            lineStackDict_list.append(lineStackDict)
        #
        return lineStackDict_list
    #
    def set_lineStackDict(self,lineDict):
        """
        Sets the lineStackDict to lineDict
        by using methods above
        """
        #
        lineStack = self.set_lineStack(lineDict)
        lineStack_dict_list = self.lineStackDicter(lineStack)
        lineDict["line_RelSignPositions"] = lineStack_dict_list
        #
        return lineDict
    #
    @staticmethod
    def set_partSignStack(partDict):
        """
        Gets the partSignStack from the partDict
        """
        #
        partSignStack_dictList = []
        partLines_list = partDict["part_partLines"]
        #
        for lineDict in partLines_list:
            lineNo = lineDict["lineNumber"]
            lineSignStack_dictList = lineDict["line_RelSignPositions"]
            for lineSignStack in lineSignStack_dictList:
                lineSignStack["line_lineNumber"] = lineNo
                partSignStack_dictList.append(lineSignStack)
            #
        #
        return partSignStack_dictList
    #
    @staticmethod
    def partStackDicter(partSignStack_dictList):
        """
        Creates the partSignStackDict_list
        """
        #
        partSignSEnum = list(enumerate(partSignStack_dictList))
        part_signStack_list = []
        #
        for partEnum in partSignSEnum:
            partPos = partEnum[0]
            partSignStacks = partEnum[1]
            #
            partSignStacks["part_RelSignPosition"] = partPos
            part_signStack_list.append(partSignStacks)
                #
        #
        return part_signStack_list
    #
    def set_partSignStackDict(self, partDict):
        """
        Sets the partSignStack to partDict
        """
        #
        stackList = self.set_partSignStack(partDict)
        partSignDict_list = self.partStackDicter(stackList)
        #
        partDict["part_RelSignPositions"] = partSignDict_list
        #
        return partDict
    #
    @staticmethod
    def set_textSignStack(textDict):
        """
        Sets the textSignStack from textPart
        """
        #
        textSignStack_dictList = []
        #
        textPart_list = textDict["text_textParts"]
        textPartEnum = list(enumerate(textPart_list))
        for textEn in textPartEnum:
            partPos = textEn[0]
            partDict = textEn[1]
            partSignDict_list = partDict["part_RelSignPositions"]
            #
            for partSignDict in partSignDict_list:
                partSignDict["text_partPosition"] = partPos
                textSignStack_dictList.append(partSignDict)
            #
        #
        return textSignStack_dictList
    #
    @staticmethod
    def textStackDicter(textSignStack_dictList):
        """
        Creates the textSignStackDict, from the list
        """
        #
        textSignSEnum = list(enumerate(textSignStack_dictList))
        text_signStack_list = []
        #
        for textEnum in textSignSEnum:
            textPos = textEnum[0]
            textSignStacks = textEnum[1]
            textSignStacks["text_RelSignPosition"] = textPos
            text_signStack_list.append(textSignStacks)
                #
        #
        return text_signStack_list
    #
    def set_textStackDict(self, textDict):
        """
        sets textStactDict to the textDict
        """
        #
        stackList = self.set_textSignStack(textDict)
        textSignDict_list = self.textStackDicter(stackList)
        #
        textDict["text_RelSignPositions"] = textSignDict_list
        #
        return textDict
    #
    def relSignSetter(self):
        """
        Wrapping up the methods above
        """
        #
        textPart_list = self.catf_text_dict["text_textParts"]
        text_part_dict_list = []
        #
        for textPart in textPart_list:
            partLines = textPart["part_partLines"]
            part_line_dicts = []
            for lineDict in partLines:
                lineModi = self.set_lineStackDict(lineDict)
                part_line_dicts.append(lineModi)
            #
            textPart["part_partLines"] = part_line_dicts
            partModi = self.set_partSignStackDict(textPart)
            text_part_dict_list.append(partModi)
        #
        self.catf_text_dict["text_textParts"] = text_part_dict_list
        #
        text_dict_modi = self.set_textStackDict(self.catf_text_dict)
        #
        self.catf_text_dict = text_dict_modi
        #
        return self.catf_text_dict
    #
    def textSignCount(self):
        """
        Gets and sets the sign count for the text.
        """
        #
        textSignList = self.catf_text_dict["text_RelSignPositions"]
        lenSigns = textSignList[-1]["text_RelSignPosition"] + 1
        # Total length is equal to last element position plus 1
        #
        self.catf_text_dict["text_totalSignCount"] = lenSigns
        #
        return self.catf_text_dict
    #
    # TODO Determinatiflerin ayrıştırılmasında problem var
    # Şöyle şeyler oluyor line_sign': '{d}en' dikkat.
    #
    @staticmethod
    def set_partWordStack(partDict):
        """
        Sets the word stack from the part dict
        """
        #
        partWordStack_list = []
        #
        partLines_list = partDict["part_partLines"]
        #
        for partLine_dict in partLines_list:
            lineWordPos_list = partLine_dict["lineWordPos"]
            lineNo = partLine_dict["lineNumber"]
            for lineWordPos in lineWordPos_list:
                word = lineWordPos[1]
                wordP = lineWordPos[0]
                wordCount = [lineNo, wordP, word]
                partWordStack_list.append(wordCount)
            #
        #
        return partWordStack_list
    #
    @staticmethod
    def partWordStackDicter(partWordStack_list):
        """
        creates the dict from the partWordStack and
        stocks everything in a list.
        """
        #
        partWEnum = list(enumerate(partWordStack_list))
        partWordStack_dictList = []
        #
        for partWe in partWEnum:
            partPos = partWe[0]
            stackDict = {}
            wordCount = partWe[1]
            stackDict["part_RelWordPosition"] = partPos
            stackDict["line_lineNumber"] = wordCount[0]
            stackDict["line_lineWordPosition"] = wordCount[1]
            stackDict["line_word"] = wordCount[2]
            partWordStack_dictList.append(stackDict)
        #
        return partWordStack_dictList
    #
    def set_partWordStackDict(self, partDict):
        """
        Sets the partWordStack_dictList to partDict
        """
        #
        stackList = self.set_partWordStack(partDict)
        stackDict_list = self.partWordStackDicter(stackList)
        partDict["part_RelWordPositions"] = stackDict_list
        #
        return partDict
    #
    @staticmethod
    def set_textWordStack(textDict):
        """
        Sets the textStackList from textDict
        """
        #
        textWordStack_list = []
        textParts = textDict["text_textParts"]
        #
        textPEnum = list(enumerate(textParts))
        #
        for textP in textPEnum:
            partPos = textP[0]
            partDict = textP[1]
            partRels = partDict["part_RelWordPositions"]
            #
            for partR in partRels:
                partR["text_partPosition"] = partPos
                textWordStack_list.append(partR)
            #
        #
        return textWordStack_list
    #
    @staticmethod
    def textWordStackDicter(textWordStack_list):
        """
        Creates the dict from textWordStack_list
        """
        #
        textWordStack_dictList = []
        textWordEnum = list(enumerate(textWordStack_list))
        #
        for textWE in textWordEnum:
            textPos = textWE[0]
            stackDict = textWE[1]
            stackDict["text_RelWordPosition"] = textPos
            textWordStack_dictList.append(stackDict)
        #
        return textWordStack_dictList
    #
    def set_textWordStackDict(self, textDict):
        """
        Sets the wordStack_dictList to textDict
        """
        #
        stackList = self.set_textWordStack(textDict)
        stack_dictList = self.textWordStackDicter(stackList)
        textDict["text_RelWordPositions"] = stack_dictList
        #
        return textDict
    #
    def relWordSetter(self):
        """
        Sets the relative word Positions
        and to catf_text_dict
        Wraps up the methods above.
        """
        #
        textPart_list = self.catf_text_dict["text_textParts"]
        text_part_dict_list = []
        #
        for textPart in textPart_list:
            textPartModi = self.set_partWordStackDict(textPart)
            text_part_dict_list.append(textPartModi)
            #
        self.catf_text_dict["text_textParts"] = text_part_dict_list
        textModi = self.set_textWordStackDict(self.catf_text_dict)
        self.catf_text_dict = textModi
        #
        return self.catf_text_dict
    #
    @staticmethod
    def set_textLineStack(textDict):
        """
        Creates the stacklist for lines in a partdict
        """
        #
        textLineStack_list = []
        #
        textparts = textDict["text_textParts"]
        textpartEnum = list(enumerate(textparts))
        #
        for textpartE in textpartEnum:
            partPos = textpartE[0]
            textpart = textpartE[1]
            lines = textpart["part_partLines"]
            for line in lines:
                lineNo = line["lineNumber"]
                lineCount = [partPos, lineNo]
                textLineStack_list.append(lineCount)
            #
        #
        return textLineStack_list
    #
    @staticmethod
    def textLineStackDicter(textLineStack_list):
        """
        sets the dictionary for textLineStack_list
        """
        #
        textLineStack_dictList = []
        #
        textLinEn = list(enumerate(textLineStack_list))
        #
        for textLin in textLinEn:
            textPos = textLin[0]
            stackList = textLin[1]
            stackDict = {}
            stackDict["text_RelLinePosition"] = textPos
            stackDict["text_partPosition"] = stackList[0]
            stackDict["line_lineNumber"] = stackList[1]
            textLineStack_dictList.append(stackDict)
            #
        #
        return textLineStack_dictList
    #
    def set_textLineStackDict(self, textDict):
        """
        sets the textlinestack_dictList to textDict
        """
        #
        stackList = self.set_textLineStack(textDict)
        stackDict_list = self.textLineStackDicter(stackList)
        textDict["text_RelLinePositions"] = stackDict_list
        #
        return textDict
    #
    def relLineSetter(self):
        """
        Sets the relative line Positions
        to catf_text_dict
        Wraps up the methods above
        """
        textModi = self.set_textLineStackDict(self.catf_text_dict)
        self.catf_text_dict = textModi
        #
        return self.catf_text_dict
    #
    def buildTextDict_SP(self):
        """
        Builds the Text dictionary
        With 2 passes.
        Includes the relative positioning
        of signs, words and lines
        """
        self.buildTextDict_FP()
        self.relSignSetter()
        self.relWordSetter()
        self.relLineSetter()
        lineCount = self.catf_text_dict["text_RelLinePositions"]
        self.catf_text_dict["text_totalLineCount"] = lineCount[-1]["text_RelLinePosition"] + 1
        # Total length is equal to last item position + 1 for compensating zero indexing
        wordCount = self.catf_text_dict["text_RelWordPositions"]
        self.catf_text_dict["text_totalWordOccuranceCount"] = wordCount[-1]["text_RelWordPosition"] + 1
        # Counts the each occurance of a word. Doesn't filter anything
        signCount = self.catf_text_dict["text_RelSignPositions"]
        self.catf_text_dict["text_totalSignOccuranceCount"] = signCount[-1]["text_RelSignPosition"] + 1
        # Count for the each occurance of a sign. Doesn't filter anything.
        #
        return self.catf_text_dict
    #
