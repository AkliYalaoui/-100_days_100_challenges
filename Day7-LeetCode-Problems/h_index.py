from typing import List

def hIndex(citations: List[int]) -> int:
    """
    Given an array of integers citations where citations[i] is the number of citations a researcher
    received for their ith paper, return the researcher's h-index.

    According to the definition of h-index on Wikipedia: 
    The h-index is defined as the maximum value of h such that the given researcher has published at
    least h papers that have each been cited at least h times.
    """
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
    return h
