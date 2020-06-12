import numpy as np
import sys


def check_equate(a, b):
    return 1 if str(a) == str(b) else 0


def lcs(strA, strB):
    x = (len(strA) + 1)
    y = (len(strB) + 1)
    matrix = np.zeros((x ,y), dtype=int)

    for i in range(1, x):
        for j in range(1, y):
            goRight = matrix[i - 1, j]
            goDown = matrix[i, j - 1]
            goDiagonal = matrix[i - 1, j - 1] + check_equate(strA[i - 1], strB[j - 1])
            matrix[i, j] = max(goRight, goDown, goDiagonal)

    return matrix[x - 1, y - 1]


if __name__ == '__main__':
    '''
    Longest Common Subsequence (LCS): 
    string S is longest common subsequence of string A nad B if S is common subsequence of A and B of maximal length
    ex:
    The LCS of "algorithm" and "belowart" is "lort"
    '''
    strA = 'belowart'
    strB = 'algorithm'
    ans = lcs(strA, strB)
    sys.exit()
