class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtracking(startIdx: int, path: List[int], curr_sum: int) -> None:
            if curr_sum == target:
                ans.append(path[:])
                return
            
            if curr_sum > target:
                return
            
            for i in range(startIdx, len(candidates)):
                curr_sum += candidates[i]
                path.append(candidates[i])
                backtracking(i, path, curr_sum)
                path.pop()
                curr_sum -= candidates[i]
        
        backtracking(0, [], 0)
        return ans