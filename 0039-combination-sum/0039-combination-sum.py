class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtracking(start, total, path) -> None:
            if total == target:
                ans.append(path[:])
                return
            
            if total > target:
                return
            
            for i in range(start, n):
                if total > target:
                    break
                    
                total += candidates[i]
                path.append(candidates[i])
                backtracking(i, total, path)
                total -= candidates[i]
                path.remove(path[-1])
        
        backtracking(0, 0, [])
        return ans