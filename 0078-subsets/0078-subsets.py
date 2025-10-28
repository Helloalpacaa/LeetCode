class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index: int, path: list[int]) -> None:
            res.append(path.copy())

            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res