class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        largest_outlier = float('-inf')

        # for num in nums:
        #     sum_element = (total - num) // 2 # 会过不了所有的test case，因为假设[7, 8, 10],10会被当成outlier
        #     if sum_element in count:
        #         if num != sum_element or count[sum_element] > 1:
        #             largest_outlier = max(largest_outlier, num)

        # 我们不能iterate number来assume它是potential outlier，而是assume它是sum_element然后去找outlier
        for num in count:
            potential_outlier = total - num * 2
            
            if potential_outlier in count:
                if potential_outlier != num or count[num] > 1:
                    largest_outlier = max(largest_outlier, potential_outlier)

        return largest_outlier