"""
222. Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in
a complete binary tree, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:
           1
         /  \
        2    3
      /  \  /
     4   5 6
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Time complexity: O(n)
    # Space complexity: O(n)
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depthLeft(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def depthRight(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d

        ld = depthLeft(root.left)
        rd = depthRight(root.right)

        if ld == rd:
            return 2 ** (ld + 1) - 1
        else:
            a = self.countNodes(root.left)
            b = self.countNodes(root.right)
            return 1 + a + b


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root1 = TreeNode(1)

s = Solution()

assert s.countNodes(root) == 6
assert s.countNodes(None) == 0
assert s.countNodes(root1) == 1
