"""
589. N-ary Tree Preorder Traversal
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)

Example 1:
            1
          / | \
        3   2   4
       / \
      5   6
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

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
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Constraints:
The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
"""
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stk, ans = [root], []
        while stk:
            node = stk.pop()
            ans.append(node.val)
            if node.children:
                for child in node.children[::-1]:
                    stk.append(child)
        return ans


ch4 = Node(6)
ch5 = Node(5)
ch1 = Node(3, children=[ch5, ch4])
ch2 = Node(2)
ch3 = Node(4)
root = Node(1, children=[ch1, ch2, ch3])
s = Solution()
assert s.preorder(root) == [1, 3, 5, 6, 2, 4]
