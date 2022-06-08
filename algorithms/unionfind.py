from __future__ import annotations
from typing import List

def init_set(n: int) -> List[int]:
    """ Create a disjoint set

    Args:
        n (int): Number of elements

    Returns:
        List[int]: List of length n, set with -1 as their values
    """
    return [-1] * n


