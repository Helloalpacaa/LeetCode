class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        stack = []

        for num in nums:
            while stack and stack[-1] * num <= k:
                num = stack.pop() * num
            stack.append(num)

        return len(stack)