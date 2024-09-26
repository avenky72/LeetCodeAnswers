class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        size = len(nums3)
        if size % 2 == 0:
            mid = int(size//2)
            mid2 = mid - 1
            median = float(nums3[mid] + nums3[mid2]) / 2
        else:
            mid = size // 2
            median = (nums3[mid])
        return float(median)
