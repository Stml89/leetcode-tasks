"""
617. Merge Two Binary Trees
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values
up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees.

Example 1:
        1         2              3
       / \       / \            / \
      3   2     1   3          4   5
     /           \   \        / \   \
    5             4   7      5   4   7
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
        1         1              2
                 /              /
                2              2

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:
The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        #
        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1
        # =========================================
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)


root_res1_right11 = TreeNode(val=4)
root_res1_left11 = TreeNode(val=5)
root_res1_right111 = TreeNode(val=7)
root_res1_right22 = TreeNode(val=5, right=root_res1_right111)
root_res1_left22 = TreeNode(val=4, right=root_res1_right11, left=root_res1_left11)
root_res1 = TreeNode(val=3, left=root_res1_left22, right=root_res1_right22)

root_node2_left11 = TreeNode(val=5)
root_node2_right1 = TreeNode(val=2)
root_node2_left1 = TreeNode(val=3, left=root_node2_left11)
root_node2 = TreeNode(val=1, left=root_node2_left1, right=root_node2_right1)

root_node1_right11 = TreeNode(val=7)
root_node1_right22 = TreeNode(val=4)
root_node1_right2 = TreeNode(val=3, right=root_node1_right11)
root_node1_left2 = TreeNode(val=1, right=root_node1_right22)
root_node1 = TreeNode(val=2, left=root_node1_left2, right=root_node1_right2)

s = Solution()
assert s.mergeTrees(root_node2, root_node1) == root_res1

root_node1 = TreeNode(val=1)
root_node2 = TreeNode(val=1)
root_node2.left = TreeNode(val=2)
s = Solution()
root_res = TreeNode(val=2)
root_res.left = TreeNode(val=2)
s.mergeTrees(root_node1, root_node2)
