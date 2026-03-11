"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.
The cloned tree is a copy of the original tree.
Return a reference to the same node in the cloned tree.
Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Example 1:
            7                   7
           /\                  /\
          4  3                4  3
            /\                   /\
           6  19                6  19

Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

Example 2:
Input: tree = [7], target =  7
Output: 7

Example 3:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

Constraints:
The number of nodes in the tree is in the range [1, 104].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.

Follow up: Could you solve the problem if repeated values on the tree are allowed?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h)
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None

        if original == target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left

        return self.getTargetCopy(original.right, cloned.right, target)

    # Time complexity: O(n)
    # Space complexity: O(h)
    def getTargetCopy1(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original_node: TreeNode, cloned_node: TreeNode) -> TreeNode:
            if original_node is None:
                return None

            if original_node == target:
                return cloned_node

            return dfs(original_node.left, cloned_node.left) or dfs(original_node.right, cloned_node.right)

        return dfs(original, cloned)


original = TreeNode(7)
original.left = TreeNode(4)
original.right = TreeNode(3)
original.right.left = TreeNode(6)
original.right.right = TreeNode(19)
cloned = TreeNode(7)
cloned.left = TreeNode(4)
cloned.right = TreeNode(3)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(19)
target = original.right
assert Solution().getTargetCopy(original, cloned, target) == cloned.right

original = TreeNode(7)
cloned = TreeNode(7)
target = original
assert Solution().getTargetCopy(original, cloned, target) == cloned

original = TreeNode(8)
original.right = TreeNode(6)
original.right.right = TreeNode(5)
original.right.right.right = TreeNode(4)
original.right.right.right.right = TreeNode(3)
original.right.right.right.right.right = TreeNode(2)
original.right.right.right.right.right.right = TreeNode(1)
cloned = TreeNode(8)
cloned.right = TreeNode(6)
cloned.right.right = TreeNode(5)
cloned.right.right.right = TreeNode(4)
cloned.right.right.right.right = TreeNode(3)
cloned.right.right.right.right.right = TreeNode(2)
cloned.right.right.right.right.right.right = TreeNode(1)
target = original.right.right.right
assert Solution().getTargetCopy(original, cloned, target) == cloned.right.right.right
