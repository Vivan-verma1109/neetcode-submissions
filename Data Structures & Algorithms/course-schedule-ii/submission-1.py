class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for a, b in pre:
            graph[b].append(a)
            degree[a] += 1
        
        q = deque()

        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for c in graph[course]:
                degree[c] -= 1
                if degree[c] == 0:
                    q.append(c)
        
        if len(res) == numCourses:
            return res
        return []

