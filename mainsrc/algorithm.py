#!/usr/bin/env python
# coding: utf-8

# # Aim
# Find and Sort the hamming_distance of the given word in the file

# In[1]:


matra_guj = ['ા', 'િ', 'ી', 'ુ', 'ૂ', 'ે', 'ૈ', 'ો', 'ૌ', 'ૅ', 'ૉ', 'ં', 'ૃ', '્', 'ઃ', 'ઁ', '઼', 'ઽ', 'ૄ']
matra_hin = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ॅ', 'ॉ', 'ं', 'ृ', '्', 'ः', 'ँ', '़', 'ऽ', 'ॄ']

gu_vow = ['અ', 'આ', 'ઇ', 'ઈ', 'ઉ', 'ઊ', 'ઋ', 'ૠ', 'ઍ', 'એ', 'ઐ', 'ઑ', 'ઓ', 'ઔ', 'ૐ']
hi_vow = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऍ', 'ए', 'ऐ', 'ऑ', 'ओ', 'औ', 'ॐ']

gu_cons = ['ક', 'ખ', 'ગ', 'ઘ', 'ઙ', 'ચ', 'છ', 'જ', 'ઝ', 'ઞ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ', 'ત', 'થ', 'દ', 'ધ', 'ન', 'પ', 'ફ',
           'બ', 'ભ', 'મ', 'ય', 'ર', 'લ', 'ળ', 'વ', 'શ', 'ષ', 'સ', 'હ']
hi_cons = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ',
           'ब', 'भ', 'म', 'य', 'र', 'ल', 'ळ', 'व', 'श', 'ष', 'स', 'ह']


# ## Create own length finding function
# When we use the library function len(word) we get the total length (અક્ષર + માત્રા), but we want the number of characters (અક્ષર) only.
# Note: Gujarati word is stored like this example given below
# 
# કાગડો: ['ક', 'ા', 'ગ', 'ડ', 'ો']
# len('કાગડો') = 5 (અક્ષર + માત્રા)
# my_len('કાગડો') = 3 (અક્ષર) [it will only consider the consonents]

# In[86]:


# આ ફંકશન માત્રાઓને ingnore કરશે.
# ઉ.દા. len(શાબાસ) == 3 not 5
def my_len(s):
    count = 0
    for i in s:
        if i not in matra_guj and i not in matra_hin:
            count += 1
    return count


# test
# print("my_len: " + str(my_len('શાબાસ')) + "  len: " + str(len('શાબાસ')))
# print("my_len: " + str(my_len('सोमवार')) + "  len: " + str(len('सोमवार')))


# ### Translitaration of Hindi to Gujarati
# we will translitarate the fonts of hindi to gujarati first and the compute the hamming distance of the two strings

# In[87]:


# this function will transliterate the hindi character to gujarati character
# why we need to Transliterate? : beacuse the hindi character is not comparable to the gujarati character ('હ' and 'ह' are not the same due to its different unicode values)
def translitarrate_hin_guj(s):
    output = []  # this will store the output
    for i in s:
        if i in matra_hin:
            output.append(matra_guj[matra_hin.index(i)])
        elif i in hi_cons:
            output.append(gu_cons[hi_cons.index(i)])
        else:
            output.append(i)
    return ''.join(output)


# testing
# print(translitarrate_hin_guj('सोमवारमां'))
# print(my_len('सोमवारमां'))

# issue: words do not append properly
# [ો, null, ા, null]


# ## Root consonant and vowel list
# <b>Using this function we are deriving the consonants of the word
# 
# Ex. root_cons_lst('કોયલ') will return ['ક', 'ય', 'લ']
# 
# <b> This function will return the list of the matras that apper in the word
# 
# print(root_vov_lst('શ્રોતા')) #will return ['્', 'ો', 'ા']
# print(root_vov_lst('કોયલ')) #will return ['ો', ' ', ' ']

# In[88]:


# Using this function we are deriving the consonants of the word
# Ex. root_cons_lst('કોયલ') will return ['ક', 'ય', 'લ']
def root_cons_lst(s):
    lst = []
    for i in s:
        if i not in matra_guj and i not in matra_hin:
            lst.append(i)
    return lst


# print(root_vov_lst(‘શ્રોતા’)) #will return [‘્’, ‘ો’, ‘ા’]
# print(root_vov_lst(‘કોયલ’)) #will return [‘ો’, ’ ’, ’ ’]
def root_matra_lst(guj):
    lst = []
    for i in guj:
        if i in matra_guj or i in matra_hin:
            lst.append(i)
            # Find a better way to do it
            # The idea is if we have the matra then remove the previous white space occurred due to character
            lst.remove(lst[lst.index(i) - 1])
        else:
            lst.append(' ')
    return lst


