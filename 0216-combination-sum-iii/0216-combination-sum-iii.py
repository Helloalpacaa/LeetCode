class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        used = [False] * 10

        def dfs(total: int, num: int, path: list[int], used_numbers: int):
            if total == n and used_numbers == k:
                res.append(path.copy())
                return
            
            if total >= n or used_numbers >= k:
                return
            
            for i in range(num, 10):
                if not used[i]:
                    used[i] = True
                    path.append(i)
                    dfs(total + i, i, path, used_numbers + 1)
                    path.pop()
                    used[i] = False
        
        dfs(0, 1, [], 0)
        return res
