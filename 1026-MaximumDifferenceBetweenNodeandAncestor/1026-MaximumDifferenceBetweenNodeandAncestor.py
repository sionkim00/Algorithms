            if maxVal is not None:
                ans[0] = max(ans[0], abs(root.val - maxVal))

            else:
                minVal = root.val
            else:
                maxVal = root.val
            dfs(root.left, min(minVal, root.val), max(maxVal, root.val))
            dfs(root.right, min(minVal, root.val), max(maxVal, root.val))

        dfs(root, None, None)

        return ans[0]
[
