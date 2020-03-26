from SudokuBoard import SudokuBoard


class User:
    def __init__(self, username):
        self.username = username
        self.easy_solved = 0
        self.medium_solved = 0
        self.hard_solved = 0
        self.sb = SudokuBoard()
        self.csb = None
        self.logged_in = True
        self.solving = False

    def logout(self):
        self.logged_in = False

    def login(self):
        self.logged_in = True

    def copy_sb(self):
        if self.csb is None:
            self.csb = SudokuBoard(self.sb.grid)
        return self.csb

    def reset_boards(self):
        self.csb = None

    def is_solving(self):
        if not self.solving:
            self.solving = True
            return False
        return True
