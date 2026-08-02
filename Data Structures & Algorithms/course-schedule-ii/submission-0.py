class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        in_degree = [0] * numCourses
        for a, b in pre:
            graph[b].append(a)
            in_degree[a] += 1
        print(graph)
        
        q = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        print(q)
        ret = []
        while q:
            course = q.popleft()
            ret.append(course)

            for nxt in graph[course]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
        if len(ret) == numCourses:
            return ret
        return []

