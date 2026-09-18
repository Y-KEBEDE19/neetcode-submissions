# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #Solving using breadth-first-search: 

        res = [] # iniatlize our result list
        queue = [] # iniatlize our queue

        if not root: # if root is empty, tree is empty, return empty list
            return []
        
        #otherwise let's perform breadth-first-search:
        queue.append(root) # we append the root into our queue, head of tree 
        while queue: # while our queue is not empty, 
            levelSize = len(queue) # size of our current level
            currentLevel = []

            for i in range(levelSize): # our current levelSize
                n = queue.pop(0) 
                currentLevel.append(n.val)

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            res.append(currentLevel) # we add currentLevel(sublist) into res
        
        return res