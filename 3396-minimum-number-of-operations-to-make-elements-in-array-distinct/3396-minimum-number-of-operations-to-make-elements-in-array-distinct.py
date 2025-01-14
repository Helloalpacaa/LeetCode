class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        occur = defaultdict(int)

        for i in range(n - 1, -1, -1):
            if nums[i] in occur:
                if (i + 1) % 3 > 0:
                    return (i + 1) // 3 + 1
                else:
                    return (i + 1) // 3
            occur[nums[i]] += 1

        return 0