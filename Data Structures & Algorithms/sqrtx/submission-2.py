class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if mid*mid == x:
                return mid
            
            elif mid*mid > x:
                right = mid - 1
            
            else :
                left = mid + 1
                res = mid
        
        return res