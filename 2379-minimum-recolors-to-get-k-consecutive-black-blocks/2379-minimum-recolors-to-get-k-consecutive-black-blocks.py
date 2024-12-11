class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 找出在一个size为7的subarray里，B最多出现几次，最终用k减去这个值
        black = 0
        max_black = 0

        for i in range(len(blocks)):
            if blocks[i] == 'B':
                black += 1
            
            if i >= k and blocks[i - k] == 'B':
                black -= 1
            
            max_black = max(max_black, black)
        
        return k - max_black
                
            
            