import sys
import numpy as np


def next(substr):
    '''
    位置 next_arr[0] 无用，从 1 开始至 m
    :param substr:
    :return:
    '''
    m = len(substr)
    next_arr = np.zeros(m + 1, dtype=int)
    next_arr[1] = -1
    next_arr[2] = 0

    for i in range(3, m + 1):
        j = next_arr[i - 1] + 1
        # 字串的前N个位置的子字串是否与从头开始的N个字串相同
        while substr[i - 2] != substr[j - 1] and j > 0:
            j = next_arr[j] + 1
        next_arr[i] = j

    return next_arr

def string_match(textA, patternB):
    n = len(textA)
    i = j = 1
    mapping_times = 0

    while i <= n:
        mapping_times += 1
        if patternB[j - 1] == textA[i - 1]:
            j += 1
            i += 1
        else:
            j = next_arr[j] + 1
            if j == 0:
                j = 1
                i += 1

    return mapping_times


if __name__ == '__main__':
    '''
    KMP string search:
    Given a text strA=a(1)a(2)...a(n) and a pattern strB=b(1)b(2)...b(m)
    find the first occurrence of strB in strA = find the smallest k
    such that for each i, 1<=i<=m, a(k+i)=b(i)

    Brute force: O(m*n)
    KMP Time Complexity: O(m+n)
    KMP Space Complexity: O(m)
    '''
    strA = 'xyxxyxyxyyxyxyxyyxyxyxx'
    strB = 'xyxyyxyxyxx'
    next_arr = next(strB)
    operation = string_match(strA, strB)
    sys.exit()
