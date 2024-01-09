        seq1 = []
        seq2 = []

        def dfs1(root):
            if not root:
                return
            if not root.left and not root.right:
                seq1.append(root.val)
            dfs1(root.left)
Optional[TreeNode]) -> bool:
    def leafSimilar(self, root1: Optional[TreeNode], root2: 
[
