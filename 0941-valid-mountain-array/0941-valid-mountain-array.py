class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 0
        right = len(arr) - 1
        
        while left + 1 < len(arr) and arr[left + 1] > arr[left]:
            left += 1
        
        while right - 1 >= 0 and arr[right - 1] > arr[right]:
            right -= 1
        
        return left == right and left != 0 and right != len(arr) - 1