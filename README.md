# Non-Euclidean-Tic-Tac-Toe
Tic-Tac-Toe is a boring game.  There's not much to visualize or think about, and thus the skill ceiling is very low.  Even a par Tic-Tac-Toe player should be able to never lose a single match.  But what if there were a way to add some spice to Tic-Tace-Toe.  What if you played it on a torus (aka Tic-Tac-Torus), hyperbola, or some other nightmare?  What if you could also spontaneously change the size of the board between every match?  This project attempts to answer those questions.

This project was created in a day, after learning about Tic-Tac-Torus in my Number Theory class.  I had attempted to play a friend on a six-by-six grid on paper, only to later discover that we could not confidently decide if someone won.  This program solves that issue, by dynamically finding all solutions for an n-by-n grid, and checking them for you.  But because this project was made under such a short time span, many short cuts were taken and there is much room for improvement.  Feel free to suggest any improvements/new ideas/new topographies!

## Current Features:
- Play Tic-Tac-Toe on a Torus
- Spontaneously change the board size to anything-- although realistically, anything after a ten-by-ten will start getting too small to play on.
- Turn indicator

## Possible Improvements
- More topographies-- spheres, hyperbola, klein bottle, etc.
- Some sort of timer
- Win counter/Ability to restart game

### An Interesting Problem
When trying to dynamically find all solutions for an n-by-n board, I initially had some difficulties.  My first thought was to consider a 3x3 board, and observe that the sum of any diagonal, straight or broken is constant:  
0|1|2  
3|4|5  
6|7|8  
  
0+4+8 = 2+4+6 = 0+5+7 = 1+5+6... = 12  
Indeed, for any n-by-n board, I found the sum of these diagonals to equal: n*(n-1)/2 + (n^2 * (n-1))/2
This follows from the fact that any n by n board can be written as  
0  |1   |2   |3...   |n-1  
n  |n+1 |n+2 |n+3... |2n-1  
2n |2n+1|2n+2|2n+3...|3n-1  
...  
(n^2)-n|(n^2)-n+1...  |(n^2)-1  
  
So one way to find every solution for an n-by-n board would be to find every set of n unique, positive integers which sum to the diagonal sum (with the further restriction that no integer be greater than (n^2)-1, the max value of a tic-tac-toe board).  This would have been hard to do, and I saw no easy way to implement such a solution, so I eventually found another method.  However, I find this to be an interesting problem, and would love to see any solutions that someone comes up with.
