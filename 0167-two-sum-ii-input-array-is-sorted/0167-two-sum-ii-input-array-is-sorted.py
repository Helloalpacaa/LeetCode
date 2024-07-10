class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            twoSum = numbers[i] + numbers[j]
            if twoSum < target:
                i += 1
            elif twoSum > target:
                j -= 1
            else:
                ans.append(i + 1)
                ans.append(j + 1)
                return ans
                