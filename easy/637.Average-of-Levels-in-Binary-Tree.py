"""
637. Average of Levels in Binary Tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10-5 of the actual answer will be accepted.

Example 1:
      3
     / \
    9  20
      / \
     15  7
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
      3
     / \
    9  20
   / \
  15  7
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        r = []

        def inner(node, level):
            if not node:
                return

            if len(r) <= level:
                r.append([])

            r[level].append(node.val)
            inner(node.left, level + 1)
            inner(node.right, level + 1)

        inner(root, 0)

        return [sum(i) / len(i) for i in r]


root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.left.left = TreeNode(15)
root2.left.right = TreeNode(7)

s = Solution()

assert s.averageOfLevels(root1) == [3.00000, 14.50000, 11.00000]
assert s.averageOfLevels(root2) == [3.00000, 14.50000, 11.00000]
