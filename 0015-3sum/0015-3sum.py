class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. sort nums
        nums.sort()
        
        ans = []

        # 2. iterate each element in nums, using two pointers to look for the solution
        for i in range(len(nums)):
            # skip the duplicate value
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # if nums[i] > 0, there is no chance that we can find a solution that 3sum == 0
            if nums[i] > 0:
                break
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                # if 3sum == 0, add it into ans, increment left pointer and decrement right pointer until left == right
                if three_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
                # if 3sum < 0, we increment the left poiner
                elif three_sum < 0:
                    left += 1
                # if 3sum > 0, we decrement the right pointer
                else:
                    right -= 1
        
        return ans
                
                