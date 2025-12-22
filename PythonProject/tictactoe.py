class Tictactoe:


    def __init__(self):
        self.current_player = "X"
        self.board = [
            ["Empty", "Empty", "Empty"],
            ["Empty", "Empty", "Empty"],
            ["Empty", "Empty", "Empty"]
        ]
        self.winner = "none"
        # Initialize board data

    def start_board(self):
        self.winner = "none"
    
    def update_board(self, data: dict):
        for key in data["board"]:
            # Get coordinates from key
            coords = key.split(",")
            x = int(coords[0])
            y = int(coords[1])
            self.board[x][y] = data["board"][key]

    def is_valid_move(self, x: int, y: int):
        if self.board[x][y] != "Empty":
            return False
        else: 
            return True
        
    def check_game_end(self, r, c):
        row = int(r)
        col = int(c)
        board = self.board
        self.check_left_right(board, row)
        self.check_up_down(board, col)
        self.check_diagonals(board)
        if self.check_board_full(board) or self.winner != "none":
            return True
        return False


    def get_winner(self):
        return self.winner
    
    def check_left_right(self, board, row):
        player = board[row][0]
        if player == board[row][1] and player == board[row][2]:
            self.winner = player
        
    def check_up_down(self, board, col):
        player = board[0][col]
        if player == board[1][col] and player == board[2][col]:
            self.winner = player

    def check_diagonals(self, board):
        player = board[1][1]
        if player == board[0][0] and player == board[2][2] or player == board[0][2] and player == board[2][0]:
            if(player != "Empty"):             
                self.winner = player

    def check_board_full(self, board):
        for x in range(3):
            for y in range(3):
                if board[x][y] == "Empty":
                    return False
        return True
    

