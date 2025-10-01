"""
897. Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is
now the root of the tree, and every node has no left child and only one right child.

Example 1:
                     5      1
                    /\       \
                   3  6       2
                  /\   \       \
                 2 4    8       3
                /      /\       ..
               1      7 9        \
                                  9
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
    5    1
   /\    \
  1  7    5
           \
           7
Input: root = [5,1,7]
Output: [1,null,5,null,7]

Constraints:
The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        new_root = TreeNode(arr[0])
        temp = new_root
        for i in range(1, len(arr)):
            temp.right = TreeNode(arr[i])
            temp = temp.right

        return new_root


root = TreeNode(val=5)
root.left = TreeNode(val=3)
root.left.left = TreeNode(val=2)
root.left.left.left = TreeNode(val=1)
root.left.right = TreeNode(val=4)

root.right = TreeNode(val=6)
root.right.right = TreeNode(val=8)
root.right.right.left = TreeNode(val=7)
root.right.right.right = TreeNode(val=9)

root1 = TreeNode(val=5)
root1.left = TreeNode(val=1)
root1.right = TreeNode(val=7)

s = Solution()
s.increasingBST(root)
s.increasingBST(root1)
