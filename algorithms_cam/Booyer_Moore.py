import numpy as np
from Z_Algorithm import processZPrefix

def booyerMoorePatMatch(pat, txt, asciiStartVal, asciiEndVal):
    '''
    time saving strats
    1. Bad Char
    2. Good Suffix
    '''
    patLen = len(pat)
    txtLen = len(txt)
    asciiRange = asciiEndVal - asciiStartVal
    startMatched = -1
    endMatched = -1

    # bad char preprocessing
    badCharPos = np.full((patLen+1, asciiRange), -1) # -1 means the character does not exist in this pattern
    for i in range(patLen):
        for j in range(asciiRange):
            badCharPos[i+1][j] = badCharPos[i][j]
        badCharPos[i+1][ord(pat[i])] = i # index of rightmost match
    
    # Z algorithm for suffix match length
    zSuffix = reversed(processZPrefix(reversed(pat)))

    # calculate good suffix
    # good suffix value at index is the index in pat of the start of the match to sufix
    # up to the good suffix index
    goodsuffix = np.zeros(patLen+1)

    for p in range(patLen+1):
        j = patLen - zSuffix(p) # use +1 when pattern index starts at 1
        goodsuffix[j] = p

    # booyer moore pattern search
    j = 0
    n = txtLen
    m = patLen
    while j <= txtLen - patLen:
        k = patLen-1 # right to left search

        while k >= 0:
            #TODO: add in start and end matched for k value changing here
            if pat[k] == txt[j+k]: # compare pat char to txt char
                k-= 1
            else:
                # get bad char and good suffix shift amounts
                #TODO: finish this implementation (probs easy hopefully)

    