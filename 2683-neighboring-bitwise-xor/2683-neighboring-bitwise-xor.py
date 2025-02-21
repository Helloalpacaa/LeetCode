class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0] * n
        
        for i in range(n - 1):
            if derived[i] == 0:
                original[i + 1] = original[i]
            else:
                original[i + 1] = 0 if original[i] == 1 else 1
        
        if derived[n - 1] == 0:
            if original[n - 1] == original[0]:
                return True
        else:
            if original[n - 1] != original[0]:
                return True
        
        return False
        
