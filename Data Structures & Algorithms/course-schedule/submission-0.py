class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for a, b in pre:
            graph[b].append(a)
        print(graph)

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
        for course in graph:
            if not dfs(course):
                return False
        return True
