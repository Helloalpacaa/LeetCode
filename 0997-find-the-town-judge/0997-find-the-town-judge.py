class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:   
        indegree = [0] * (n + 1)

        for person, judger in trust:
            indegree[person] -= 1
            indegree[judger] += 1
        
        for i in range(1, n + 1):
            if indegree[i] == n - 1:
                return i
        
        return -1

        