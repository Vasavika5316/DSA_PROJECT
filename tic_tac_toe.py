class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_player = 'X'  # Player 'X' starts the game

    def print_board(self):
        print("-------------")
        for i in range(3):
            print(f"| {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} |")
            print("-------------")

    def is_valid_move(self, position):
        # Check if the chosen position is within the board range and the cell is empty
        return 0 <= position < 9 and self.board[position] == ' '

    def make_move(self, position):
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'  # Toggle player turn
        else:
            print("Invalid move! Please choose an empty position within 1-9.")

    def check_winner(self):
        # Define winning combinations (indices for rows, columns, and diagonals)
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]]) and (self.board[condition[0]] != ' '):
                return self.board[condition[0]]  # Return the winning player ('X' or 'O')
        if ' ' not in self.board:
            return 'Draw'  # Game ends in a draw if the board is full
        return None  # Game is ongoing

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Player 'X' goes first. Enter a number from 1-9 to place your mark.")

        while True:
            self.print_board()
            try:
                position = int(input(f"Player '{self.current_player}', enter your move (1-9): ")) - 1
                if self.is_valid_move(position):
                    self.make_move(position)
                    winner = self.check_winner()
                    if winner:
                        self.print_board()
                        if winner == 'Draw':
                            print("It's a draw!")
                        else:
                            print(f"Player '{winner}' wins!")
                        break
                else:
                    print("Invalid input or position is already taken! Please try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number (1-9).")

# Example usage:
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
