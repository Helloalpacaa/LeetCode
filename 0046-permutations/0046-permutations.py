class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(path: List[int], used: set[int]) -> None:
            if len(path) == len(nums):
                ans.append(path[:])

            for i in range(0, len(nums)):
                if i in used:
                    continue

                path.append(nums[i])
                used.add(i)
                backtracking(path, used)
                used.remove(i)
                path.pop()
        
        backtracking([], set())
        return ans
