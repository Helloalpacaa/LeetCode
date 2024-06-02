class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            a1 = firstList[i][0]
            a2 = firstList[i][1]
            b1 = secondList[j][0]
            b2 = secondList[j][1]
            
            if (a1 <= b2 and b1 <= a2) or (b1 <= a2 and b2 >= a1):
                intersection.append([max(a1, b1), min(a2, b2)])
                
            if (a2 < b2):
                i += 1
            else:
                j += 1
            
        return intersection