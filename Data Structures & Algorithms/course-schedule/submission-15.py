class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = defaultdict(list)

        for a, b in pre:
            graph[b].append(a)
            in_degree[a] += 1
        
        q = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for nxt in graph[course]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
        

        return taken == numCourses