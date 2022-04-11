import os
import numpy
script_path = os.path.abspath('') # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
script_dir2 = os.path.split(script_dir)[0]
print(script_dir)

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
        elif i in hi_vow:
            output.append(gu_vow[hi_vow.index(i)])
        else:
            output.append(i)
    return ''.join(output)

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
            
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                distances[t1][t2]=min(distances[t1][t2 - 1],distances[t1 - 1][t2],distances[t1 - 1][t2 - 1]) + 1

    printDistances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]



def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


# test_list

word1 = "અનુવાદ"
word2 = "अनुवाद"
hin_as_guj = translitarrate_hin_guj(word2)

print(levenshteinDistanceDP(word1, hin_as_guj))