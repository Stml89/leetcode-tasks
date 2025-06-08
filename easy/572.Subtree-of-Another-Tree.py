"""
572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
 and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
root ==    3     subRoot ==      4
           /\                    /\
          4  5                  1  2
         /\
        1  2
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
root ==    3     subRoot ==      4
           /\                    /\
          4  5                  1  2
         /\
        1  2
          /
         0
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        l_root = ""
        l_sub_tree = ""

        def inner(node):
            if not node:
                return
            return f"|{node.val}" + f"{inner(node.left)}" + f"{inner(node.right)}"

        l_root += inner(root)
        l_sub_tree += inner(subRoot)
        print(l_root)
        print(l_sub_tree)

        if l_sub_tree in l_root:
            return True
        return False
    #     if not root:
    #         return False
    #     if self.is_same_tree(root, subRoot):
    #         return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    #
    # def is_same_tree(self, r: TreeNode, s: TreeNode) -> bool:
    #     if r and s:
    #         return r.val == s.val and self.is_same_tree(r.left, s.left) and self.is_same_tree(r.right, s.right)
    #     return r is s
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     root_serial = self.serialize(root)
    #     print(root_serial)
    #     subRoot_serial = self.serialize(subRoot)
    #     print(subRoot_serial)
    #
    #     return subRoot_serial in root_serial
    # def serialize(self, node):
    #     if not node:
    #         return "#"
    #
    #     return f"|{node.val}" + "," + self.serialize(node.left) + "," + self.serialize(node.right)


ch_node31 = TreeNode(1)
ch_node32 = TreeNode(2)
ch_node21 = TreeNode(4, left=ch_node31, right=ch_node32)
ch_node22 = TreeNode(5)
root_node = TreeNode(3, left=ch_node21, right=ch_node22)

ch_node311 = TreeNode(1)
ch_node322 = TreeNode(2)
subroot = TreeNode(4, left=ch_node311, right=ch_node322)
s = Solution()
assert s.isSubtree(root_node, subroot)

ch_node41 = TreeNode(0)
ch_node31 = TreeNode(1)
ch_node32 = TreeNode(2, left=ch_node41)
ch_node21 = TreeNode(4, left=ch_node31, right=ch_node32)
ch_node22 = TreeNode(5)
root_node = TreeNode(3, left=ch_node21, right=ch_node22)

ch_node311 = TreeNode(1)
ch_node322 = TreeNode(2)
subroot = TreeNode(4, left=ch_node311, right=ch_node322)
s = Solution()
assert not s.isSubtree(root_node, subroot)

root_node = TreeNode(12)
subroot = TreeNode(2)
s = Solution()
assert not s.isSubtree(root_node, subroot)

root_node = TreeNode(1)
subroot = TreeNode(1)
s = Solution()
assert s.isSubtree(root_node, subroot)
