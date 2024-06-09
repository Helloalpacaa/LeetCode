class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        arr = list(s)
        while i < len(s):
            self.reverse(arr, i, min(i + k - 1, len(s) - 1))
            i += k * 2
        
        return "".join(arr)
    
    def reverse(self, arr: list, i: int, j: int) -> None:
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
            