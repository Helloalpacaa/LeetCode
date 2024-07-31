# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        # 前置遍历，在到达每一个节点时先更新从root到这个节点的最大值和最小值，然后把maxDiff向上返回
        def traversal(node: Optional[TreeNode], minVal: int, maxVal: int) -> int:
            if node is None:
                return maxVal - minVal
            
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            left = traversal(node.left, minVal, maxVal)
            right = traversal(node.right, minVal, maxVal)

            return max(left, right, maxVal - minVal)
        
        return traversal(root, root.val, root.val)