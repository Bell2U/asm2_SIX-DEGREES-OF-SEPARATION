from BloomFilter import BloomFilter
from Vertex import Vertex

"""
Graph Class
----------

This class represents the social network as a graph. 

The class supports the following functions:
    - bfs(Vertex, Vertex, BloomFilter): Perform a BFS from the start vertex to the end using the bloom filter.

Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
Good Luck!
"""


class Graph:
    def bfs(self, start: Vertex, end: Vertex, bloom_filter: BloomFilter) -> int:
        """
        Performs a BFS from the start vertex to the end using the bloom filter.
        Note you should use the bloom filter to avoid excessive memory usage with large graph inputs.
        The bloom filter is constructed from your filled in BloomFilter class.
        :param start: The start vertex.
        :param end: The end vertex.
        :param bloom_filter: The bloom filter used in the graph.
        :return: The degree of separation between the start and end vertices or -1 if they're not connected.
        """

        # TODO: Fill this in
