
# Difficult_TicTacToe

----------

This is not any python TicTacToe. I codded my own algorithm to add hard modes. It currently Have two hard modes. Check it out and try to win against both two modes.

This is a simple TicTacToe with three modes. These modes are:

```
["Computer(dump) (vs) Player","Computer(Smart) (vs) Player",  "Player (vs) Player"]
```

1.  Player vs Player
    
2.  Computer(dumb)
    
3.  Computer(Smart)
    

So, i'm going to breakdown into each mode one by one.

## Player vs Player

This mode is one of the most simplest mode. This mode allows two player to play with each other. I used even and odd logic to determine the turn of each player.

## Computer(dumb)

This mode is more simpler then the Player vs Player. The logic of dumb computer is extremely simpler like very simple. It don't know about anything about tictactoe. It is brainless computer and just gives us random moves from all the available moves

## Computer(smart)

This is the mode that is smarter then the dumb computer and it might be smarter then you. Its logic is very linear. It just filter best move one by one from all the available moves. It's logic is not so great but I will try to improve it in future


## Basic Working

The dump computer just plays random moves as I discussed earlier. But the smart computer uses a little bit of strategy. The strategy that the smart computer uses is mix of offensive and deffensive strategy. Ai will use the self.wins list to for it's strategy in defensive and it will automatically detech that if the player is making nay move that is in the sellf.wins list. If player is trying to make any move then it will block it. But in the offensive strategy computer will try to make the move that are in self.wins


----------

This is the final version of the game so it might have many issues. If you find any issue just report it.