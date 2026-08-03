class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        q = deque(people)
        print(q)
        boats = 0

        while q:
            right = q.pop()
            if not q:
                boats += 1
                break
            left = q.popleft()

            if right + left <= limit:
                boats += 1
            else:
                q.appendleft(left)
                boats += 1
        return boats