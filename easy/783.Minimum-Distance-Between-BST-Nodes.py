"""
783. Minimum Distance Between BST Nodes

Given the root of a Binary Search Tree (BST), return the minimum difference between the values
of any two different nodes in the tree.

Example 1:
         4
        /\
       2  6
      /\
     1 3
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
         1
        /\
       0  48
          /\
        12  49
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105

Note: This question is the same as 530:
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""
from heapq import heappush, heappop
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        values = []

        def inner(node):
            if not node:
                return

            heappush(values, node.val)
            inner(node.left)
            inner(node.right)

        inner(root)
        last1 = heappop(values)
        last2 = heappop(values)
        return last2 - last1

    def minDiffInBST1(self, root: Optional[TreeNode]) -> int:
        values = []

        def inner(node):
            if not node:
                return

            values.append(node.val)
            inner(node.left)
            inner(node.right)

        inner(root)
        values.sort()
        return values[1] - values[0]


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(48)
root2.left.left = TreeNode(12)
root2.left.right = TreeNode(49)

root3 = TreeNode(27)
root3.right = TreeNode(34)
root3.right.right = TreeNode(58)
root3.right.right.left = TreeNode(50)
root3.right.right.left.left = TreeNode(44)

s = Solution()

assert s.minDiffInBST(root) == 1
assert s.minDiffInBST(root2) == 1
assert s.minDiffInBST(root3) == 6
