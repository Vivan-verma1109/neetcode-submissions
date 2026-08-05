class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        graph = defaultdict(list)
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

            for nxt in graph[course]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
        if len(res) == numCourses:
            return res

        return []
