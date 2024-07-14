# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        total = []
        count = []
        self.traversal(root, 0, total, count)
        for i in range(len(total)):
            ans.append(total[i] / count[i])
        
        return ans
    
    def traversal(self, node: Optional[TreeNode], height: int, total: List[int], count: List[int]) -> None:
        if node is None:
            return
        
        if len(total) <= height:
            total.append(0)
            count.append(0)
            
        total[height] += node.val
        count[height] += 1
        
        self.traversal(node.left, height + 1, total, count)
        self.traversal(node.right, height + 1, total, count)
        