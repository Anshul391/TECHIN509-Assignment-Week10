class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def add_horizontal(self):
        print(f""" ---""", end="")
    def next_line(self):
        print()
    def add_vertical(self, char):
        print(f"| {char} ", end="")

    def draw_board(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                self.add_horizontal()
            self.next_line()
            for y in range(len(self.grid[0])):
                self.add_vertical(self.grid[x][y])
            print("|")
        for y in range(len(self.grid[0])):
                self.add_horizontal()
        self.next_line()

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == ('X' or 'O'):
                print(f'{self.grid[i][1]} won (Horizontal)')
                return True
            elif self.grid[1][i] == self.grid[2][i] == self.grid[0][i] == ('X' or 'O'):
                print(f"{self.grid[1][i]} won (Vertical)")
                return True
            if i == 0:
                if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == ('X' or 'O'):
                    print(f"{self.grid[0][0]} won Diagonal A")
                    return True
                elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == ('X' or 'O'):
                    print(f"{self.grid[1][1]} won Diagonal B")
                    return True

    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)
