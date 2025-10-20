class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        groups = defaultdict(list)
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            groups[name].append([int(time), int(amount), city, transaction])
        
        for name, trans in groups.items():
            trans.sort(key=lambda x:x[0])

            for i in range(len(trans)):
                time_i, amount_i, city_i, raw_i = trans[i]

                if amount_i > 1000:
                    invalid.add(raw_i)
                
                j = i - 1
                while j >= 0 and time_i - trans[j][0] <= 60 and city_i != trans[j][2]:
                    invalid.add(raw_i)
                    invalid.add(trans[j][3])
                    j -= 1
                
                j = i + 1
                while j < len(trans) and trans[j][0] - time_i <= 60 and city_i != trans[j][2]:
                    invalid.add(raw_i)
                    invalid.add(trans[j][3])
                    j += 1
        
        return list(invalid)
                
