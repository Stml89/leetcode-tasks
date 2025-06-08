"""
559. Maximum Depth of N-ary Tree
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
            1
         /  |  \
        3   2   4
       / \
      5   6
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
                   1
        /      /       \         \
       2       3        4          5
              / \        \        / \
             6   7       8       9  10
                  \       \      /
                  11      12    13
                    \
                     14
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

Constraints:
The total number of nodes is in the range [0, 104].
The depth of the n-ary tree is less than or equal to 1000.
"""
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # if not root:
        #     return 0
        #
        # if not root.children:
        #     return 1
        #
        # heighest = [self.maxDepth(child) for child in root.children]
        # return max(heighest) + 1
        if not root:
            return 0
        result = 0
        queue = [root]
        while queue:
            result += 1
            for _ in range(len(queue)):
                current_node = queue.pop(0)
                if current_node.children:
                    for child in current_node.children:
                        queue.append(child)
        return result


ch4 = Node(5)
ch5 = Node(6)
ch1 = Node(3, children=[ch5, ch4])
ch2 = Node(2)
ch3 = Node(4)
root = Node(1, children=[ch1, ch2, ch3])
s = Solution()
assert s.maxDepth(root) == 3
