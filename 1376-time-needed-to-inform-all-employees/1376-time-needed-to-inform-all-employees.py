class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_list = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                manager_list[manager[i]].append(i)

        def dfs(managerID: int, time: int) -> int:
            if not manager_list[managerID]:
                return time

            max_time = 0
            for employee in manager_list[managerID]:
                max_time = max(max_time, dfs(employee, time + informTime[managerID]))
            
            return max_time

        return dfs(headID, 0)