        def dfs(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            
            return l.val == r.val and dfs(l.left, r.left) and dfs
(l.right, r.right)
        return dfs(p, q)
[
