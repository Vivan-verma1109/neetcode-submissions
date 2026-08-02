class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + (nums2)
        nums1.sort()
        print(nums1)

        if len(nums1) % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            r = nums1[len(nums1) // 2]
            l = nums1[(len(nums1) - 1) // 2]
            return (l + r) / 2
