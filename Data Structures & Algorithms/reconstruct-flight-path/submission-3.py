class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for a,b in tickets:
            graph[a].append(b)
        print(graph)
        res = []

        for src in graph:
            graph[src].sort(reverse = True)

        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            res.append(node)
        
        dfs("JFK")
        return (res[::-1])
