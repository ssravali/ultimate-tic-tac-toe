from game import *
from agent import *

class TicTacToeSimulator:
    def __init__(self, agent1, agent2):
        self.agent1 = agent1;
        self.agent2 = agent2;

    # play a single game and return the winner
    def playGame(self):
        state = startState();
        while not isEnd(state):
            printBoard(state[0]);
            print state[1], state[2];
            print;
            assert(player(state) >= 0 and player(state) <= 1);
            if player(state) == 1:
                action = self.agent1.getAction(state);
            else:
                action = self.agent2.getAction(state);
            print action;
            state = succ(state, action);
        return utility(state);

    # play n games and return the percentage of times agent1 won
    def playGames(self, n):
        won = 0.0;
        for i in range(n):
            won += 1 if self.playGame() == 1 else 0;
        return won / n;
