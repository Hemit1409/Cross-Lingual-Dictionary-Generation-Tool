

from Stemming import LanguageCode

if LanguageCode == 'gu':
    FileName = 'GujaratiOutput.txt'
    StartingASCIIValue = 2693
    EndingASCIIValue = 2815
elif LanguageCode == 'hi':
    FileName = 'HindiOutput.txt'
    StartingASCIIValue = 2304
    EndingASCIIValue = 2431



def englishRemoval():
    with open(FileName, 'r', encoding='utf-8') as ORER:
        DataFrom_ORER = ORER.readlines()
        LengthOf_DataFromORER = len(DataFrom_ORER)
        EmptyList = []

        for iterVar_One in range(0, LengthOf_DataFromORER):
            LengthOf_Element = len(DataFrom_ORER[iterVar_One])
            StartingIndex = 1
            EndingIndex = LengthOf_Element - 2

            if (StartingIndex < LengthOf_Element) and (0 < EndingIndex > StartingIndex):
                for iterVar_Two in range(StartingIndex, EndingIndex):
                    if (ord(DataFrom_ORER[iterVar_One][0]) < StartingASCIIValue or ord(
                            DataFrom_ORER[iterVar_One][0]) > EndingASCIIValue) or (
                            ord(DataFrom_ORER[iterVar_One][EndingIndex]) < StartingASCIIValue or ord(
                        DataFrom_ORER[iterVar_One][EndingIndex]) > EndingASCIIValue):
                        EmptyList.append(iterVar_One)
                        break
                    elif ord(DataFrom_ORER[iterVar_One][iterVar_Two]) < StartingASCIIValue or ord(
                            DataFrom_ORER[iterVar_One][iterVar_Two]) > EndingASCIIValue:
                        EmptyList.append(iterVar_One)
                        break
            else:
                EmptyList.append(iterVar_One)

        def listReversal(ListName):
            return [element for element in reversed(ListName)]

        ReversedList = listReversal(EmptyList)

        for iterVar_Two in ReversedList:
            DataFrom_ORER.pop(iterVar_Two)

    ORER.close()

    with open(FileName, 'w', encoding='utf-8') as removeEnglish:
        for iterVar_Three in DataFrom_ORER:
            removeEnglish.write(iterVar_Three)


englishRemoval()
