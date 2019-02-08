import numpy as np

from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from game import GameState

GAME_NUMBER = 100
GRAPH_SIZE = 6
SIMULATION_NUMBER = 20
MAKER = 1
BREAKER = -1

edges = list()
perfMatc = list()


def createEdges():
    edges.clear()
    for x in range(1, GRAPH_SIZE):
        for y in range(x):
            edges.append(str(x) + str(y))


def createPerfMatch():
    perfMatc.clear()
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            for k in range(j + 1, len(edges)):
                tmp = []
                if edges[i][0] not in edges[j] and edges[i][1] not in edges[j] \
                        and edges[i][0] not in edges[k] and edges[i][1] not in edges[k] \
                        and edges[j][0] not in edges[k] and edges[j][1] not in edges[k]:
                    tmp.append(edges[i])
                    tmp.append(edges[j])
                    tmp.append(edges[k])
                    perfMatc.append(tmp)


def move():
    for x in range(1, GRAPH_SIZE):
        for y in range(x):
            if c_board[x][y] == MAKER or c_board[x][y] == BREAKER:
                moving = str(x) + str(y)
                if moving in edges:
                    if c_board[x][y] == BREAKER:
                        plyr = "Breaker"
                    else:
                        plyr = "Maker"
                    # print("moving:", moving, "player:", plyr)
                    edges.remove(moving)
                    if c_board[x][y] == BREAKER:
                        for k, v in enumerate(perfMatc):
                            if moving in v:
                                perfMatc.remove(perfMatc[k])


makerWinCount = 0
breakerWinCount = 0

def judge(state):
    if state.is_game_over():
        global makerWinCount
        global breakerWinCount
        if state.game_result == MAKER:
            print("MAKER WIN!")
            makerWinCount += 1
        if state.game_result == BREAKER:
            print("BREAKER WIN!")
            breakerWinCount += 1
        print("breakerWinCount = ", breakerWinCount)
        print("makerWinCount = ", makerWinCount)
        print("-----------------------")
        return 1


def play(state, player):
    board_state = GameState(state=state, next_to_move=player, pmArray=perfMatc)
    root = MonteCarloTreeSearchNode(state=board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(SIMULATION_NUMBER)
    c_state = best_node.state
    c_board = c_state.board
    return c_state, c_board


def init():
    createEdges()
    createPerfMatch()
    state = np.zeros((GRAPH_SIZE, GRAPH_SIZE))
    c_state, c_board = play(state, MAKER)
    return c_state, c_board


for i in range(GAME_NUMBER):
    c_state, c_board = init()
    move()
    player = BREAKER
    while True:
        c_state, c_board = play(c_board, player)
        move()
        if player == MAKER:
            player = BREAKER
        else:
            player = MAKER
        if judge(c_state) == 1:
            break
