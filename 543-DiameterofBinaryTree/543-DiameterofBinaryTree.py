        def dfs(root):
            if not root:
                return 0
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
# class TreeNode:

# Definition for a binary tree node.
            return max(dfs(root.left), dfs(root.right)) + 1
            
        return dfs(root) + 1
[
