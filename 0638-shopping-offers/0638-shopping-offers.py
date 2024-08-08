class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        # looking for the minimum cost
        def backtracking(current_needs: List[int]) -> int :
            if sum(current_needs) == 0:
                return 0
            
            # use a tuple as a key of memo, because tuple won't be accidentaly modified
            # and it's more memory efficient than list
            if tuple(current_needs) in memo:
                return memo[tuple(current_needs)]

            # Initialize with buying everything at regular price
            min_cost = sum(price[i] * current_needs[i] for i in range(len(needs)))

            for offer in special:
                if all(offer[i] <= current_needs[i] for i in range(len(needs))):
                    new_needs = [current_needs[i] - offer[i] for i in range(len(needs))]
                    offer_cost = offer[-1] + backtracking(new_needs)
                    min_cost = min(min_cost, offer_cost)
            
            memo[tuple(current_needs)] = min_cost
            return min_cost

        memo = {}
        return backtracking(needs)
                    

