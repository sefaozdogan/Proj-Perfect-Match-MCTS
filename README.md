## INTRODUCTION

This game is being developed using Monte Carlo Tree Search. Monte Carlo Tree Search has one main purpose: given a game state to choose the most promising next move. 
We deal with an interactive situation in the game. There is interaction between two actors involved these are maker and breaker.
We can easily verify that in project, perfect matching game on k6 complete graph. This game is finite two person zero-sum sequential game. Sequential because players make their moves in sequence, one after another. Indeed, there are two players involved, there is always finite amount of moves a person may perform and the game is strictly competitive. The goals of both players are completely opposite, all games outcomes sum up to zero. That means in any terminal state of the game the sum of gains for all players equals zero.


## ARCHITECTURAL GOALS

MCTS is an algorithm that figures out the best move out of a set of moves by Selecting → Expanding → Simulating → Back-propagation the nodes in tree to find the final solution. This method is repeated until it reaches the solution and learns the policy of the game.

Perfect Matching Mechanism: A matching (M) of graph (G) is said to be a perfect match, if every vertex of graph g (G) is incident to exactly one edge of the matching (M).
Shown in this formula;
deg(V) = 1 ∀ V
The degree of each and every vertex in the subgraph should have a degree of 1.

The key abstractions related to the project are defined below; Perfect Matching,
Complete Graph: That is a graph that has an edge between every single vertex in the graph.
Combinatorial Game: A combinatorial game is a two-player game, where there is no hidden information or randomness.
