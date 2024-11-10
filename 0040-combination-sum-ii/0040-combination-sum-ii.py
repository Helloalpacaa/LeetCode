class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtracking(path: List[int], startIdx: int, total: int) -> None:
            if total == target:
                ans.append(path[:])
                return
            
            for i in range(startIdx, len(candidates)):
                if total > target:
                    break
                
                if i > startIdx and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                total += candidates[i]
                backtracking(path, i + 1, total)
                total -= candidates[i]
                path.pop()
        
        backtracking([], 0, 0)
        return ans