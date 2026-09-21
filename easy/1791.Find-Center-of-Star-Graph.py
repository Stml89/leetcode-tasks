"""
1791. Find Center of Star Graph

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there
is one center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the
nodes ui and vi. Return the center of the given star graph.

Example 1:
       4
       |
       2
     /  \
    1    3

Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

Constraints:
3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.

Hint 1
The center is the only node that has more than one edge.
Hint 2
The center is also connected to all other nodes.
Hint 3
Any two edges must have a common node, which is the center.
"""
from typing import List


# Time Complexity: O(1)
# Space Complexity O(1)
def findCenter(edges: List[List[int]]) -> int:
    a, b = edges[0]
    c, d = edges[1]

    if a == c or a == d:
        return a

    return b


# Time Complexity: O(1)
# Space Complexity O(1)
def findCenter1(edges: list[list[int]]) -> int:
    return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


assert findCenter([[1, 2], [2, 3], [4, 2]]) == 2
assert findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
