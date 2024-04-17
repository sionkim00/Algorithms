#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, 
root: Optional[TreeNode]) -> str:
        def helper(root, cur):
            if not root:
                return
            
            cur = chr(ord('a') + 
root.val) + cur
            
[
