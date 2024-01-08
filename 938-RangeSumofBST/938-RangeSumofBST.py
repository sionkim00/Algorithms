        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if root.val >= low and root.val <= high:
                res[0] += root.val
            dfs(root.right)
        dfs(root)
        return res[0]
[
