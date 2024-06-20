class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        i = 0
        j = 0
        
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] >= secondList[j][0] and firstList[i][1] <= secondList[j][1]:
                intersection.append([max(firstList[i][0], secondList[j][0]), firstList[i][1]])
                i += 1
            elif secondList[j][1] >= firstList[i][0] and secondList[j][1] <= firstList[i][1]:
                intersection.append([max(firstList[i][0],secondList[j][0]), secondList[j][1]])
                j += 1
            elif firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
        
        return intersection
            