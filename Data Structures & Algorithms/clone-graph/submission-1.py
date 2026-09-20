"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Implementing Depth_First Search: 

        # Given a node -> return a deep copy 
        # Implemetning recursive DFS
        # Base Case: if our node has already been copied, determined using hash_map
        # Recursive Case: loop through the neighbors and add each by recursively calling the function

        old_to_new = {}
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            
            return copy

        return clone(node) if node else None
            