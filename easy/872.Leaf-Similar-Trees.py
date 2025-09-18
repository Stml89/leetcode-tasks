"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
        3
      /  \
     5    1
    /\   /\
   6  2 9  8
     /\
    7  4

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
       3                 3
      / \               / \
     5   1             5   1
    /\   /\           /\   /\
   6  2 9  8         6  7 4  2
     /\                     /\
    7  4                   9  8

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
     1       1
    /\      /\
   2  3    3  2
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_r1 = []
        leaf_r2 = []

        def inner(node, leafs):
            if not node.left and not node.right:
                leafs.append(node.val)
                return

            inner(node.left, leafs)
            inner(node.right, leafs)

        inner(root1, leaf_r1)
        inner(root2, leaf_r2)

        return leaf_r1 == leaf_r2


s = Solution()
root1 = TreeNode(val=3)
root1.left = TreeNode(val=5)
root1.right = TreeNode(val=1)
root1.left.left = TreeNode(val=6)
root1.left.right = TreeNode(val=2)
root1.left.right.left = TreeNode(val=7)
root1.left.right.right = TreeNode(val=4)
root1.right.left = TreeNode(val=9)
root1.right.right = TreeNode(val=8)

root2 = TreeNode(val=3)
root2.left = TreeNode(val=5)
root2.right = TreeNode(val=1)
root2.left.left = TreeNode(val=6)
root2.left.right = TreeNode(val=7)
root2.right.left = TreeNode(val=4)
root2.right.right = TreeNode(val=2)
root2.right.right.left = TreeNode(val=9)
root2.right.right.right = TreeNode(val=8)

assert s.leafSimilar(root1, root2)

root3 = TreeNode(val=1)
root3.left = TreeNode(val=2)
root3.right = TreeNode(val=3)

root4 = TreeNode(val=1)
root4.left = TreeNode(val=3)
root4.right = TreeNode(val=2)

assert not s.leafSimilar(root3, root4)
