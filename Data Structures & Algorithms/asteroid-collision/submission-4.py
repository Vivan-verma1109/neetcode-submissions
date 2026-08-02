class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if abs(ast) > stack[-1]:
                    stack.pop()
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    ast = 0
                else:
                    ast = 0
                
            
            if ast:
                stack.append(ast)
                
        
        return stack