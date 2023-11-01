# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            leftBool, leftVal = dfs(root.left)
            rightBool, rightVal = dfs(root.right)

            curBool = leftBool and rightBool
            if abs(leftVal - rightVal) > 1:
                curBool = False

            return [curBool and rightBool, 1 + max(leftVal, rightVal)]
        ansBool, ansVal = dfs(root)
        return ansBool
