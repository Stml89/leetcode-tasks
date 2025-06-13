"""
501. Find Mode in Binary Search Tree
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inner(node, c):
            if not node:
                return

            inner(node.left, c)
            inner(node.right, c)
            c[node.val] += 1

        count_numbers = defaultdict(int)
        inner(root, count_numbers)
        max_count = max(count_numbers.values())
        res = [i for i in count_numbers if count_numbers[i] == max_count]
        return res


three2 = TreeNode(2, )
two1 = TreeNode(2, left=three2)
root1 = TreeNode(1, right=two1)

root2 = TreeNode(0)

two3 = TreeNode(2, )
root3 = TreeNode(1, right=two3)

left45 = TreeNode(0)
left44 = TreeNode(0, left=left45)
left43 = TreeNode(0, )
left4 = TreeNode(0, right=left43, left=left44)
right44 = TreeNode(1, )
left44 = TreeNode(1, )
right4 = TreeNode(1, right=right44, left=left44)
root4 = TreeNode(1, right=right4, left=left4)

s = Solution()
assert s.findMode(root1) == [2]
assert s.findMode(root2) == [0]
assert s.findMode(root3) == [2, 1]
assert s.findMode(root4) == [0, 1]
