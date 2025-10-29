class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find
        parent = defaultdict(list)
        
        def find(u) -> str:
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        
        def join(u, v) -> None:
            parent.setdefault(u, u)
            parent.setdefault(v, v)
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
        
        emails_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emails_to_name[email] = name
                join(account[1], email)
        
        unions = defaultdict(list)
        for email in emails_to_name:
            unions[find(email)].append(email)
        
        return [[emails_to_name[root]] + sorted(emails) for root, emails in unions.items()]
