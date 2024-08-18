class Solution:
    def SolveSudoku(self, grid):
        unsolved = []
        for x in range(9):
            for y in range(9):
                if not grid[x][y]:
                    unsolved.append((x, y))

        index = 0
        while 0 <= index < len(unsolved):
            x, y = unsolved[index]
            
            grid[x][y] += 1
            if grid[x][y] > 9:
                grid[x][y] = 0 
                index -= 1
                continue
            
            if self.checkLegal(grid, x, y):
                index += 1
        
        return index >= 0
            
        
        
    def checkLegal(self, grid, x, y):
        num = grid[x][y]
        # row and col
        for i in range(9):
            if i != y and grid[x][i] == num:
                return False
            if i != x and grid[i][y] == num:
                return False      
        # box
        box = (x // 3, y // 3)
        for bx in range(box[0] * 3, box[0] * 3 + 3):
            for by in range(box[1] * 3, box[1] * 3 + 3):
                if (bx, by) != (x, y) and grid[bx][by] == num:
                    return False 
        return True
        
    
    def printGrid(self, arr):
        arr = sum(arr, [])
        arr = map(str, arr)
        print(" ".join(arr))

grid = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9]
]

ans = Solution().SolveSudoku(grid)
print(ans)