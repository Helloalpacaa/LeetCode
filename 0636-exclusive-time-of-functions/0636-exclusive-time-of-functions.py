class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = [] #stack表示的是当前处理的function
        prev_time = 0

        for log in logs:
            num, typ, time = log.split(":")
            num, time = int(num), int(time)

            if typ == "start":
                if stack:
                    # 开始另一个function，中断前一个function，但是它还会在stack里，等待自己的最终的end
                    ans[stack[-1]] += time - prev_time
                stack.append(num)
                prev_time = time
            else:
                # 碰到end，结束当前function
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans