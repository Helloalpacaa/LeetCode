class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0, len(s), k * 2):
            self.reverse(arr, i, min(i + k - 1, len(s) - 1))
            
        return "".join(arr)
    
    def reverse(self, arr: list, i: int, j: int) -> None:
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            