from __future__ import annotations
from typing import List

def z_algorithm(text:str) -> List[int]:
    """ Z algorithm to computre the z-values of each character for a given text.
    
    Z-values represent the length of the longest matching substring starting at the character index i, to the texts' prefix. For example:

    Args:
        text (str): Text to compute the z-values

    Returns:
        List[int]: Z-values for the given string
    """
    n = len(text)
    z_values = [0]
    # Base case length = 1
    if n == 1:
        return z_values
    
    # Base case - compute Z2
    k = 1
    z_val = 0
    while text[k] == text[k-1]:
        z_val += 1
        k += 1
    if z_val > 0:
        r = z_val + 1
        l = 2
    else:
        r = 0
        l = 0
    z_values.append(z_val)


    for k in range(1, n):
        if k > r:
            # Explicit character comparison
            q = k
            z_val = 0
            while text[q] == text[q - k]:
                z_val += 1
                q += 1
            if z_val > 0:
                r = q - 1
                l = k
            else:
                z_val = 0
            z_values.append(z_val)
        else: # k <= r
            z_kl = z_values[k - l + 1]
            if z_kl < r - k + 1:
                z_val = z_kl
                z_values.append(z_val)
            else:
                q = r + 1
                j = r - k + 2
                while text[]