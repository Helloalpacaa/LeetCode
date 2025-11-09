class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def is_balanced(num: int) -> bool:
            count = defaultdict(int)
            for c in str(num):
                count[c] += 1
            
            for c in str(num):
                if int(c) != count[c]:
                    return False
            
            return True
        
        x = n + 1
        while x:
            if is_balanced(x):
                return x
            x += 1
        