"""
938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all
nodes with a value in the inclusive range [low, high].

Example 1:
            10
            /\
           5  15
          /\   \
         3  7  18
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
             10
            /  \
           5    15
          /\   / \
         3  7 13 18
        /  /
       1  6
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.


Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inner(node):
            summary = 0
            if not node:
                return 0

            if low <= node.val <= high:
                summary = node.val

            if node.val > low:
                summary += inner(node.left)
            if node.val < high:
                summary += inner(node.right)

            return summary

        return inner(root)

    # Time complexity: O(n)
    # Space complexity: O(h)
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if not node:
                continue

            if low <= node.val <= high:
                result += node.val
                stack.append(node.right)
                stack.append(node.left)
            elif node.val < low:
                stack.append(node.right)
            else:
                stack.append(node.left)

        return result


s = Solution()
root1 = TreeNode(val=10)
root1.left = TreeNode(val=5)
root1.right = TreeNode(val=15)
root1.left.left = TreeNode(val=3)
root1.left.right = TreeNode(val=7)
root1.right.right = TreeNode(val=18)
assert s.rangeSumBST(root1, low=7, high=15) == 32

s = Solution()
root2 = TreeNode(val=10)
root2.left = TreeNode(val=5)
root2.right = TreeNode(val=15)
root2.left.left = TreeNode(val=3)
root2.left.right = TreeNode(val=7)
root2.left.left.left = TreeNode(val=1)
root2.left.right.left = TreeNode(val=6)
root2.right.right = TreeNode(val=18)
root2.right.left = TreeNode(val=13)
assert s.rangeSumBST(root2, low=6, high=10) == 23
