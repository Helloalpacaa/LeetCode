class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count = 0
        
        # s[i]为0 or 1, 那么index i为偶数的时候，s[i]也为偶数，index为奇数的时候，s[i]也为奇数，这就组成了一个alternating string
        # 以上条件要求最终的string为010101...计算它需要修正的characters数量为count
        # 那么最终string为101010...需要修正的characters的数量就为n - count
        for i in range(n):
            if int(s[i]) != i % 2:
                count += 1
        
        return min(count, n - count)