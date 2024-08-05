class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        paths = []
        path = []

        def backtracking(startIdx: int, path: List[int]) -> None:
            if len(path) == k:
                paths.append(path[:])
                return
            
            for i in range(startIdx, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(1, [])
        return paths