# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #BFS Implementation: 

        if not root:
            return 0

        queue = deque()

        queue.append(root)
        count = 0

        while queue:
            current_level = len(queue)
            
            for i in range(current_level):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            count += 1

        return count







