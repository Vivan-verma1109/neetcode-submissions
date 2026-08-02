class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in matrix:
            if i[-1] >= target:
                arr = i
                break
        print(arr)
        l = 0 
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if arr[mid] == target:
                return True

            elif arr[mid] > target:
                r = mid - 1
            
            elif arr[mid] < target:
                l = mid + 1
        return False