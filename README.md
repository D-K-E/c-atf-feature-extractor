# c-atf-feature-extractor
A Preprocessor for C-ATF files

The extractor is entirely written in python. It takes a c-atf text and spits out a huge python heavily nested dictionary. An api would be available for facilitating the usage of it. 

**The Resulting dictionary contains the following information with regard to text**:

### On text level:   

- text_textPartCount: Number of parts in a texts: like @obverse, @reverse, etc.   

- text_totalSignOccuranceCount: Total count of sign occurrences, this is to be differentiated from the number of signs used in a document. For example a text might have 30 signs with each of them occurring 3 times, thus total occurrence count would be 90. I will also provide number of signs, later on.

- text_RelSignPositions: Relative Sign Positions with respect to text level. Meaning that the signs are counted throughout the text without considering changes in line or part. If the line 1 has 20 sign occurrences, for line 2, the counter continues from where the line 1 has left off. 

- text_RelWordPositions: Relative Word Positions with respect to text level. Same as signs but done for words.

- text_language: Gives the specified language in the protocol section of the c-atf document, ex.. #atf: lang akk.

- text_totalLineCount: Gives the total number of lines in the text.

- text_objectType: Gives the object type stated with @, ex. @tablet, etc.

- text_id: Gives the text id, ex.. P480793, etc.

- text_RelLinePositions: Relative Line Positions with respect to text level. Same as signs but done for lines.

- text_textParts: A list containing the parts of the text. Parts are stored as dictionaries.   

-----

### On Part Level:

- part_partTitle: Gives the title of the part indicated with @, ex. @observe, @reverse, etc.

- part_partString: Gives the text of the part as string.

- part\_AL\_occurances: Gives the list of Another Language Occurrences, these are indicated with _ in c-atf they can contain multiple lines, and a language switch. We'll explain some of the features contained by this in a second.

- part_RelSignPositions: Relative Sign Positions with respect to part level. Same thing as text level, but this time the counter starts from zero for each part.

- part_RelWordPositions: Relative Word Positions with respect to part level. Same thing as signs but done for words.

- part_partLines: A list of dictionaries. Dictionaries relate information about the states of individual lines.

#### AL Occurances:

Another language occurances can be dispersed to multiple lines thus they are handled at a part level rather then in line level.

The key part\_AL\_occurances gives a list of list of dicts. Each list of dicts represent an AL occurrence. Each dict represents a word. 
**The structure of the dict is as follows**:

- alWord\_AlOc: is a string representation of the entire Another Language occurrence. Ex. For an AL occurrence of \_an kur\_u2, the dictionary might belong to the word kur_u2, but this key would contain the \_an kur\_u2 anyway.

- alWord\_AlOc_Position: contains a dictionary with following keys: alWord\_Position, and totalWords\_AlOc: First one indicates the position of the another language word inside the AL occurrence, the second one gives the total number of AL words inside the AL occurrence.

- alWord_LineNumber: Stores the number of the line which contains the AL word.

- alWord\_LinePosition: contains a dictionary with the following keys: alWord\_Position and totalWords_Line: First one indicates the position of the AL word inside the line, the second one gives the total number of words in the line.

- alWord\_language: Stores the language of the another language occurrence if stated, ex: if there is something like %hit right after the underscore it would give the hit as the value of this key.

- alWord\_textLanguage: Stores the language of the text, indicated in the protocol

- alWord\_word: Stores the AL word, so for an AL occurrence of \_an kur\_u2, this key would contain only kur\_u2.

---

### On Line Level:

- lineText: Contains the string representation of the line.
- lineNumber: Contains the line number.
- isLineStructure: Stores a boolean value. Indicates whether the line is a comment about the structure indicated with $ in C-ATF.
- isLineContent: Stores a boolean value. Indicates whether the line is a comment about the content of another line indicated with # in C-ATF.
- lineWordCount: Stores the the number total word count in the line.
- lineWordPos: Line Word Positions: Stores the words with their positions in the line. Different from the lineWords
- lineWords: Stores a list of dictionaries. Each dictionary represent a unique word in the line. 
- line\_RelSignPositions: Relative Sign Positions with respect to line level. Same thing as in part level, this time the counter results to 0 at the beginning of each line.

-------

### On Word Level:

Word dictionary includes some features from sign dictionary for facilitating processing afterwards.

