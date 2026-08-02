class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in pre:
            graph[b].append(a)
        
        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True