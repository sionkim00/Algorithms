# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        stack = [[root, 1, 1]]
        di = defaultdict(list)

        while stack:
            curNode, curW, curLvl = stack.pop()
            if not curNode:
                continue
            di[curLvl].append(curW)
            stack.append([curNode.left, curW * 2 - 1, curLvl + 1])
            stack.append([curNode.right, curW * 2, curLvl + 1])
        maxW = 0
        for lvl in di:
            maxW = max(maxW, max(di[lvl]) - min(di[lvl]) + 1)
        return maxW