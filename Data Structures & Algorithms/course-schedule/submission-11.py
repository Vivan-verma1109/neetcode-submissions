class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = {}
        degree = [0] * numCourses

        for i in range(numCourses):
            graph[i] = []

        for a, b in pre:
            graph[b].append(a)
            degree[a] += 1
        
        q = deque()

        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        
        taken = 0
        while q:
            course = q.popleft()
            taken += 1

            for nxt in graph[course]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
        return taken == numCourses