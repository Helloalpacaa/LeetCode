class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        groups: dict[str, list[str]] = defaultdict(list)
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            groups[name].append((int(time), int(amount), city, i, transaction))
        
        print(groups)
        
        invalid = []
        for name, group in groups.items():
            n = len(group)
            for i in range(n):
                time_i, amount_i, city_i, index_i, transaction_i = group[i]

                if amount_i > 1000:
                    invalid.append(transaction_i)
                else:
                    for j in range(n):
                        if i == j:
                            continue
                        time_j, amount_j, city_j, index_j, transaction_j = group[j]
                        if abs(time_i - time_j) <= 60 and city_i != city_j and index_i != index_j:
                            invalid.append(transaction_i)
                            break
        
        return invalid
