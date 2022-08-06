import numpy as np
from Z_Algorithm import processZPrefix

def kmp(pat, txt):
    patLen = len(pat)
    z = processZPrefix(pat)

    sp = np.zeros(patLen)

    # calcumatlate SP values
    # basically finds the leftmost prefix match
    for j in range(patLen-1, 0, -1):
        i = j + z[j]
        sp[i] = z[j]

    #TODO: search algorithm
    '''
    basically match from left to right scanning left to right
    at mismatch, use SP to move pattern to right by SP value as it's 
    identified the longest match from pervious match to prefix of pattern
    '''