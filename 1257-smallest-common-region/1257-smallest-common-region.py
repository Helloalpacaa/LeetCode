class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            for i in range(1, len(region)):
                parent[region[i]] = region[0]
        print(parent)
        ancestors1 = set()

        while region1:
            ancestors1.add(region1)
            region1 = parent.get(region1)
        
        print(ancestors1)
        while region2 not in ancestors1:
            print(region2)
            region2 = parent[region2]
        
        return region2