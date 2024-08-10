class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtracking(count: int, curr_sum: int, index: int) -> bool:
            if count == k:
                return True
            
            if curr_sum == target:
                return backtracking(count + 1, 0, 0)
            
            for i in range(index, len(nums)):
                if used[i] or nums[i] > target - curr_sum:
                    continue
                
                used[i] = True
                if backtracking(count, curr_sum + nums[i], i + 1):
                    return True
                used[i] = False

                if curr_sum == 0:
                    break
            
            return False
        
        nums.sort(reverse=True)
        return backtracking(0, 0, 0)

                
