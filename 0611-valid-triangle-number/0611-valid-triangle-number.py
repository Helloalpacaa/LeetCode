class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()

        for k in range(len(nums) - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # all the pairs from i to j - 1 with j can form a triangle
                    res += j - i
                    # move j to j - 1 to check if j - 1 can form a traiangle
                    j -= 1
                else:
                    # need to get a larger nums[i]
                    i += 1
        
        return res

                