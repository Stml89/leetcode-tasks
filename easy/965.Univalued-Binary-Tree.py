"""
965. Univalued Binary Tree

A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:
        1
       / \
      1   1
     /\    \
    1  1    1
Input: root = [1,1,1,1,1,null,1]
Output: true

Example 2:
         2
        / \
       2   2
      /\
     5  2
Input: root = [2,2,2,5,2]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        values = []

        def inner(node):
            if not node:
                return

            inner(node.left)
            values.append(node.val)
            inner(node.right)

        inner(root)

        first_value = values[0]
        for i in range(1, len(values)):
            if values[i] != first_value:
                return False
        return True

    # Time complexity: O(n)
    # Space complexity: O(n)
    def isUnivalTree1(self, root: Optional[TreeNode]) -> bool:
        def is_unival(node, value):
            if not node:
                return True
            if node.val != value:
                return False
            return is_unival(node.left, value) and is_unival(node.right, value)

        return is_unival(root, root.val)

    # Time complexity: O(n)
    # Space complexity: O(n)
    def isUnivalTree2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if (root.left and root.val != root.left.val) or (root.right and root.right.val != root.val):
            return False
        return self.isUnivalTree2(root.left) and self.isUnivalTree2(root.right)


s = Solution()

root1 = TreeNode(val=1)
root1.left = TreeNode(val=1)
root1.left.left = TreeNode(val=1)
root1.left.right = TreeNode(val=1)
root1.right = TreeNode(val=1)
root1.right.right = TreeNode(val=1)
assert s.isUnivalTree(root1)

root2 = TreeNode(val=2)
root2.left = TreeNode(val=2)
root2.right = TreeNode(val=2)
root2.right.left = TreeNode(val=5)
root2.right.right = TreeNode(val=2)
assert not s.isUnivalTree(root2)
