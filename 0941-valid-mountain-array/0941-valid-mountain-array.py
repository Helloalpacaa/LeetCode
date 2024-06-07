class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        maxIndex = arr.index(max(arr))
        if maxIndex == 0 or maxIndex == len(arr) - 1:
            return False
        
        for i in range(0, maxIndex + 1):
            if i > 0 and arr[i] <= arr[i - 1]:
                return False
        
        for i in range(maxIndex, len(arr)):
            if i > maxIndex and arr[i] >= arr[i - 1]:
                return False
        
        return True