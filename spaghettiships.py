import random

from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax


class Ship:
    def __init__(self, ship_size, begining, position_h_or_v):
        self.ship_size = ship_size
        self.begining = begining
        self.h_or_v = position_h_or_v


class Board:
    def __init__(self, *ai):
        self.board = [i for i in range(1, 26, 1)]
        if ai:
            self.get_random_ships();
        else:
            self.get_ships_from_input()

    def get_ships_from_input(self):
        placed_ships = 0
        while placed_ships < 3:
            self.print_board_numbers(self.board)
            beg = input("place begining on board")
            v_or_h = input("type v or h")
            ship = Ship(3, int(beg), v_or_h)
            if self.place_ship_on_board(ship):
                placed_ships += 1
        self.print_board_numbers(self.board)

    def are_coordinates_free(self, board, size, begin, h_v):
        if h_v == 'h':
            middle = begin + 1
            ending = begin + 1 + 1
        if h_v == 'v':
            middle = begin + 5
            ending = begin + 5 + 5
        statement1 = middle in board
        statement2 = begin in board
        statement3 = ending in board
        return statement1 and statement2 and statement3

    def place_ship_on_board(self, ship):
        if ship.begining in self.board:
            start = self.board.index(ship.begining)
            print(self.board.index(ship.begining))
            if ship.h_or_v == 'h':
                if start % 5 < ship.ship_size and self.are_coordinates_free(self.board, ship.ship_size, ship.begining,
                                                                            ship.h_or_v):
                    self.board[start] = 'o'
                    for i in range(ship.ship_size):
                        self.board[start + (i)] = 'o'
                    return True
            elif ship.h_or_v == 'v' and self.are_coordinates_free(self.board, ship.ship_size, ship.begining,
                                                                  ship.h_or_v):
                if start + (5 * (ship.ship_size - 1)) - 1 < len(self.board):
                    # self.board[start] = 'o'
                    for c in range(ship.ship_size):
                        self.board[(start) + 5 * c] = '0'
                    return True

    def print_anonimized_board(self, board):
        counter = 0
        for s in board:
            if isinstance(s, int):
                print("  ~", end='')
            else:
                print("  o", end='')
            counter = counter + 1
            if counter == 5:
                counter = 0
                print(" ")

    def print_board_numbers(self, board):
        counter = 0
        for s in board:
            # print(type(s))
            if isinstance(s, int) and s < 10:
                print("  ", s, "", end='')
            elif isinstance(s, str):
                print("   O ", end='')
            else:
                print(" ", s, "", end='')
            counter = counter + 1
            if counter == 5:
                counter = 0
                print(" ")


class SpaghettiShips(TwoPlayersGame):
    """ In turn, the players remove one, two or three bones from a
    pile of bones. The player who removes the last bone loses. """

    def __init__(self, players):
        self.players = players
        self.nplayer = 1  # player 1 starts
        self.players[0].board = Board()
        self.players[1].board = Board(ai)
## TO DO ##
    # def possible_moves(self): return [self.hunt, self.target]
    #
    # def make_move(self, move): self.pile -= int(move)  # remove bones.
    #
    # def win(self): return self.opponent.board  # opponent took the last bone ?
    #
    # def is_over(self): return self.win()  # Game stops when someone wins.
    #
    # def scoring(self): return 100 if self.win() else 0  # For the AI
### MAYBY USABLE MAYBY NOT
    # def hunt(self):
    #     guess = random.randint(0, 99)
    #     if guess in self.opponent.board:
    #         return guess
    #
    # def randomly_locate_ships(board):
    #     random.randint(0, 100)
    #
    # def ships_elements_left(list):
    #     return -1 in list


# Start a match (and store the history of moves when it ends)
ai = Negamax(13)  # The AI will think 13 moves in advance
game = SpaghettiShips([Human_Player(), AI_Player(ai)])
history = game.play()
