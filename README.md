# TicDabToe

## Description
● TicDabToe is an extension of the 4x4 Ultimate TicTacToe(which is an extension of 3x3
TicTacToe), where there are 16 blocks each having 4x4 cells.

● Each game is between two teams.

● At the beginning, a coin is flipped to decide the team which will move first (First player).

● The marker for the first player is ‘x’ and for the second player is ‘o’

● The objective of the game is to win the board by making a legitimate pattern of the
blocks.

● Note: This version of Intelligent TicTacToe is an extension of the original version of and
is different from it.


![Alt text](/ai1.png?raw=true "The Game")

## The Rules
1. [​ FIRST MOVE​ ] The very first move of the game is an open move, i.e. Any cell on the
entire board is valid.

2. [​ CORRESPONDENCE RULE​ ] If the opponent places his/her marker in any of the cells,
then you need to place your marker anywhere in the block corresponding to the cell.
For example, if a player places his marker in the top left cell of some block, the next
player needs to move in any of the open cells in the top left block. Similarly for the right
center cell, right center block is open. Please refer to the code for more clarity.

3. [​ ABANDON RULE​ ] Once a block is won by a player, it has to be abandoned. That is,
you may consider the entire block to be full and no other player may play in that block.

4. [​ FREE MOVE RULE​ ] In case all of the cells in the destined block obtained from Rule 2
are occupied or the destined block is abandoned as per Rule 3, then the player may
move in any free cell in the entire board.

5. [​ WIN RULE​ ] The player who wins any four consecutive cells in a block which are either
a row, column or diagonal wins the block and the player who wins any four
consecutive blocks of the board, wins the game and the game is over. If all the cells
are filled, and no pattern has been formed then the game is over.


![Alt text](/ai2.png?raw=true "Winning Patterns")


## Scoring
Winning a game, by forming a pattern as described in [WIN RULE] will give you
16 points.

If the player makes an invalid move, or exceeds time limit, or makes an illegal
change to the board, or uses threading or makes any system call, then the
opponent earns 16 points and the player earns 0 points.

If no player has a pattern at the end of the game, both the players get points
equal to the number of blocks they have won respectively.


