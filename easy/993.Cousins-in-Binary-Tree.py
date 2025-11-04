"""
993. Cousins in Binary Tree

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return
true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:
        1
       / \
      2   3
     /
    4
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
        1
       / \
      2   3
      \     \
       4     5
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
        1
       / \
      2   3
       \
        4
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:
The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = deque([(root, None)])

        while stack:
            parent_x = None
            parent_y = None
            for _ in range(len(stack)):
                node, parent = stack.popleft()
                if node.val == x:
                    parent_x = parent
                if node.val == y:
                    parent_y = parent
                if node.left:
                    stack.append((node.left, node))
                if node.right:
                    stack.append((node.right, node))
            if parent_x and parent_y:
                if parent_x != parent_y:
                    return True
        return False

    # Time complexity: O(n)
    # Space complexity: O(n)
    def isCousins1(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent = {}
        depth = {}

        def dfs(node, par, d):
            if not node:
                return
            parent[node.val] = par
            depth[node.val] = d
            dfs(node.left, node, d + 1)
            dfs(node.right, node, d + 1)

        dfs(root, None, 0)
        return parent[x] != parent[y] and depth[x] == depth[y]


s = Solution()

root1 = TreeNode(val=1)
root1.left = TreeNode(val=2)
root1.right = TreeNode(val=3)
root1.left.left = TreeNode(val=4)
assert not s.isCousins(root1, x=4, y=3)

root2 = TreeNode(val=1)
root2.left = TreeNode(val=2)
root2.right = TreeNode(val=3)
root2.left.right = TreeNode(val=4)
root2.right.right = TreeNode(val=5)
assert s.isCousins(root2, x=5, y=4)

root3 = TreeNode(val=1)
root3.left = TreeNode(val=2)
root3.right = TreeNode(val=3)
root3.left.right = TreeNode(val=4)
assert not s.isCousins(root3, x=2, y=3)
