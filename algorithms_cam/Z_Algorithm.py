import numpy as np

def processZPrefix(pat):
      '''
      input: pattern
      output: Z suffix array
      '''
      m = len(pat)
      z = np.zeros(m, dtype=int)
      l=0
      r=0
      for k in range(1, m):
          j = k+1
          if pat[k] == pat[0]:
              if k > r:
                  while(j < m):
                      if pat[j] == pat[j-k]: # check for match with prefix
                          j += 1
                      elif pat[j] != pat[j-k]:
                          break
                  z[k] = j-k # record Z value
                  r = j-1
                  l = k
              elif k <= r:
                  if z[k-l] < r-k: # if zbox at k inside z box l-r then get ealier value
                      z[k] = z[k-l]
                  elif z[k-l] >= r-k: # check if current box could extend past matched box
                      j = r
                      while(j < m):
                          if pat[j] == pat[j-k]: # check for match with prefix
                              j += 1
                          elif pat[j] != pat[j-k]:
                              break
                      z[k] = j-k # record Z value
                      r = j-1
                      l = k

      return z
