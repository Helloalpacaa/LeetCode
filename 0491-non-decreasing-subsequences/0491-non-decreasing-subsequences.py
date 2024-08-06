class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(startIdx: int, path: List[int]) -> None:
            if len(path) >= 2:
                ans.append(path[:])
            
            used = set()
            
            for i in range(startIdx, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in used:
                    continue
                
                path.append(nums[i])
                used.add(nums[i])
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return ans