"""
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
            4
           /\
          2  7
         /\
        1  3
Output: [2,1,3]

Example 2:
            4
           /\
          2  7
         /\
        1  3
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(7)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)

s = Solution()

assert s.searchBST(root1, 2) is TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
assert s.searchBST(root2, 5) is None
