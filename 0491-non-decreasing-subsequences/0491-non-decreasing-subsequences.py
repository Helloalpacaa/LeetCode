class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(path: List[int], index: int) -> None:
            if len(path) >= 2:
                ans.append(path[:])
            
            used = set()

            for i in range(index, len(nums)):
                if path and nums[i] < path[-1] or nums[i] in used:
                    continue
                
                path.append(nums[i])
                used.add(nums[i])
                backtracking(path, i + 1)
                path.pop()
        
        backtracking([], 0)
        return ans