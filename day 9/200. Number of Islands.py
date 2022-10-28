# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid) -> int:
        self.grid = grid
        row, col = len(grid), len(grid[0])
        self.visited = set()

        lands = 0
        for r in range(row):
            for c in range(col):
                lands += int(self.visit(r, c))
        # print (self.visited)
        return lands


    def visit(self, row, col):
        land = self.grid[row][col] == "1"
        if (row, col,) in self.visited or land is False:
            return False

        self.visited.add((row, col,))
        if row < (len(self.grid) - 1):
            land |= self.visit(row + 1, col)
        if row > 0:
            land |= self.visit(row - 1, col)
        if col < (len(self.grid[0]) - 1):
            land |= self.visit(row, col + 1)
        if col > 0:
            land |= self.visit(row, col - 1)
        
        return land

