class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(node):
            if node in visiting:
                return False
            if graph[node] == []:
                return True
            visiting.add(node)
            
            res = True
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            visiting.remove(node)
            graph[node] = []
            return True

        visiting = set()
        for key in graph:
            if not(dfs(key)):
                return False
        return True