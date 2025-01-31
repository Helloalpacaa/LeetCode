class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)

        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(web)
        
        patterns = Counter()
        for user, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))
        
        return max(sorted(patterns), key=patterns.get)