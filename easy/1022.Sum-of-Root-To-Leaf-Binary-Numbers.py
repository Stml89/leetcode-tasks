"""
1022. Sum of Root To Leaf Binary Numbers

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a
binary number starting with the most significant bit.
- For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.
The test cases are generated so that the answer fits in a 32-bits integer.

Example 1:
        1
       / \
      0   1
     /\   /\
    0  1 0  1
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:
Input: root = [0]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.

Hint 1
Find each path, then transform that path to an integer in base 10.
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        s = ""

        def inner(node, s):
            if not node:
                return 0

            s += str(node.val)
            l = inner(node.left, s)
            r = inner(node.right, s)
            if not l and not r:
                return int(s, 2)
            return l + r

        return inner(root, s)


s = Solution()

root1 = TreeNode(val=1)
root1.left = TreeNode(val=0)
root1.right = TreeNode(val=1)
root1.left.left = TreeNode(val=0)
root1.left.right = TreeNode(val=1)
root1.right.left = TreeNode(val=0)
root1.right.right = TreeNode(val=1)
assert s.sumRootToLeaf(root1) == 22

root2 = TreeNode(val=0)
assert s.sumRootToLeaf(root2) == 0
