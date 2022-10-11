import re
from typing import Callable, List

"""
BloomFilter Class
----------

This class represents the bloom filter to be used in the graph. 

Each BloomFilter consists of the following properties:
    - hash_functions: A list of hash functions used in the bloom filter. Each function hashes a string to a number in the range of [0, bits*elements).
    - bits: The number of bits per element in the bloom filter.
    - elements: The number of elements in the bloom filter (capacity).
    - filter: The bit array representing the bloom filter.

The class also supports the following functions:
    - add(str): Adds a new entry to the bloom filter.
    - get(str): Returns a boolean that probabilistically indicates whether the given string is in the bloom filter.

Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
Good Luck!
"""


class BloomFilter:
    # These are the defined properties as described above
    hash_functions: List[Callable[[str], int]]
    bits: int
    elements: int
    filter: List[bool]

    def __init__(self, hash_functions: List[Callable[[str], int]], bits: int, elements: int) -> None:
        """
        The constructor for the BloomFilter class.
        :param hash_functions: A list of hash functions used in the bloom filter. Each function hashes a string to a number in the range of [0, BITS).
        :param bits: The number of bits in the bloom filter.
        :param elements: The number of elements in the bloom filter (capacity).
        """

        # TODO: Fill this in
        self.hash_functions = hash_functions
        self.bits = bits
        self.elements = elements
        self.filter = [False]*(self.bits*self.elements)
        self.currnt_elements = 0
        

    def add(self, item: str) -> None:
        """
        Adds a new entry to the bloom filter.
        :param item: The string to be added to the bloom filter.
        """

        # TODO: Fill this in
        # check if the bloom filter reaches to its maximum capasity
        if self.currnt_elements > self.elements:
            return

        # Hash the string and get all the results
        hash_results = [self.hash_functions[i](item) for i in range(0, len(self.hash_functions))]

        # flip the bit on the index indicated by hash result
        for filter_idx in hash_results:
            self.filter[filter_idx] = True
        
        # current_elements increment 
        self.currnt_elements += 1


    def get(self, item: str) -> bool:
        """
        Given a string, returns a boolean that probabilistically indicates whether the given string is in the bloom filter.
        :param item: The string to be checked in the bloom filter.
        :return: A boolean that indicates whether the string has been seen before.
        """

        # TODO: Fill this in
        # hash the string with all the hash functions
        hash_results = [self.hash_functions[i](item) for i in range(0, len(self.hash_functions))]

        # check if the corresponding bits are all one
        for filter_idx in hash_results:
            if self.filter[filter_idx] is False:
                return False
        return True
