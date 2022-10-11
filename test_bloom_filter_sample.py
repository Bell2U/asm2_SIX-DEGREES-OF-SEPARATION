from unittest import TestCase

from BloomFilter import BloomFilter

BITS = 4
ELEMENTS = 4

"""
This is a sample test suite for you to write your own test.
Note that the provided hash functions are NOT good hash function but
are used for demonstration purposes only. You should write your own
hash functions and test cases to test your implementation.

No tests are provided or will be provided for the bfs function.
You are free (and encouraged!) to use this as a base to write your own tests.
"""


# These are BAD hash function and are used for demonstration only.
# It just takes the first letter of a string and returns its ASCII value in the range [0, BITS * ELEMENTS).
# This means that it will always return the same value for a given string
# or any string that starts with the same letter.
def bad_hash_function_1(name: str) -> int:
    return ord(name[0]) % (BITS * ELEMENTS)


def bad_hash_function_2(name: str) -> int:
    return (ord(name[0]) + 8) % (BITS * ELEMENTS)


class TestBloomFilterSample(TestCase):
    def setUp(self) -> None:
        self.bf = BloomFilter([bad_hash_function_1, bad_hash_function_2], bits=16, elements=1)

    def test_bloom_filter_sample(self):
        self.bf.add("a")  # This should set the 1st and 9th index to True
        self.assertEqual(self.bf.get("a"), True, "Bloom Filter returns incorrect result")

        self.bf.add("z")  # This should set the 10th and 2nd index to True
        self.assertEqual(self.bf.get("z"), True, "Bloom Filter returns incorrect result")

        # This should return True because the 2nd and 10th index are set to True even though the key 'b' has not been added
        # This is what makes a Bloom Filter a probabilistic data structure
        self.assertEqual(self.bf.get("b"), True, "Bloom Filter returns incorrect result")