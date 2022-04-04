from collections import OrderedDict  # To remove duplicate from FinalOutputFile

with open('data/FinalOutputFile.txt', "r", encoding='utf-8') as fof:
    tokensList = fof.readlines()
    LengthOfTokensList = len(tokensList)
    print(tokensList[1])
    for iterationVariable in range(0, LengthOfTokensList):
        LengthOfTokensAtIndex = len(tokensList[iterationVariable])

        if LengthOfTokensAtIndex >= 3:
            if (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ं') and (
                    tokensList[iterationVariable][LengthOfTokensAtIndex - 3] == 'ा') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 4] == 'म'):  # Logic for 'मां' : 3 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 4))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"
                print(tokensList)

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ी') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 3] == 'न'):  # Logic for 'नी' : 2 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 3))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ी') and (
                    tokensList[iterationVariable][LengthOfTokensAtIndex - 3] == 'थ') and (
                    tokensList[iterationVariable][LengthOfTokensAtIndex - 4] == 'ा'):  # Logic for 'ाथी'
                if LengthOfTokensAtIndex == 7:  # Logic for निटाथी, रिटाथी, मिनाथी, सित्ताथी, गीताथी, टीनाथी, तिक्षाथी : 3 space movement
                    tokensList[iterationVariable] = ''.join(
                        tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 3))
                    tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"
                else:  # Logic for गुस्साथी
                    tokensList[iterationVariable] = ''.join(
                        tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 4))
                    tokensList[iterationVariable] = tokensList[iterationVariable] + 'ो' + "\n"

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ी') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 3] == 'थ'):  # Logic for 'थी' : 2 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 3))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'े') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 3] == 'न'):  # Logic for 'ने' : 2 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 3))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ा') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 3] == 'न'):  # Logic for 'ना' : 2 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 3))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ो') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 3] == 'न'):  # Logic for 'नो' : 2 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 3))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ं') and (
                    tokensList[iterationVariable][LengthOfTokensAtIndex - 3] == 'ु') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 4] == 'न'):  # Logic for 'नुं' : 3 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 4))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ए':  # Logic for 'ए' : 1 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 2))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ओ':  # Logic for 'ओ' : 1 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 2))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"

            elif (tokensList[iterationVariable][LengthOfTokensAtIndex - 2] == 'ं') and (
                    tokensList[iterationVariable][LengthOfTokensAtIndex - 3] == 'ा') and (
                    tokensList[iterationVariable][
                        LengthOfTokensAtIndex - 4] == 'न'):  # Logic for 'नां' : 3 space movement
                tokensList[iterationVariable] = ''.join(
                    tokensList[iterationVariable][iAnother] for iAnother in range(0, LengthOfTokensAtIndex - 4))
                tokensList[iterationVariable] = tokensList[iterationVariable] + "\n"
fof.close()

with open('data/FinalOutputFile.txt', "w", encoding='utf-8') as fow:
    for iteration in tokensList:
        fow.write(iteration)
fow.close()


def removeDuplicatesFromOutput():  # defining function for remove duplicate words from FinalOutputFile.txt
    OpeningFinalOutputFile = open('data/FinalOutputFile.txt', "r", encoding='utf-8')  # opening file in reading mode
    ExistingDataInFinalOutputFile = OpeningFinalOutputFile.readlines()  # reading content of file
    OpeningFinalOutputFile.close()  # closing object

    NewDataForFinalOutputFile = list(OrderedDict.fromkeys(ExistingDataInFinalOutputFile))  # using OrderedDict class
    # from collections package to remove duplicate words
    OpeningFinalOutputFile = open('data/FinalOutputFile.txt', "w", encoding="utf-8")  # opening file in writing mode
    for iterationVariable2 in NewDataForFinalOutputFile:  # writing new data into FinalOutputFile.txt
        OpeningFinalOutputFile.write(iterationVariable2)

    OpeningFinalOutputFile.close()  # closing object


removeDuplicatesFromOutput()  # calling function to remove duplicate words
