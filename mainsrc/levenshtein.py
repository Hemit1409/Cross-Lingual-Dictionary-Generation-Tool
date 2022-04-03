import numpy

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
    print(output)        
    return ''.join(output)

def levenshteinDistanceDP2(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    printDistances(distances, len(token1), len(token2))
    print(token1)
    return distances[len(token1)][len(token2)]

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    printDistances(distances, len(token1), len(token2))
    return 0

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


# test_list

word1 = "શાબાસ"
word2 = "सोमवार"
hin_as_guj = translitarrate_hin_guj(word2)

# word1 = "શાબાસ"
# word2 = "सोमवार"

word1 = "Hemit"
word2 = "Henill"
hin_as_guj = translitarrate_hin_guj(word2)        

#levenshteinDistanceDP2("kelm", "hello")
levenshteinDistanceDP2(word1, word2)
