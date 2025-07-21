class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = defaultdict(int)
        mod = 10**9 + 7

        for x, y in points:
            groups[y] += 1
        
        ans = total = 0
        for y, count in groups.items():
            lines = count * (count - 1) // 2 # 计算出这个y点里有多少条线
            ans = (ans + total * lines) % mod # 当前点线的数量 * 之前其他的所有线的数量
            total = (total + lines) % mod # 更新所有的线的数量
        
        return ans