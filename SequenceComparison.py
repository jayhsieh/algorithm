import numpy as np
import sys


def check_replace(a, b):
    return 0 if str(a) == str(b) else 1


def minimux_diff(mapfrom, mapto):
    x = (len(mapfrom) + 1)
    y = (len(mapto) + 1)
    matrix = np.zeros((x ,y), dtype=int)

    for i in range(x):
        matrix[i, 0] = i

    for j in range(y):
        matrix[0, j] = j

    for i in range(1, x):
        for j in range(1, y):
            insert = matrix[i - 1, j] + 1
            delete = matrix[i, j - 1] + 1
            replace = matrix[i - 1, j - 1] + check_replace(mapfrom[i - 1], mapto[j - 1])
            matrix[i, j] = min(insert, delete, replace)

    return matrix[x - 1, y - 1]


if __name__ == '__main__':
    '''
    Sequence Comparison: how to measure the dissimilarity between strA and strB
    How to change strA to strB by character by character using three types of edit operation
    1. insert a character 
    2. delete a character 
    3. replace one character with a different character
    such that the number of edit steps is minimum
    '''
    strA = 'abbc'
    strB = 'babb'
    operation = minimux_diff(strA, strB)
    sys.exit()
