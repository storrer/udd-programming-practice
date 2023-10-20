"""

"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x_index, x in enumerate(grid):
            for y_index, y in enumerate(x):
                if y == "1":
                    self.find_connections(grid, x_index, y_index)
                    count += 1
                    grid[x_index][y_index] = "0"

        return count
        
    def find_connections(self, grid, x, y):
        # "Look" north, East, South West
        connections = [(x,y)]
        north = (-1, 0)
        east = (0, 1)
        south = (1, 0)
        west = (0, -1)
        transformations = [north,east,south,west]
        # North Search
        while connections:
            x_curr,y_curr = connections.pop()      
            for transformation in transformations:
                x_trans = x_curr + transformation[0]
                y_trans = y_curr + transformation[1]

                if self.is_in_grid(grid, x_trans, y_trans) and grid[x_trans][y_trans] == "1":
                    connections.append((x_trans,y_trans))
                    grid[x_trans][y_trans] = "0"


        
    
    def is_in_grid(self, grid, x, y):
        return x in range(0,len(grid)) and y in range(len(grid[0]))

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid2))
print(sol.numIslands(grid1))
