from typing import List

"""
Vertex Class
----------

This class represents an individual user in the social network. 

Each Vertex consists of the following properties:
    - username: The username for the current User. Guaranteed to be unique.
    - followers: A list of followers connected to this Vertex (adjlist)

The class also supports the following functions:
    - add_follower(Vertex): Adds a follower to the current user. 
    - get_followers(): Returns a list of all the followers connected to the Vertex.
    - get_username(): Returns the username of the User.

**You do not need to edit this class**

"""


class Vertex:
    # These are the defined properties as described above
    username: str
    followers: "List[Vertex]"

    def __init__(self, username: str) -> None:
        """
        The constructor for the Vertex class.
        :param username: The username of the user.
        """
        self.username = username
        self.followers = []

    def add_follower(self, vertex: "Vertex") -> None:
        """
        Adds a follower to the given user with the given distance.
        :param vertex: The vertex to add an edge to.
        """

        # vertex is None, self-loop or already in the adjlist
        if not vertex or vertex == self or vertex in self.followers:
            return

        # Add to adjlist
        self.followers.append(vertex)

    def get_followers(self) -> "List[Vertex]":
        """
        Returns the list of followers for the user.
        :return: The list of followers for the user.
        """

        return self.followers

    def get_username(self) -> str:
        """
        Returns the username of the user.
        :return: The username of the user.
        """

        return self.username
