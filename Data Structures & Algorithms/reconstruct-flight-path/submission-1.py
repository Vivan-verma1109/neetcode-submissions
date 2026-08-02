class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        t = set()

        for a, b in tickets:
            t.add(a)
            t.add(b)
        for i in t:
            graph[i] = []
        for a, b in tickets:
            graph[a].append(b)
        print(graph)
        
        for src in graph:
            graph[src].sort(reverse = True)

        ret = []

        def dfs(flight):
            while graph[flight]:
                nxt = graph[flight].pop()
                dfs(nxt)
            ret.append(flight)
        dfs("JFK")
        print(ret)
        return ret[::-1]