- word\_hasComplement: Boolean value. True if the word has a compliment indicated with +.
- word\_Signs: Stores a list of dictionaries. Each dictionary represent a unique sign.
- word\_hasUnknownReading: Boolean value. True if the word has an uppercase reading outside of a compound sign.
- word\_hasNutillu: Boolean value. True if the word has a sign with nutillu modifier.
- word\_hasRotated: Boolean value. True if the word has a sign with rotation modifier.
- word\_hasAllograph: Boolean value. True if the word has a sign with allograph indicator ~.
- word\_hasDamage: Boolean value. True if the word has a sign with #.
- word\_punctuationDict: Stores a dictionary which includes information about the punctuation. Keys are punctuation\_punctElement, and punctuation\_punctGrapheme: First one contains the value of the punctuation without the qualifying grapheme, ex. *, /; the second one contains the grapheme qualifying the punctuation, ex. the disz in *(disz).
- word\_hasSpecification: Boolean value. True if the word has parentheses in it.
- word\_wordSignCount: Stores the sign occurrence count for a word.
- word\_hasGunu: Boolean value. True if the word has a sign with gunu modifier.
- word\_isSpecifiedWordDivider: boolean value. True if the word is composed of the following structure: /(GRAPHEME).
- word\_signRelations: Stores a list of dictionaries. Each dictionary represents a relation indicated with an operator. Contained relation types are, sign-sign, sign-group, group-sign, group-group.
- word\_hasKabatenu: Boolean value. True if the word has a sign with kabatenu modifier.
- word\_isDColon: Boolean value. True if the word is punctuation of Double Colon '::'.
- word\_hasJoining: Boolean value. True if the word has the joining operator in it.
- word\_hasFlat: Boolean value. True if the word has a sign with flat modifier.
- word\_hasCrossing: Boolean value. True if the word has the crossing operator.
- word\_hasCollation: Boolean value. True if the word has a collation indicated with '*'.
- word\_hasComposite: Boolean value. True if the word has compound sign in it.
- word\_hasVertReflected: Boolean value. True if the word has a sign with vertically Reflected modifier.
- word\_hasQuery: Boolean value. True if the word has a sign with ?.
- word\_hasFormVariant: Boolean. True if the word has \.
- word\_hasSpecialAllograph: Boolean value. True if the word has a special allograph. 
- word\_determinatives: Stores a list of tuples of dicts. Each dict represents a sign in a determinative. And each tuple represents a determinative. Keys of this determinative sign dictionary will be explained below.
- word\_numberDict: Stores a dict with following keys. number\_repetitionCount, number\_grapheme: First one indicates the repetition count of a number, ex. n+1, n, 4, etc. The second one indicates the grapheme of the number, ex. asz in 4(asz), etc.
- word\_hasCurved: Boolean value. True if the word has a sign with curved modifier.
- word\_hasContaining: Boolean value. True if the word has the containing operator.
- word\_hasCorrection: Boolean value. True if the word has a sign with !.
- word\_word: String representation of the white-space delimited word.
- word\_hasSheshig: Boolean value. True if the word has a sign with sheshig modifier.
- word\_isColon: Boolean value. True if the word is a punctuation of the type, :.
- word\_isBulletSpecified: Boolean value. True if the word is a punctuation of the type *(GRAPHEME).
- word\_wordSignsPos: List of tuples. Stores the signs with their relative positions inside the word.
- word\_isNumber: Boolean value. True if the word belongs to one of the three number types specified by Grapheme Description Language of ORACC.
- word\_wordLang: Stores the information of the language of the word. This can be different from the text language if the word is inside an AL occurrence.
- word\_hasVariant: Boolean value. True if the word has a sign with variant modifier.
- word\_hasAbove: Boolean value. True if the word has the above operator.
- word\_hasTenu: Boolean value. True if the word has a sign with tenu modifier.
- word\_isColonDQ: Boolean value. True if the word is a punctuation of the type, :".
- word\_hasHorReflected: Boolean value. True if the word has a sign with Horizontally Reflected modifier.
- word\_isColonRQ: Boolean value. True if the word is a punctuation of the type, :' or MZL592~b.
- word\_hasBeside:  Boolean value. True if the word has the beside operator.
word\_isBullet: Boolean value. True if the word is a punctuation of the type, *.
word\_hasContainingGroup: Boolean value. True if the word has containing operator with parentheses.
word\_isWordDivider: Boolean value. True if the word is an unspecified word divider.
word\_hasZidatenu: Boolean value. True if the word has a sign with zidatenu modifier.

#### Determinatives:

Each determinative of the word is a tuple, which contains dictionaries representing signs.   

**The structure of the dictionary is of the following**:  

