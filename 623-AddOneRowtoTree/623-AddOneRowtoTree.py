                return
            if not root:
            if depth > 2:
                left = TreeNode(val, root.left, None)
                right = TreeNode(val, None, root.right)

                dfs(root.left, depth-1)
                dfs(root.right, depth-1)
            else:
        def dfs(root, depth):
[
