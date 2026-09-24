class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        s = set(deadends)
        q = deque()
        q.append(("0000", 0))
        visited = set("0000")

        while q:
            pos, turns = q.popleft()
            if pos == target:
                return turns
            
            for i in range(4):
                up = pos[:i] + str((int(pos[i]) + 1) % 10) + pos[i+1:]
                down = pos[:i] + str((int(pos[i]) - 1) % 10) + pos[i+1:]

                for nxt in (up, down):
                    if nxt not in visited and nxt not in s:
                        visited.add(nxt)
                        q.append((nxt, turns + 1))
        
        return -1

                
            


            