- detSign\_DetPosition: stores a dictionary with following keys. detSign\_position, totalSigns\_determinative. First one contains the position of the sign inside the determinative. Second one contains total number of signs inside the determinative.
- detSign\_WordPosition: stores a dictionary with following keys. detSign\_position, totalSigns\_word. First one stores the position of the sign inside the word. Second one contains total number of signs inside the word.
- detSign\_det: Stores the string representation of the determinative.
- detSign\_detMark: Stores a string representation. It can have three values: Inpos, postpos, prepos. Prepos, for determinatives at the beginning of a word. Postpos for determinatives at the end of a word. Inpos for determinatives that are neither at the beginning nor at the end of the word. They maybe used for example for determinatives that follow other determinatives inside a word.
- detSign\_detSign: Stores the string representation of the sign of the determinative to which the dictionary is consecrated.
- detSign\_det\_WordPos: Stores a tuple which contains the beginning and the end of the sign range of the determinative which contains the above mentioned sign. Ex. for a made up word like {gesz}{an-il-hal}sza-pa-ra-ku2-me-{mesz}, the dictionary concerning il of {an-il-hal} would contain (1,3), since gesz is in the 0 position.

----

### On Sign Level:

Apart from the 'is' versions of the sign features indicated in word level, ex. isDamaged instead of hasDamage. Sign dictionary has the following
information keys:

- sign\_isPartOfCompound: Boolean value. True if the sign is part of a compound sign, ex. KA in KAxKA.
- sign\_nestLevel: Stores the nest level of the sign if the sign is contained in a compound sign involving groups, ex. 1 for KA in IR3x(AN.KA). The complete compound sign is considered as the 0 and each balanced parentheses is counted as a nest indicator.
- sign\_relatedSigns: Stores a dictionary. Its keys will be explained below.
- sign\_sign: Stores the string representation of the sign.
- sign\_compoundSign: Stores the string representation of the compound sign if the sign is a part of a compound sign.

#### Sign Relations:

These are indicated at two levels: at word level and at sign level. Word level representation contains group-group relations which could not be conceived at a sign level. A more elegant solution would be to implement a compoundSignHandler class for this occasion, this will most probably be done in the future. However sign relation dictionaries contained at both of the levels have the same keys.

**The structure of the sign relation dictionary is of the following**:

- SR\_operator: String representation of the operator, ex: +, x, %, etc.
- SR\_operator\_antec: String representation of the characters before the operator.
- SR\_operator\_subsq: String representation of the characters after the operator.
- SR\_nest\_level: Indicates the nest level of sign relation occurrence.
- SR\_nest\_content: Stores the string representation of the text content in which a sign relation occurs.
- SR\_compoundSign: Stores the string representation of the compound sign in which the nested sign relation occurrence is observed.
- SR\_nest\_range: Stores the character range of the nest in which the sign relation is observed.
- SR\_relation\_type: Stores a dictionary with the following keys. operator\_antecedent, operator\_subsequent. First one indicates whether a group or a sign comes before the operator, the second one indicates whether a group or sign comes after the operator.
- SR\_operator\_position: Stores the character position of the operator. Position is with regard to the compound sign's character range.
- SR\_operator\_type: Stores the operator type, ex. crossing, above, joining, etc.
- SR\_operator\_antec\_range: Stores the character range of the elements that come before the operator.
- SR\_operator\_subseq\_range: Stores the character range of the elements that come after the operator.

----

## Usage Example:

For now the parser is conceived for documents containing individual texts like in [here] (http://cdli.ucla.edu/search/archival_view.php?ObjectID=P480793 "Random Example from CDLI")

For now I am more concerned with fine tuning the parser rather than supporting multiple documents at once, because supporting multiple documents at once is quite easy. I would just need to add couple of lines to initial section getter. 

To use the feature extractor on a brute text like this [one](https://gist.github.com/D-K-E/dc7f5fcb7815b1e52bfb4c763bb0b3ac "Downloaded Single Text From CDLI") use the following:

After importing the cAtfFeatExtractor.py from the extractor module.

```python

with open("Archival view of P462811.txt","r",encoding="utf-8", newline="\n") as cAtfFile:
    test_file = cAtfFile.read()

test_textClass = cAtfTextBuilder(test_file)

test_text = test_textClass.buildTextDict_SP()

```

If you use `FP`, First Pass, instead of `SP`, Second Pass, at the end of `buildTextDict_` your dictionary would not have the relative positions of the signs with regard to different levels and total counts with regard to different levels. Use that if you don't need those.
