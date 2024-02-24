            for nei in adj[src]:
                dfs(nei, adj)
        
        for t in sorted(list(time_map.keys())):
            visit = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src, time_map[t])
            visit.add(src)
            secrets.add(src)

        return list(secrets)
            if src in visit:
                return
6
