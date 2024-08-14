class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda p:(-p[0], p[1]))

        for i in range(len(people)):
            ans.insert(people[i][1], people[i])
        
        return ans