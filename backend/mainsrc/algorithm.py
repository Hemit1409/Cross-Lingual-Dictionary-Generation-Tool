import sys
import requests

matra_guj = ['ા', 'િ', 'ી', 'ુ', 'ૂ', 'ે', 'ૈ', 'ો', 'ૌ', 'ૅ', 'ૉ', 'ં', 'ૃ', '્', 'ઃ', 'ઁ', '઼', 'ઽ', 'ૄ']
matra_hin = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ॅ', 'ॉ', 'ं', 'ृ', '्', 'ः', 'ँ', '़', 'ऽ', 'ॄ']

gu_vow = ['અ', 'આ', 'ઇ', 'ઈ', 'ઉ', 'ઊ', 'ઋ', 'ૠ', 'ઍ', 'એ', 'ઐ', 'ઑ', 'ઓ', 'ઔ', 'ૐ']
hi_vow = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऍ', 'ए', 'ऐ', 'ऑ', 'ओ', 'औ', 'ॐ']

gu_cons = ['ક', 'ખ', 'ગ', 'ઘ', 'ઙ', 'ચ', 'છ', 'જ', 'ઝ', 'ઞ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ', 'ત', 'થ', 'દ', 'ધ', 'ન', 'પ', 'ફ',
           'બ', 'ભ', 'મ', 'ય', 'ર', 'લ', 'ળ', 'વ', 'શ', 'ષ', 'સ', 'હ']
hi_cons = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ',
           'ब', 'भ', 'म', 'य', 'र', 'ल', 'ळ', 'व', 'श', 'ष', 'स', 'ह']

def my_len(s):
    count = 0
    for i in s:
        if i not in matra_guj and i not in matra_hin:
            count += 1
    return count


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

def root_cons_lst(s):
    lst = []
    for i in s:
        if i not in matra_guj and i not in matra_hin:
            lst.append(i)
    return lst


def root_matra_lst(guj):
    lst = []
    for i in guj:
        if i in matra_guj or i in matra_hin:
            lst.append(i)
            lst.remove(lst[lst.index(i) - 1])
        else:
            lst.append(' ')
    return lst


def hamming_distance_vow(guj, hin_as_guj):
    hamming = [False, 0]
    guj_vov_lst = root_matra_lst(guj)
    hin_vov_lst = root_matra_lst(hin_as_guj)
    if (guj_vov_lst[0] == hin_vov_lst[0]):
        hamming[0] = True
    for i, j in zip(guj_vov_lst, hin_vov_lst):
        if i == len(guj_vov_lst) or j == len(hin_vov_lst):
            break
        if i != j:
            hamming[1] += 0.5
    return hamming


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


def hamming_distance(guj, hin):
    hin_as_guj = translitarrate_hin_guj(hin)
    if my_len(guj) != my_len(hin):
        return [-1]
    else:
        consonants_count = hamming_distance_cons(guj, hin_as_guj)
        vowels_count = hamming_distance_vow(guj, hin_as_guj)
        return [float(vowels_count[1] + consonants_count[1]), vowels_count, consonants_count]


import os

script_path = os.path.abspath('')  # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]  # i.e. /path/to/dir/
script_dir2 = os.path.split(script_dir)[0]
# print(script_dir)

# my_guj_token = script_dir + "\data\myListGuj.txt"
# my_hin_token = script_dir + "\data\myListHindi.txt"

my_guj_token = "E:\\Sem6\\gui3\\backend\data\myListGuj.txt"
my_hin_token = "E:\\Sem6\\gui3\\backend\data\myListHindi.txt"

guj_file = open(my_guj_token, "r", encoding="utf-8")
hin_file = open(my_hin_token, "r", encoding="utf-8")

guj_content = [line.rstrip() for line in guj_file.readlines()]  # reading content from selected file


hin_content = [line.rstrip() for line in hin_file.readlines()]


def optimal_dict_genrator(guj, level):
    # for guj_words in guj_content:
    guj_words = guj
    # {hamming_dist: {first_letter, first_matra, char_dist, vov_dist}}
    my_dict = {}
    out_list = list()
    for hin_word in hin_content:
        tempContainer = list()
        hin = translitarrate_hin_guj(hin_word)
        dist = hamming_distance(guj_words, hin_word)

        # print(dist)

        def comparator(dist_list):
            # when first matra is same
            if dist_list[1][0]:
                # when first char is same
                if dist_list[2][0]:
                    return 1
                # when first char is different
                else:
                    return 3
            # when first matra is not same
            else:
                # when first char is same
                if dist_list[2][0]:
                    return 2
                # when first char and matra are not same
                else:
                    return 4

        # [actual_dist ,[first_matra, matra_dist], [first_char, char_dist]]
        # [0.5, [True, 0.5], [True, 0]]
        if (0 < dist[0] <= level and dist[0] != -1):
            # print("hamming_distance: " + str(dist) + "  " + str(guj_words) + " " + str(hin_words))

            out_list.append(hin_word)
            if dist[0] in my_dict.keys():
                res = comparator(dist)
                if res in my_dict[dist[0]]:
                    my_dict[dist[0]][res].append(hin_word)
                else:
                    my_dict[dist[0]][res] = [hin_word]
            else:
                res = comparator(dist)
                my_dict[dist[0]] = {res: [hin_word]}

    return my_dict
    # hamming_distance("કૂતરો", "कुत्ता")
    
def optimal_list(guj, level):
    optimal_file_path =  'E:\\Sem6\\gui3\\backend\data\opList.txt'
    out_file = open(optimal_file_path, "w", encoding="utf-8")
    optimal_dict = optimal_dict_genrator(guj, level)
    # print(optimal_dict)
    out_list = list()
    for key in sorted(optimal_dict.keys()):
        # print(key)
        for key2 in sorted(optimal_dict[key].keys()):
            # print(key2)
            # print(optimal_dict[key][key2])
            for i in optimal_dict[key][key2]:
                out_file.write(i + "\n")
                out_list.append(i)
    return out_list

if __name__ == '__main__':
    # optimal_list('વાઘ', 1.5)
    ip_list = "E:\\Sem6\\gui3\\backend\data\ipWord.txt"
    infile = open(ip_list, "r", encoding="utf-8")
    my_list = []
    for i in infile:
        my_list.append(i)

    print(optimal_list(my_list[0].rstrip() ,float(my_list[1])))
    # print(my_list[0].rstrip() ,my_list[1])