# 15-puzzle-check

TLDR:
I created this because in all the years I've been playing around with the Fifteen Puzzle it had never occurred to me that there were patterns or configurations that were unsolvable. This little console app aims to determine just that - if an imagined configuration of the Fifteen Puzzle is indeed solvable. 

All you’ll need to do is input a list of numbers that represent the desired configuration you’re trying to solve for. I have taken some care to make sure the input will be validated before proceeding but, as they say, s#it happens. 

It’s probably best to draw a little diagram like this to keep track of which numbers you’ll need to input. Read/input each row starting from the top and moving from left to right; repeat for the next row below. The ‘blank space’ is entered as ‘16’. Put a space between each number and after typing the last number hit enter. 
```
- - - - - - - - - - - -  
|  1  |  5  | 9  | 13 |
- - - - - - - - - - - - 
|  2  |  6  | 10 | 14 | 
- - - - - - - - - - - - 
|  3  |  7  | 11 | 15 |
- - - - - - - - - - - - 
|  4  |  8  | 12 |    | 
- - - - - - - - - - - - 
```
For example this above diagram would be written as:
1 5 9 13 2 6 10 14 3 7 11 15 4 8 12 16

The input processed (and will be displayed as it is above with a 16 for the space) and you will see a few lines telling you about the puzzle just imputed. 
It will tell you the number of transpositions required to solve the puzzle, and it will tell you the parity of the solution. If these are matched then the configuration you entered is solvable. If tey don’t match then it isn’t solvable. 
Thank you for taking a look.   

Long version: 
The Fifteen Puzzle sits on my desk under my monitor, it has for years and still does. . . I pick it up and casually shuffle the tiles around until the solution presents itself. I find it calming and meditative. I’ve done various ‘solves’ for the puzzle; odds on top and evens on bottom, spirals, snakes etc. One fine day about a year ago I imagined this pattern: 
```
- - - - - - - - - - - - 
|  1  |  8  |  9 |    |
- - - - - - - - - - - - 
|  2  |  7  | 10 | 15 | 
- - - - - - - - - - - - 
|  3  |  6  | 11 | 14 |
- - - - - - - - - - - - 
|  4  |  5  | 12 | 13 | 
- - - - - - - - - - - - 
```
It seemed simple enough. . . I work at it for about 15 min and I can’t get the last 2 tiles (the 14 and the 15 or the 13 and the 14) to be in the right spot. OKAY I thought. Time to focus and get this done. About an HOUR goes by and I can’t get it. “Hmmm have I lost my touch?” I thought. So I did a standard solve and a few others without a problem. I try again - and the same result - I can’t get the ‘solve’ I was looking for. 

TO THE INTERNET ! 

I look for a ‘15 puzzle solver’ surely I must be doing something wrong to not be able to get this. I find various solvers that solve to the classic ‘1 through 15’ solution, but not much that looks like I’ll be able to input my own puzzle and have it solve it for me step by step. 
Searching continues… 

I soon learn about the history of the Fifteen Puzzle and how a mathematician in 1870 by the name of Sam Loyd issued a challenge (with a $1000 cash prize) to solve the Fifteen Puzzle in a different way such that 14 and the 15 tiles should be swapped. Only thing was he knew his $1000 would be safe because he knew it could not be solved. Ever. Mathematically impossible. 

It was through this research I found out that half of the possible configurations are not solvable. If you could simply put a tile anywhere you’d like without having to slide it in place there are 16! possibilities and half of them consist of illegal moves to get there - basically meaning that in a world confined to sliding tiles to swap positions, many patterns and designs we come up with are not solvable to begin with. 

So how then are we able to look at a puzzle and determine if we should bother trying to solve it? Why math of course. I won’t go into all the details here (and I don’t claim to be a skilled mathematician) but in essence you need to know 2 things: 
1.What the parity (ODD or EVEN) of the solution is to be 
2.How many moves or transpositions it will take to get to a given solution. 
If the number of transpositions is EVEN and the parity is EVEN, it’s solvable. Likewise if the number of transpositions is ODD and the parity is ODD, then it’s also solvable. If they are mismatched then the solution is not solvable. 

You can find the parity of a solution by looking at the ‘blank space’ or the ‘16th tile’. Where this is located relative to the ‘Natural’ or ‘Home’ configuration, which is in the lower right corner, will tell you if the desired configuration has an ODD or EVEN parity. This needs to match the number of transpositions to get the desired configuration back to the ‘Home’ configuration, otherwise known as the standard ‘1 through 15’ tile arrangement. If you can solve it in reverse you can solve from ‘Home’ to the desired configuration. 

This Home configuration can be written as a single list of numbers: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 (with 16 as the space). You may swap any 2 tiles and have a new list of numbers as a result. In the real world you can take as many moves/slides as you need too to swap these tiles but it still counts as ONE transposition. You repeat this until the tiles are all sorted in order. Sometimes a swap will put two tiles in the right place at once - that’s part of the natural solution and expected to happen. Other times a swap will chase a number back and forth a few times. That’s also part of the process. 

So there it is. After several months of digging and reading and trying I have made a little thing that allows me to know if a random 15 puzzle configuration I imagined is worth my time or not. I hope that someone else may find this useful. 

