class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. sort the candidates array to avoid duplicate combination
        candidates.sort()
        combinations = []

        def backtracking(index: int, path: List[int], curr_sum) -> None:
            if curr_sum == target:
                combinations.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                if curr_sum > target:
                    break
                
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                curr_sum += candidates[i]
                backtracking(i + 1, path, curr_sum)
                curr_sum -= candidates[i]
                path.pop()
        
        backtracking(0, [], 0)
        return combinations