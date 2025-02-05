class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif nums[left] > nums[right]: # If the array is rotated
                if nums[left] <= nums[mid]: # If left part is rotated
                    if nums[left] <= target < nums[mid]: # If the target is in the left part
                        right = mid - 1
                    else:
                        left = mid + 1
                else: # If right part is rotated
                    if nums[mid] < target <= nums[right]: # If the target is in the right part
                        left = mid + 1
                    else:
                        right = mid - 1
            else: # The array is not rotated, use the normal binary search
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

