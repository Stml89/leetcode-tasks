"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.

Example 1:
         4
        / \
       2   6
      /\
     1  3
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
          1
         / \
        0  48
           / \
         12   49

Input: root = [1,0,48,null,null,12,49]
Output: 1

Example 3:
          236
          / \
      140    701
             / \
          227   911

Input: root = [236,104,701,null,227,null,911]
Output: 9
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def inner(node):
            if not node:
                return

            values.append(node.val)
            inner(node.left)
            inner(node.right)

        inner(root)

        values.sort()
        mindiff = float('inf')
        for i in range(len(values) - 1):
            mindiff = min(mindiff, abs(values[i] - values[i + 1]))

        return mindiff


# Example 1:
right2 = TreeNode(val=3)
left2 = TreeNode(val=1)
right1 = TreeNode(val=6)
left1 = TreeNode(val=2, left=left2, right=right2)
root = TreeNode(val=4, left=left1, right=right1)

s = Solution()
assert s.getMinimumDifference(root) == 1
