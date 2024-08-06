class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtracking(path: List[int], startIdx: int) -> None:
            ans.append(path[:])

            for i in range(startIdx, len(nums)):
                if i > startIdx and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtracking(path, i + 1)
                path.pop()
        
        backtracking([], 0)
        return ans