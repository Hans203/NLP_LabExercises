import numpy as np
def levenshtein_distance(str1, str2):
    len1, len2 = len(str1),len(str2)
    mat = np.zeros((len1+1,len2+1), dtype = int)
    print(mat)
    for i in range(0, len1+1):
        mat[i][0] = i
    for j in range(0, len2+1):
        mat[0][j] = j
    for i in range(1, len1+1):
        for j in range(1, (len2+1)):
            if str1[i-1] == str2[j-1]:
                mat[i][j] = mat[i-1][j-1]
            else:
                mat[i][j] = 1+min(mat[i-1][j-1], mat[i][j-1], mat[i-1][j])
        print(mat)
            
    
    return mat[len1][len2]
str1 = "cat"
str2 = "chat"
distance = levenshtein_distance(str1.lower(), str2.lower())
print(f"The edit distance between '{str1}' and '{str2}' is {distance}")

user_inp1 = input("Enter String 1: ")
user_inp2 = input("Enter String 2: ")
print(f"\nThe edit distance between '{user_inp1}' and '{user_inp2}' is {levenshtein_distance(user_inp1, user_inp2)}\n")

def alignment(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    mat = np.zeros((len1+1, len2+1), dtype=int)
    for i in range(1, len1+1):
        mat[i][0] = mat[i-1][0]-2
    for j in range(1, len2+1):        
        mat[0][j] = mat[0][j-1]-2

    for i in range(1, len1+1):
        for j in range(1, (len2+1)):
            top_value = mat[i-1][j]-2
            left_value = mat[i][j-1]-2
            diag_value = mat[i-1][j-1]
            if seq1[i-1] == seq2[j-1]:
                diag_value += 1
            else:
                diag_value -= 1
            mat[i][j] = max(top_value, left_value, diag_value)
    res1 = ""
    res2 = ""
    match=1
    mismatch=-1
    gap=-2
    i, j = len1, len2
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            score_diag = match
        else:
            score_diag = mismatch

        if mat[i][j] == mat[i - 1][j - 1] + score_diag:
            res1 = seq1[i - 1] + res1
            res2 = seq2[j - 1] + res2
            i -= 1
            j -= 1
        elif mat[i][j] == mat[i - 1][j] + gap:
            res1 = seq1[i - 1] + res1
            res2 = "-" + res2
            i -= 1
        else:
            res1 = "-" + res1
            res2 = seq2[j - 1] + res2
            j -= 1

    # Finish remaining
    while i > 0:
        res1 = seq1[i - 1] + res1
        res2 = "-" + res2
        i -= 1

    while j > 0:
        res1 = "-" + res1
        res2 = seq2[j - 1] + res2
        j -= 1

    return res1, res2
seq1 = "AGGCTATCACCTGACCTCCAGGCCGATGCCC"
seq2 = "TAGCTATCACGACCGCGGTCGATTTGCCCGAC"

result1, result2 = alignment(seq1, seq2)
print(f"The Sequence alignment for {seq1} and {seq2} are:\n {result1}, {result2}")
user_inp3 = input("Enter String 1: ")
user_inp4 = input("Enter String 2: ")
print(f"\nThe edit distance between '{user_inp3}' and '{user_inp4}' is {alignment(user_inp3, user_inp4)}\n")
