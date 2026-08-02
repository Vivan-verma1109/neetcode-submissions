class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for x in range(len(temperatures)):
        
            while stack and temperatures[x] > temperatures[stack[-1]]:
                res[stack.pop()] = x - stack[-1]
        
            stack.append(x)
        
        return res
