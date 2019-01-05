from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from game import GameState

def createEdges():
    for i in range(1, 6):
        for j in range(i):
            edges.append(str(i) + str(j))


def createPerfMatch():
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


def hamle():
    for i in range(1, 6):
        for j in range(i):
            if c_board[i][j] == 1 or c_board[i][j] == -1:
                hamle = str(i) + str(j)
                if hamle in edges:
                    if c_board[i][j]==-1:
                        plyr="Breaker"
                    else:
                        plyr = "Maker"
                    #print("hamle:", hamle, "oyuncu:", plyr)
                    edges.remove(hamle)
                    if c_board[i][j] == -1:
                        for k, v in enumerate(perfMatc):
                            if hamle in v:
                                perfMatc.remove(perfMatc[k])

maker = 0
breaker = 0

def judge(state):
    if state.is_game_over():
        global maker
        global breaker
        if state.game_result == 1.0:
            print("MAKER WIN!")
            maker += 1
            print("breaker=", breaker)
            print("maker=", maker)
            print("-----------------------")
        if state.game_result == -1.0:
            print("BREAKER WIN!")
            breaker += 1
            print("breaker=", breaker)
            print("maker=", maker)
            print("-----------------------")

        return 1

#Oynayacagı oyun sayısı
for i in range(100):
    edges = []
    perfMatc = []

    def init():
        createEdges()
        createPerfMatch()

        state = np.zeros((6, 6))
        initial_board_state = GameState(state=state, next_to_move=1, pmArray=perfMatc)
        root = MonteCarloTreeSearchNode(state=initial_board_state, parent=None)
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(200)
        c_state = best_node.state
        c_board = c_state.board
        return c_state, c_board


    c_state, c_board = init()
    hamle()
    player = -1

    while True:
        board_state = GameState(state=c_board, next_to_move=player, pmArray=perfMatc)
        root = MonteCarloTreeSearchNode(state=board_state, parent=None)
        mcts = MonteCarloTreeSearch(root)
        best_node = mcts.best_action(200)
        c_state = best_node.state
        c_board = c_state.board
        hamle()
        if player == 1:
            player = -1
        else:
            player = 1

        if judge(c_state) == 1:
            break