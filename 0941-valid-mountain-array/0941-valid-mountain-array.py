class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(arr):
            if i + 1 < len(arr) and arr[i + 1] > arr[i]:
                i += 1
            else:
                break
        
        j = len(arr) - 1
        while j >= 0:
            if j - 1 >= 0 and arr[j - 1] > arr[j]:
                j -= 1
            else:
                break
        
        return False if i == 0 or j == len(arr) - 1 or i != j else True