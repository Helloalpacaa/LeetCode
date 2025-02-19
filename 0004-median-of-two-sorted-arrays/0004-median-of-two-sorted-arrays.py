class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = (m + n + 1) // 2

        left = 0
        right = m
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1

            left1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            right1 = float('inf') if mid1 == m else nums1[mid1]
            left2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            right2 = float('inf') if mid2 == n else nums2[mid2]

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 <= right2:
                left = mid1 + 1
            else:
                right = mid1 - 1