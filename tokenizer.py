import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

file = open(r"gujaratiDataSet.txt","r+",encoding="utf-8")
str=file.read()

file1 = open(r"hindiDataSet.txt","r+",encoding="utf-8")
str2=file1.read()

print (sent_tokenize(str))
print (sent_tokenize(str2))

wordlist=word_tokenize(str)
wordlist2=word_tokenize(str2)

print("printing")
print(wordlist)
print(wordlist2)

#file1 = open(r"C:\Users\Hemit\Desktop\token\output.txt","w",encoding="utf-8")

with open(r"gujaratitokens.txt","w",encoding="utf-8") as file2:
    for words in wordlist:
        file2.write("%s\n" % words)

with open(r"hinditokens.txt","w",encoding="utf-8") as file3:
    for words2 in wordlist2:
        file3.write("%s\n" % words2)
            
file1.close
file2.close
file3.close
file.close
