class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(largest_sum) -> bool:
            count = 1
            curr_sum = 0

            for num in nums:
                if num > largest_sum:
                    return False

                if curr_sum + num > largest_sum:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
                else:
                    curr_sum += num
            
            return True
        
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
