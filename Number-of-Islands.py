'''
'''

class Solution:
    def numIslands(self, grid):
        if len(grid) < 1:
            return 0

        num_isl = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.walk(grid, r, c)
                    num_isl += 1
        return num_isl

    def walk(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] == "1":
            grid[r][c] = 0
            self.walk(grid, r-1,c)
            self.walk(grid, r+1,c)
            self.walk(grid, r,c-1)
            self.walk(grid, r,c+1)


grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid_1))
print(sol.numIslands(grid_2))