class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = dict()
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        
        lucky_number = -1
        for key in frequency.keys():
            if key == frequency[key]:
                lucky_number = max(lucky_number, key)

        return lucky_number