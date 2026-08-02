class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l = 0
            r = len(matrix[0]) - 1

            while l <= r:
                left = matrix[row][l]
                right = matrix[row][r]
                
                if left == target or right == target:
                    return True
                
                if target > left and target < right:
                    mid = (l + r) // 2 
                    midVal = matrix[row][mid]
                    if midVal == target:
                        return True
                    
                    elif midVal > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    break
        return False
