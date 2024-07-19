# A simple game of Tic Tac Toe
# Author: Ryan van Mastrigt

class board():
    # class that creates, alters, and shows the gameboard
    def __init__(self, row_no, col_no):
        # initialize an empty 3x3 board
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        # markers are X and O
        self.markers = ['X', 'O']
        # set the naming convention for rows (row_no) and columns (col_no)
        self.row_no = row_no
        self.col_no = col_no
    def print(self):
        # print the state of the board
        print(' \t' + self.row_no[0] + '\t    \t' + self.row_no[1] +'\t   \t' + self.row_no[2])
        for y, row in enumerate(self.board):
            print(self.col_no[y] + '\t' + row[0] + '\t | \t' + row[1] + '\t | \t' + row[2] + '\n')
            if y < 2:
                print('\t---------------------------------\n')
    def clear(self):
        # clear the board
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
    def place(self, location, player):
        # place the marker of player at location
        valid_move = True
        # if location is empty, place marker, else ask for a new move
        if self.board[location[0]][location[1]] == '':
            self.board[location[0]][location[1]] = self.markers[player-1]
        else:
            print('illegal move, try again')
            valid_move = False
        return valid_move
    def check_winner(self):
        # check if there is a winner
        game_over = False
        winner = -1
        # check the rows
        for row in self.board:
            # count the number of X and O per row
            count_X, count_O = self.counter(row)
            # if the number exceeds 2, there is a winner
            if count_X>2:
                game_over = True
                winner = 1
            if count_O>2:
                game_over = True
                winner = 2
        # check the columns
        for c in range(3):
            # count the number of X and O per column
            column = [self.board[i][c] for i in range(3)]
            count_X, count_O = self.counter(column)
            # if the number exceeds 2, there is a winner
            if count_X>2:
                game_over = True
                winner = 1
            if count_O>2:
                game_over = True
                winner = 2
        # check the diagonals
        diagonal = [self.board[0][0], self.board[1][1], self.board[2][2]]
        # count the number of X and O in the diagonal
        count_X, count_O = self.counter(diagonal)
        #if the number exceeds 2, there is a winner
        if count_X>2:
                game_over = True
                winner = 1
        if count_O>2:
            game_over = True
            winner = 2
        return game_over, winner
    def counter(self, list):
        # count the number of markers in list
        count_X = 0
        count_O = 0
        for i in list:
            if i == self.markers[0]:
                count_X += 1
            elif i == self.markers[1]:
                count_O += 1
        return count_X, count_O

class tictactoe():
    # run a game of Tic Tac Toe
    def __init__(self):
        # initialize the board with naming convention row_no and col_no
        self.row_no = ['1', '2', '3']
        self.col_no = ['A', 'B', 'C']
        self.board = board(self.row_no, self.col_no)
        print('Welcome to Tic Tac Toe!')
    def make_a_move(self, player):
        # allow player to place a marker
        valid_move = False
        while not valid_move:
            # ask the player for a location 
            print('player {:d}, please give the location for your next marker:'.format(player))
            string = str(input())
            # if the location is valid, make the move. Else return to start while loop
            try:
                x = self.col_no.index(string[0])
            except ValueError:
                print('invalid move, try again')
                continue
            try:
                y = self.row_no.index(string[1])
            except ValueError:
                print('invalid move, try again')
                continue
            valid_move = self.board.place([x, y], player)
        # print the board and check if there is a winner
        self.board.print()
        self.game_over, self.winner = self.board.check_winner()
    def run(self):
        # run the game
        # while repeat is True, game runs
        self.repeat = True
        while self.repeat:
            #start of the round, clear board
            self.board.clear()
            self.game_over = False
            self.winner = -1
            turn = 0
            print('player 1 is X, player 2 is O')
            while self.game_over == False:
                # while there is no winner, keep making moves
                if turn == 0:
                    self.board.print()
                if turn == 9:
                    #after 9 turns, no more markers can be placed and the game ends in a stalemate if the 9th move did not result in a winner
                    print("stalemate\n")
                    self.game_over = True
                    break
                # player switches each turn, player 1 always starts
                playing_player = turn % 2 + 1
                # ask the player to make a move
                self.make_a_move(playing_player)
                turn += 1
            if self.game_over:
                # if the game is over, announce winner if not stalemate and ask to play again
                if self.winner != -1:
                    # announce winner
                    print('game over, player {:d} won!\n'.format(self.winner))
                check_playagain=True
                while check_playagain:
                    # ask to play again
                    print('play again? \n')
                    print('y/n')
                    string = str(input())
                    if string == 'n':
                        # stop playing
                        print('Thanks for playing, goodbye')
                        self.repeat = False
                        check_playagain=False
                    elif string == 'y':
                        # play again, repeat remains True
                        print('starting new game')
                        check_playagain=False
                    elif string != 'y':
                        # invalid response, ask again
                        print('invalid string, please enter y or n')
        return 0
    
#initialize the game
game = tictactoe()
# run the game
game.run()


