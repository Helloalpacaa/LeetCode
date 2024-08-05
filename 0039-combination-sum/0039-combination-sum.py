class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtracking(path: List[int], startIdx: int, total: int) -> None:
            if total > target:
                return
            
            if total == target:
                ans.append(path[:])
                return
            
            for i in range(startIdx, len(candidates)):
                if total > target:
                    break

                path.append(candidates[i])
                total += candidates[i]
                backtracking(path, i, total)
                total -= candidates[i]
                path.pop()
            
        backtracking([], 0, 0)
        return ans