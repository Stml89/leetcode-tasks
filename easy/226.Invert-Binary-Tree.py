"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
           4                4
         /  \             /  \
        2    7      ->   7    2
      /  \  / \        /  \  / \
     1   3 6   9      9   6 3   1
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

root_ans = TreeNode(4)
root_ans.left = TreeNode(7)
root_ans.right = TreeNode(2)
root_ans.left.left = TreeNode(9)
root_ans.left.right = TreeNode(6)
root_ans.right.left = TreeNode(3)
root_ans.right.right = TreeNode(1)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

root1_ans = TreeNode(2)
root1_ans.left = TreeNode(3)
root1_ans.right = TreeNode(1)

s = Solution()

assert s.invertTree(root) is root_ans
assert s.invertTree(root1) == root1_ans
assert s.invertTree(None) == []
