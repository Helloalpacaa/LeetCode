class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i = 0
        j = len(people) - 1
        
        while i <= j:
            leftSpace = limit - people[j]
            if i < j and leftSpace >= people[i]:
                i += 1
            
            boats += 1
            j -= 1
        
        return boats
            
            