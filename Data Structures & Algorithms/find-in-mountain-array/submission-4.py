class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # step 1 find the peak
        n = mountainArr.length()
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        print(peak)

        # search left first

        l = 0
        r = peak

        while l <= r:
            mid = (l + r) // 2
            temp = mountainArr.get(mid)
            if temp == target:
                return mid
            if temp > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # search roght
        l = peak + 1
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            temp = mountainArr.get(mid)
            if temp == target:
                return mid
            if temp > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
