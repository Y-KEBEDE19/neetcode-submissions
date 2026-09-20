"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        
        # Implementing Depth First Search: 
        new_to_old = {}

        def clone(node):
            if node in new_to_old: # Base Case
                return new_to_old[node] # return the copy of the node in our map

            # recursive section:
            copy = Node(node.val)
            new_to_old[node] = copy # deep_clone of our node

            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy

        return clone(node) if node else None