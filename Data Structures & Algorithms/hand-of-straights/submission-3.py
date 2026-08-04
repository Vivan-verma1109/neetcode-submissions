class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        sortC = sorted(c.keys())
        print(c)

        for x in sortC:
            while c[x] > 0:
                for y in range(x, x + groupSize):
                    if c[y] == 0:
                        return False
                    c[y] -= 1
        return True
                
