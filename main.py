from tictactoe import TicTacToe


def print_options() -> None:
    """Prints all the options in vertical order

    Args:
        options (list[str]): the list that contains all the options
    """

    options: list[str] = [
        "Computer(dumb) (vs) Player",
        "Computer(Smart) (vs) Player",
        "Player (vs) Player",
    ]

    for index in range(len(options)):

        print(f"[{index+1}] {options[index]}")


def get_option() -> list[bool]:
    """Gets the input from the user ranging from 1-3

    Returns:
        str: options for mode
    """

    print_options()

    try:
        option: str = input("Enter option:> ")
    except KeyboardInterrupt:
        exit(0)

    computer = True
    dumb = True

    if option == "1":
        return [computer, dumb]

    if option == "2":
        dumb = False
    elif option == "3":
        computer = False
    else:
        print("Invalid option Please try again!")
        exit(0)

    return [computer, dumb]


arguments: bool = get_option()
computer = arguments[0]
dumb = arguments[1]

obj = TicTacToe()
obj.MainGameLoop(computer=computer, dumb=dumb)
