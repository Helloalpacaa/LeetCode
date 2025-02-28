class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_count = dict(sorted(count.items(), key=lambda item:-item[1]))

        ans = []
        for key, value in sorted_count.items():
            for _ in range(value):
                ans.append(key)
        
        return "".join(ans)