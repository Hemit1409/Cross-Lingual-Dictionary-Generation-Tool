import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

with open(r"data/gujsentences.txt","r+",encoding="utf-8") as file:
  str = file.read()

file.close()

with open(r"data/hindisentences.txt","r+",encoding="utf-16") as file1:
  str2 = file1.read()

print (sent_tokenize(str))
print (sent_tokenize(str2))

wordlist=word_tokenize(str)
wordlist2=word_tokenize(str2)

print("printing")
print(wordlist)
print(wordlist2)


with open(r"data/gujaratitokens.txt","w",encoding="utf-8") as file2:
    for words in wordlist:
        file2.write("%s\n" % words)

with open(r"data/hinditokens.txt","w",encoding="utf-8") as file3:
    for words2 in wordlist2:
        file3.write("%s\n" % words2)
            
file1.close
file2.close
file3.close

