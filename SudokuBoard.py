class SudokuBoard:

    def __init__(self, originalGrid = None):
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.unsolved = True
        if not(originalGrid is None):
            for x in range(0, 9):
                for y in range(0, 9):
                    self.grid[x][y] = originalGrid[x][y]

    def num_in_row(self, row, col, num):
        for y in range(0, 9):
            if y != col and self.grid[row][y] == num:
                return True
        return False

    def num_in_col(self, row, col, num):
        for x in range(0, 9):
            if x != row and self.grid[x][col] == num:
                return True
        return False

    def num_in_square(self, row, col, num):
        x = row - row % 3
        y = col - col % 3
        for i in range(0, 3):
            for n in range(0, 3):
                if (row != i+x or col != n+y) and self.grid[i+x][n+y] == num:
                    return True
        return False

    def find_empty_space(self, coordinate):
        for x in range(0, 9):
            for y in range(0, 9):
                if self.grid[x][y] == 0:
                    coordinate[0] = x
                    coordinate[1] = y
                    return False
        return True

    def set_value(self, row, col, num):
        self.grid[row][col] = num
