"""
Author: Cameron Britten, John Requizo

Week 8: semi-Numerical Algorithms
"""


def mod_exp(a:int, b:int, n:int) -> int:
    """ Compute the Modular exponenetation of a^b mod n where b is very very large.

    Args:
        a (int): Base
        b (int): Exponent
        n (int): Modular

    Returns:
        int: Modular exponentation of a^b mod n
    """

    binary_rep = bin(b)[2:][::-1]

    # Key property of modular arithmetic:
    # x * y mod z = (x mod z * y mod z) mod z

    # Repeated squaring
    # Base case
    x = a**(2**0) % n
    result = 1
    for i in range(1, len(binary_rep)):
        x = (x * x) % n
        if binary_rep[i] == "1":
            result = result * x % n
        
    return result

    
if __name__ == "__main__":
    m = mod_exp(7, 560, 561)
    m = mod_exp(8, 1001, 562)
    print(m)