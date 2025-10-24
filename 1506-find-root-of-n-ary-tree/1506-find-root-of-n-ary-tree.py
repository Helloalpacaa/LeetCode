"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # all_nodes = set()
        # children_nodes = set()

        # for node in tree:
        #     all_nodes.add(node)
        #     for child in node.children:
        #         children_nodes.add(child)
        
        # root = (all_nodes - children_nodes).pop()

        # return root

        xor = 0
        for node in tree:
            xor ^= node.val
            for child in node.children:
                xor ^= child.val
        
        # xor is the root's val, since a ^ a = 0, x ^ 0 = x
        for node in tree:
            if node.val == xor:
                return node
        
        return None

