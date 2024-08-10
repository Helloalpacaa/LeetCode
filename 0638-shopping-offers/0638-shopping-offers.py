class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}

        def backtracking(curr_needs: List[int]) -> int:
            if sum(curr_needs) == 0:
                return 0
            
            if tuple(curr_needs) in memo:
                return memo[tuple(curr_needs)]
            
            min_cost = sum(curr_needs[i] * price[i] for i in range(len(curr_needs)))

            for sale in special:
                if all(curr_needs[i] >= sale[i] for i in range(len(curr_needs))):
                    new_needs = [curr_needs[i] - sale[i] for i in range(len(curr_needs))]
                    min_cost = min(min_cost, sale[-1] + backtracking(new_needs))
            
            memo[tuple(curr_needs)] = min_cost
            return min_cost
        
        return backtracking(needs)
