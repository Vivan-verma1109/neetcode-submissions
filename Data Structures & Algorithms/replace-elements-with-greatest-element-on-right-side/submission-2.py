class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        for i in range(len(arr) -1, -1, -1):
            temp = max(arr[i], biggest)
            arr[i] = biggest
            biggest = temp
        return (arr)
