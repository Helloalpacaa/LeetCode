# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def traversal(node: 'TreeNode') -> 'TreeNode':
            if node is None:
                return None
            
            left = traversal(node.left)
            right = traversal(node.right)
        
            # 如果这个node在nodes里，那么不管left和right的return结果是什么，都往上返回这个node
            # 哪怕left和right里有其他nodes，那这个node也是它们的LCA
            if node in nodes:
                return node
            
            # 如果当前node不在nodes里，但是left和right都有返回值，说明当前node是LCA
            if left and right:
                return node
            
            # 如果前面两种情况都不是，那么就return left or right的结果，任意其中一个有值那就return有值的一方
            # 如果它们都为None那return的也是None
            return left or right
            
        return traversal(root)
            