class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 找到在window size为minutes的情况下，最大能转换的customers数量（只去计算grumpy为1的部分）
        satisified = 0
        max_satisfied = 0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                satisified += customers[i]

            if i >= minutes and grumpy[i - minutes] == 1:
                satisified -= customers[i - minutes]
            
            max_satisified = max(satisified, max_satisfied)
        
        return sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0) + max_satisified
            

