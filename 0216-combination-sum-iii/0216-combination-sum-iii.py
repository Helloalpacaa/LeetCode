class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtracking(path: List[int], startNum: int, total: int) -> None:
            if len(path) > k:
                return
            
            if len(path) == k and total == n:
                ans.append(path[:])
                return
            
            for num in range(startNum, 10):
                path.append(num)
                total += num
                backtracking(path, num + 1, total)
                total -= num
                path.pop()
        
        backtracking([], 1, 0)
        return ans