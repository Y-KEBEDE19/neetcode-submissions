class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Solving this with depth first search: 

        # Approach: 

        # We loop through the each value of the grid using a traditional nested loop
        # we pass that pair of values, (x,y) to our dfs function: 
        # our function checks if it is a valid pair, meaning it's not water 
        # goes every direction recursively and eventually returning back to our nested loop
        # when it reaches our nested loop, the whole connected island has been processed
        # so we increase count (which is the number of islands we have seen)

        # we can either use a visited set, or we can set the value to 0 once we have seen it

        # This solution we will use a visisted set: 

        row,col = len(grid), len(grid[0]) # the length of our rows and columns
        count = 0 # number of islands we have seen so far, which initially is 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #visited = set() # Initalizing our set

        # Here we will Implement our dfs function: 
        def dfs(x ,y ):
            # Base Case:
            if x >= row or x < 0 or y >= col or y < 0 or grid[x][y] == "0":
                return
            
            grid[x][y] = "0"
            # recursive case:
            for dx,dy in directions: 
                dfs(x + dx, y + dy)
    
            
        for r in range(row): 
            for c in range(col):
                if grid[r][c] == "1": # if this pair has not been visited
                    dfs(r,c)
                    count += 1

        return count



