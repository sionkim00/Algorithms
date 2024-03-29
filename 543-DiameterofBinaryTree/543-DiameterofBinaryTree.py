#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            ans[0] = max(ans[0], left + right)
            return max(left, right)
        dfs(root)
        return ans[0]
[
