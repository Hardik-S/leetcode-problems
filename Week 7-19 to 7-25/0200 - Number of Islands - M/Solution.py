class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        numIsle = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.findAdj(grid, i, j)
                    numIsle += 1
        print("numIsle: ", numIsle)
        return numIsle

    def findAdj(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = ''
        self.findAdj(grid, i + 1, j)
        self.findAdj(grid, i - 1, j)
        self.findAdj(grid, i, j + 1)
        self.findAdj(grid, i, j - 1)


solve = Solution()

solve.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])

solve.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
