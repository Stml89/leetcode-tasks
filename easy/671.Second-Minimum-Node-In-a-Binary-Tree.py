"""
671. Second Minimum Node In a Binary Tree
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree
has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its
two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead.

Example 1:
     2
    / \
   2   5
      / \
     5   7
Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
     2
    / \
   2   2
Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

Constraints:
The number of nodes in the tree is in the range [1, 25].
1 <= Node.val <= 231 - 1
root.val == min(root.left.val, root.right.val) for each internal node of the tree.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = set()

        def inner(node):
            if not node:
                return
            values.add(node.val)
            inner(node.left)
            inner(node.right)

        inner(root)
        if len(values) == 1:
            return -1
        return list(sorted(values))[1]


root1 = TreeNode(2)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(7)

root2 = TreeNode(2)
root2.left = TreeNode(2)
root2.right = TreeNode(2)

root3 = TreeNode(5)
root3.left = TreeNode(8)
root3.right = TreeNode(5)

s = Solution()

assert s.findSecondMinimumValue(root1) == 5
assert s.findSecondMinimumValue(root2) == -1
assert s.findSecondMinimumValue(root3) == 8
