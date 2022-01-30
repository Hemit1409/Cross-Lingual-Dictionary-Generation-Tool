import tkinter.filedialog
import tkinter
import random
from indicnlp.tokenize import indic_tokenize
from collections import OrderedDict
import os
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
script_dir2 = os.path.split(script_dir)[0]
print(script_dir2)

InputDataFileName = tkinter.filedialog.askopenfilename()
ReadInputDataFile = open(InputDataFileName, 'r', encoding='utf-8')
InputData = ReadInputDataFile.read()

LengthOf_InputData = len(InputData)
GujaratiCOUNTER = 0
HindiCOUNTER = 0
LanguageCode = ''  # empty string

for iterVar_One in range(0, 10):
    RandomIndex = random.randint(0, LengthOf_InputData - 1)
    ASCII_OfElement = ord(InputData[RandomIndex])

    if ASCII_OfElement == 32:
        continue

    else:
        if 2693 <= ASCII_OfElement <= 2815:
            GujaratiCOUNTER = GujaratiCOUNTER + 1
        if 2304 <= ASCII_OfElement <= 2431:
            HindiCOUNTER = HindiCOUNTER + 1

if GujaratiCOUNTER > HindiCOUNTER:
    print('Input Langauge Is Gujarati')
    LanguageCode = 'gu'
elif HindiCOUNTER > GujaratiCOUNTER:
    print('Input Language Is Hindi')
    LanguageCode = 'hi'
else:
    print('Run this Program Again')


def Tokenization():
    InputDataTokenization = indic_tokenize.trivial_tokenize(InputData, LanguageCode)
    with open(script_dir2+'\data\IntermediateOutput.txt', 'w', encoding='utf-8') as IHO:
        for iterVar_Two in InputDataTokenization:
            IHO.write(iterVar_Two + '\n')
    IHO.close()


Tokenization()


def stopWordsRemoval():
    global Output
    with open(script_dir2+'\data\IntermediateOutput.txt', 'r', encoding='utf-8') as IO:
        InputDataFrom_IO = IO.readlines()

    if LanguageCode == 'gu':
        with open(script_dir2+'\data\GujaratiStopWords.txt', 'r', encoding='utf-8') as SW:
            InputDataFrom_SW = SW.readlines()
        Output = open(script_dir2+'\data\GujaratiOutput.txt', 'w', encoding='utf-8')
    elif LanguageCode == 'hi':
        with open(script_dir2+'\data\HindiStopWords.txt', 'r', encoding='utf-8') as SW:
            InputDataFrom_SW = SW.readlines()
        Output = open(script_dir2+'\data\HindiOutput.txt', 'w', encoding='utf-8')

    LengthOf_InputDataFrom_IO = len(InputDataFrom_IO)
    LengthOf_InputDataFrom_SW = len(InputDataFrom_SW)

    COUNTER = 0
    for iterVar_Three in range(0, LengthOf_InputDataFrom_IO):
        for iterVar_Four in range(0, LengthOf_InputDataFrom_SW):
            if InputDataFrom_IO[iterVar_Three] == InputDataFrom_SW[iterVar_Four]:
                COUNTER = COUNTER + 1
                break

        if COUNTER == 0:
            Output.write(InputDataFrom_IO[iterVar_Three])

        COUNTER = 0

    IO.close()
    SW.close()
    Output.close()


stopWordsRemoval()


def duplicatesRemoval():
    global FileName
    if LanguageCode == 'gu':
        FileName = script_dir2+'\data\GujaratiOutput.txt'
    elif LanguageCode == 'hi':
        FileName = script_dir2+'\data\HindiOutput.txt'

    ExistingData_OutputFile = open(FileName, 'r', encoding='utf-8')
    InputDataFrom_EOF = ExistingData_OutputFile.readlines()
    ExistingData_OutputFile.close()

    NewDataFor_OutputFile = list(OrderedDict.fromkeys(InputDataFrom_EOF))

    NewData_OutputFile = open(FileName, 'w', encoding='utf-8')
    for iterVar_Five in NewDataFor_OutputFile:
        NewData_OutputFile.write(iterVar_Five)
    NewData_OutputFile.close()


duplicatesRemoval()
