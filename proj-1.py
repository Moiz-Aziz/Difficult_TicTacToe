from TicTacToeAi import DumbAi
from random import shuffle


class TicTacToe(DumbAi):
    """
    Simple TicTacToe game with simple multiplayer
    """

    def __init__(self) -> None:

        # These are the essentials
        # these vars are used everywhere throughout the program
        self.board: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # We have two players which are X and O
        self.players: list[str] = ["O", "X"]

        # this is the self.win list that it have two uses
        # the first use of this list is to check if someone won or not
        # the second purose of this list is that computer uses it to use it's strategy

        self.wins: list[list[int]] = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        shuffle(self.players)

    def PrintBoard(self) -> None:
        """Just prints the boring board"""

        print(f" {self.board[0]}  | {self.board[1]} |  {self.board[2]}")
        print(f"----|---|----")
        print(f" {self.board[3]}  | {self.board[4]} |  {self.board[5]}")
        print(f"----|---|----")
        print(f" {self.board[6]}  | {self.board[7]} |  {self.board[8]}")

    def ChedefckUserInput(self, user: int, player: str) -> list:
        """Just checks is in range or not"""
        condition: bool = True
        if user <= 9 and user >= 1:
            condition = False
        else:
            print("Invalid value! Value should be between 1-9")

        return [user, condition]

    def CheckBoard(self, user: int, player: str) -> int:
        """checks if the place is already taken or not and if place is empty then it fills it"""

        if self.board[user] != self.players[0] and self.board[user] != self.players[-1]:

            self.FillBoard(user=user, player=player)
            return 0

        else:
            print("Place is already taken!")
            return 1

    def FillBoard(self, user: int, player: str) -> None:

        # Here the player is 'X' or 'O'
        self.board[user] = player

    def ChoosePlayer(self, tries: int) -> str:
        """This function determines the turn each player"""
        return self.players[tries % 2]

    def checkWins(self, player: str) -> bool:
        """This function checks who won the game"""

        # These vars determine who won the game
        checkX = 0
        checkO = 0

        for firstRow in range(len(self.wins)):

            for secondRow in self.wins[firstRow]:

                if self.board[secondRow] == "X":
                    checkX += 1
                    checkO = 0
                elif self.board[secondRow] == "O":
                    checkX = 0
                    checkO += 1
                else:
                    checkX = 0
                    checkO = 0

            if checkX >= 3 or checkO >= 3:
                displayedPlayer = "X" if player == "O" else "O"
                print(f"Player-{displayedPlayer} Won the game!")
                return True

        return False

    def CheckDraw(self, tries: int, player) -> bool:
        """This function decide if game is over or game is draw"""
        if self.checkWins(player=player):
            print("Gameover!")
            return True

        if tries == -9:
            print("Result: Draw")
            return True

    def DecideUserVsComputer(self, computer: bool, player: str, dumb: bool) -> str:
        """This function decide who has the next move."""

        # If use has selected the computer move then we we have two computer options
        # so we will decide which computer to use depending upon the dumb value
        if computer and player == "O":

            if dumb:
                user = self.LittleDumbAi(self.board)
            else:
                user = self.NotSoDumbAi()
        else:
            user: int = self.GetUserInput(player)

        return user

    def MainGameLoop(self, computer: bool = False, dumb=True) -> None:
        """
        This is the main game loop
        """

        tries: int = 0
        running: bool = True

        while running:

            # Each player have 50% luck to get the first chance
            player: str = self.ChoosePlayer(tries)
            self.PrintBoard()

            # After each move we will check that if someone won or not
            if self.checkWins(player=player) or self.CheckDraw(
                tries=tries, player=player
            ):
                running = False
                continue

            # Now we will get the value of user it may be person or a computer
            user: int = self.DecideUserVsComputer(
                computer=computer, player=player, dumb=dumb
            )

            # This function checks that if the place is taken or not
            check: int = self.CheckBoard(user=user, player=player)

            tries += check - 1

    def GetUserInput(self, player: str) -> int:

        # Now this function gets the input from the user
        running: bool = True
        while running:
            try:
                user = int(input(f"(Player-{player}) Enter your value (1-9): "))
                userVal = self.ChedefckUserInput(user=user, player=player)

                running = userVal[-1]

            except ValueError:
                print("Invalid input! Please enter an integer ranging between 1-9")

            except KeyboardInterrupt:
                exit()

        # we will subtract 1 from the user input to get the index in the board
        return userVal[0] - 1


# this function is not related to the program. This func is temp for the class testing
# You can also modify the main menu
#


def Menu() -> None:

    options: str = [
        "Computer(dumb) (vs) Player",
        "Computer(Smart) (vs) Player",
        "Player (vs) Player",
    ]

    computer = False
    dump = None

    while True:

        for i in range(len(options)):

            print(f"[{i+1}] {options[i]}")

        option = input("Enter your option: ")

        if option == "1":
            computer = True
            dump = True
        elif option == "2":
            computer = True
            dumb = False
        elif option == "3":
            computer = False
        else:
            print("Invalid option Please try again!")
            continue

        obj = TicTacToe()

        obj.MainGameLoop(computer=computer, dumb=dump)

        againOption = input("Do you want to play again: (y/n): ")

        if againOption != "y":
            break


Menu()
