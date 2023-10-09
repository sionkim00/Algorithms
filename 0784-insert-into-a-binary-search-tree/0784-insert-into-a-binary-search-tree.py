# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root

        if not root:
            newNode = TreeNode(val)
            return newNode

        while head:
            if not head:
                break
            if not head.left and head.val > val:
                newNode = TreeNode(val)
                head.left = newNode
                break
            if not head.right and head.val < val:
                newNode = TreeNode(val)
                head.right = newNode
                break
            if val > head.val:
                head = head.right
            else:
                head = head.left

        return root