# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.sets = set()
        self.traversal(root, 0)
    
    def traversal(self, node: Optional[TreeNode], val: int) -> None:
        if node is None:
            return
        
        node.val = val
        self.sets.add(val)

        self.traversal(node.left, val * 2 + 1)
        self.traversal(node.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.sets


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)