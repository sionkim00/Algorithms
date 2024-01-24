            newCounter[root.val] += 1
            if not root.val in newCounter:
                newCounter[root.val] = 0
            if not root:
                return 0
            newCounter = {**counter}
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root, counter):
#         self.right = right
class Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
[
