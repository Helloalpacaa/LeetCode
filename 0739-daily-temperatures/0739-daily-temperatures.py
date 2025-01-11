class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        monotonic_stack = deque()

        for i in range(n):
            while monotonic_stack and temperatures[i] > temperatures[monotonic_stack[-1]]:
                # 不能用这种写法，Python不像Java是按先后顺序的
                # ans[monotonic_stack[-1]] = i - monotonic_stack.pop()
                prev_day = monotonic_stack.pop()
                ans[prev_day] = i - prev_day
            monotonic_stack.append(i)

        return ans
