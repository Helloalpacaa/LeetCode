class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                two_sum = nums[i] + nums[j]
                target = 0 - two_sum

                if two_sum > 0:
                    break

                left = j + 1
                right = n - 1
                while left <= right:
                    mid = (left + right) // 2

                    if nums[mid] == target:
                        ans.append([nums[i], nums[j], target])
                        break
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return ans
