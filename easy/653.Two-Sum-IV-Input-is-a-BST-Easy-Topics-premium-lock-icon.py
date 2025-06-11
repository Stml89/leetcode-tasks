"""
653. Two Sum IV - Input is a BST
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such
that their sum is equal to k, or false otherwise.

Example 1:
        5
       /\
      3  6
     /\   \
    2  4   7
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
        5
       /\
      3  6
     /\   \
    2  4   7
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""
# TODO
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []

        def inner(node):
            if not node:
                return
            l.append(node.val)
            inner(node.left)
            inner(node.right)

        inner(root)
        curr = 0
        point = 1
        while curr != len(l) - 1:
            if (l[curr] + l[point]) == k:
                return True
            if point < len(l) - 1:
                point += 1
            else:
                curr += 1
                point = curr + 1
        return False


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

s = Solution()

assert s.findTarget(root, 9)
assert not s.findTarget(root, 28)
