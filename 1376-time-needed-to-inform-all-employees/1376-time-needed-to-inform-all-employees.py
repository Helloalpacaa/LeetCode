class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)
        
        def dfs(employee):
            max_time = 0
            for subordinate in subordinates[employee]:
                max_time = max(max_time, dfs(subordinate))
            
            return max_time + informTime[employee]
        
        return dfs(headID)
