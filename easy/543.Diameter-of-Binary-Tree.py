"""
543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
         1
      2    3
    4  5
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
         1
      2
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def inner(node):
            nonlocal max_d
            if not node:
                return 0

            l = inner(node.left)
            r = inner(node.right)
            max_d = max(max_d, l + r)
            return 1 + max(l, r)

        inner(root)
        return max_d


# Example 1:
right2 = TreeNode(val=5)
left2 = TreeNode(val=4)
right1 = TreeNode(val=3)
left1 = TreeNode(val=2, left=left2, right=right2)
root = TreeNode(val=1, left=left1, right=right1)

s = Solution()
assert s.diameterOfBinaryTree(root) == 3

# Example 2:
left1 = TreeNode(val=2)
root = TreeNode(val=1, left=left1)

s = Solution()
assert s.diameterOfBinaryTree(root) == 1
