"""
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
          3
         / \
        9  20
            /  \
           15   7
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def _node(node, is_left=False):
            if not node:
                return 0

            if is_left and not node.left and not node.right:
                return node.val
            return _node(node.left, True) + _node(node.right, False)

        return _node(root)


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
assert s.sumOfLeftLeaves(root) == 24

root1 = TreeNode(1)
assert s.sumOfLeftLeaves(root1) == 0
