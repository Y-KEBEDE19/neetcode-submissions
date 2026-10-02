# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return None

        queue = deque()
        queue.append(root)

        while queue: # while queue not empty ** while we haven't reached the end of our tree

            current_level_size = len(queue) # our current level size

            for i in range(current_level_size): # go through that level

                current_node = queue.pop() 

                if current_node.left and current_node.right: # we only switch spots if both exist
                    queue.append(current_node.left) # we append the left to our queue
                    queue.append(current_node.right) # same with right
                    
                    temp = current_node.left # 
                    current_node.left = current_node.right
                    current_node.right = temp
                elif current_node.left and not current_node.right:
                    queue.append(current_node.left)

                    current_node.right = current_node.left
                    current_node.left = None
                elif current_node.right and not current_node.left:
                    queue.append(current_node.right)

                    current_node.left = current_node.right
                    current_node.right = None
                    

        return root

            
                    

                