# print('શ્રોતા ->> ',root_matra_lst('શ્રોતા'))
# print('કોયલ ->> ',root_matra_lst('કોયલ'))


# # Find hamming distance between two strings
# 
# ### New type of hamming distance
# in this approach we will define the difference of માત્રા as 0.5 and difference of full letter as 1 (This idea is currently in development stage)
# ex. hamming_distance("अवसर", "अकसर"))

# In[89]:


# will count the hamming distance of the skeleton of the matras
def hamming_distance_vow(guj, hin_as_guj):
    hamming = [False, 0]
    guj_vov_lst = root_matra_lst(guj)
    hin_vov_lst = root_matra_lst(hin_as_guj)
    # checking first matra of the skeleton in the 0th index of the list
    if (guj_vov_lst[0] == hin_vov_lst[0]):
        hamming[0] = True
    for i, j in zip(guj_vov_lst, hin_vov_lst):
        # TODO: ignore last matra in count of hamming dist
        # if the last character of the matra is different then ignore it
        # why? --> સસલું, સસલા, સસલો, સસલી વગેરેનો અર્થ સમાન જ છે, ફક્ત એકવચન - બહુવચન અને સ્ત્રીલિંગ - પુંલિંગમાં ફરક છે.
        if i == len(guj_vov_lst) or j == len(hin_vov_lst):
            break
        if i != j:
            hamming[1] += 0.5
    return hamming


# will count hamming distance of the character
def hamming_distance_cons(guj, hin):
    count = [False, 0]
    s1_cons = root_cons_lst(guj)
    s2_cons = root_cons_lst(hin)
    if s1_cons[0] == s2_cons[0]:
        count[0] = True
    for i, j in zip(s1_cons, s2_cons):
        if i != j:
            count[1] += 1
    return count


# will count the ultimate hamming distance of the matras and the characters
def hamming_distance(guj, hin):
    # transliterate the string of hindi into gujarati
    hin_as_guj = translitarrate_hin_guj(hin)
    # TODO: find the counter example of this logic: if the character length of the word is not same then no need to find the hamming dist
    if my_len(guj) != my_len(hin):
        # print("Not same length : " + str((guj)) + " " + str((hin)))
        return [-1]
    else:
        consonants_count = hamming_distance_cons(guj, hin_as_guj)
        # print(consonants_count)
        vowels_count = hamming_distance_vow(guj, hin_as_guj)
        # print(vowels_count)
        return [float(vowels_count[1] + consonants_count[1]), vowels_count, consonants_count]


# test_list
# word1 = "વાઘ"
# word2 = "बाघ"
# print("hamming_distance: " + str(hamming_distance(word1, word2)) + "  " + str(word1) + " " + str(word2))


# # Find the hamming distance of a word from tokenized list

# In[91]:


# guj_token = "FinalOutputFileGujarati.txt"
# hin_token = "FinalOutputFileHindi.txt"
import os

script_path = os.path.abspath('')  # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
script_dir2 = os.path.split(script_dir)[0]
print(script_dir)

my_guj_token = script_dir + "\data\myListGuj.txt"
my_hin_token = script_dir + "\data\myListHindi.txt"
guj_file = open(my_guj_token, "r", encoding="utf-8")
hin_file = open(my_hin_token, "r", encoding="utf-8")

# rstrip() to remove '\n'
guj_content = [line.rstrip() for line in guj_file.readlines()]  # reading content from selected file
# print(guj_content)

hin_content = [line.rstrip() for line in hin_file.readlines()]


# print(hin_content)

def optimal_list(guj, level):
    # for guj_words in guj_content:
    guj_words = guj
    # {hamming_dist: {first_letter, first_matra, char_dist, vov_dist}}
    my_dict = {}
    out_list = list()
    for hin_words in hin_content:
        tempContainer = list()
        hin = translitarrate_hin_guj(hin_words)
        dist = hamming_distance(guj_words, hin_words)

        # [actual_dist ,first_matra, matra_dist], [first_char, char_dist]
        # [0.5, [True, 0.5], [True, 0]]
        if (0 < dist[0] <= level):
            # print("hamming_distance: " + str(dist) + "  " + str(guj_words) + " " + str(hin_words))
            out_list.append(hin_words)

    return out_list
    # hamming_distance("કૂતરો", "कुत्ता")

    # # Making Priority List based on nearest hamming distance

    # In[ ]:


if __name__ == '__main__':
    print(optimal_list('વાઘ', 1.5))
