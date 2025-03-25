class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtracking(index: int, path: List[int]) -> None:
            if index > n:
                return

            ans.append(path[:])

            for i in range(index, n):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return ans