# Importing Necessary Files
from indicnlp.tokenize import sentence_tokenize
from indicnlp.tokenize import indic_tokenize  # importing indic_tokenize for word tokenization
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator  # importing
# UnicodeIndicTransliterator for gujarati phonetics to hindi phonetics

# Importing tkinter package for direct file choosing process
import tkinter.filedialog
import fileinput
import tkinter

# Way 1 -> Original Started From Here Using open function : Need to Give File name / particular path of file (
# Completed Upto  removal of stop words)
IntermediateInputFileGujarati = open(r"data/gujsentences.txt", "r+", encoding='utf-8')  # opening demo input file
IntermediateInputStringGujarati = IntermediateInputFileGujarati.read()  # reading input file using object of input file
HindiTrasliteration = UnicodeIndicTransliterator.transliterate(IntermediateInputStringGujarati, "gu",
                                                               "hi")  # phonetic conversion from gujarati to hindi
print(HindiTrasliteration)  # printing converted data

HindiWordTokenization = indic_tokenize.trivial_tokenize(HindiTrasliteration,
                                                        lang="hi")  # tokenization applied to the hindi conversion
print(HindiWordTokenization)  # printing tokenized data

IntermediateOutputHindiFile = open('data/OutputHindiDemo.txt', "w",
                                   encoding='utf-8')  # opening output file for writing all tokens
for ObjectToWrite in HindiWordTokenization:  # running for loop for writing all tokens into opened file
    IntermediateOutputHindiFile.write(ObjectToWrite + "\n")  # writing
IntermediateOutputHindiFile.close()  # object is closed


# defining function stopWordsFunction() to remove stop words
def stopWordsFunction():
    OpeningTokensFile = open('data/OutputHindiDemo.txt', "r+", encoding='utf-8')
    Tokens = OpeningTokensFile.readlines()  # opening OutputHindiDemo file which contains tokens of hindi phonetics
    OpeningStopWordsFile = open('data/HindiStopWordsList.txt', "r+", encoding='utf-8')
    StopWords = OpeningStopWordsFile.readlines()  # opening HindiStopWordsList file which contains all stop words
    CreatingOROpeningNewFile = open('data/FinalOutputFile.txt', "w+", encoding='utf-8')  # creating / opening new file

    LengthOfTokens = len(Tokens)  # taking total number of tokens from Tokens
    LengthOfStopWords = len(StopWords)  # taking total number of stop words from StopWords
    print(LengthOfTokens)  # printing total number of tokens
    print(LengthOfStopWords)  # printing total number of stop words

    counter = 0  # declaring counter variable and set to zero
    for TokenReadingVariable in range(0, LengthOfTokens):
        for StopWordsReadingVariable in range(0, LengthOfStopWords):
            if Tokens[TokenReadingVariable] == StopWords[StopWordsReadingVariable]:  # comparing each tokens with
                # stop words
                counter = counter + 1  # increasing counter by plus one
        if counter >= 1:  # if counter is greater than one then it means selected word / token is stop words
            print()
        else:  # if counter = 0 then it means word / token is not stop word
            CreatingOROpeningNewFile.write(
                Tokens[TokenReadingVariable])  # writing that particular word / token into file
        counter = 0  # set counter again to zero for next word / token


stopWordsFunction()  # calling stopWordsFunction

# Way 2-> Original started from here Using tkinter : Not need to give file name / particular path of file (Incompleted)
# IntermediateInputFileGujarati = tkinter.filedialog.askopenfilename()
# OpeningFileObject = open(IntermediateInputFileGujarati, "r+", encoding="utf-8")
# IntermediateInputStringGujarati = OpeningFileObject.read()
# HindiTokenization = UnicodeIndicTransliterator.transliterate(IntermediateInputStringGujarati, "gu", "hi")
# print(HindiTokenization)
# HindiWordTokenization = indic_tokenize.trivial_tokenize(HindiTokenization, lang="hi")
# print(HindiWordTokenization)
