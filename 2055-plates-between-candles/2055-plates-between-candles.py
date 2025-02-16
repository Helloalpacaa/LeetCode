class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        arr = []
        for i in range(len(s)):
            if s[i] == '|':
                arr.append(i)
        
        prefix_sum = [0] * len(arr)
        for i in range(1, len(arr)):
            prefix_sum[i] = prefix_sum[i - 1] + (arr[i] - arr[i - 1] - 1)
        
        ans = []
        for query in queries:
            left = bisect.bisect_left(arr, query[0])
            right = bisect.bisect_right(arr, query[1]) - 1
            if left > right or left >= len(arr) or right < 0:
                ans.append(0)
            else:
                ans.append(prefix_sum[right] - prefix_sum[left])
        
        return ans