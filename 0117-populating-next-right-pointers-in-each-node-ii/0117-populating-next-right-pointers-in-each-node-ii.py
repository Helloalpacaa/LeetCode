"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        # queue = deque([root])

        # while queue:
        #     size = len(queue)
        #     while size > 0:
        #         node = queue.popleft()
        #         size -= 1
        #         if size > 0:
        #             node.next = queue[0]
                
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # return root

        original_root = root

        while root:
            dummy = Node()
            curr = dummy

            while root:
                if root.left:
                    curr.next = root.left
                    curr = curr.next
                if root.right:
                    curr.next = root.right
                    curr = curr.next
                root = root.next
            root = dummy.next
        
        return original_root
        