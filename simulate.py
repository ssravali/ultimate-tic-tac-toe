import game as *;
import agent as *;

class TicTacToeSimulator:
    def __init__(self, Agent1, Agent2):
        self.agent1 = Agent1;
        self.agent2 = Agent2;

    # play a single game and return the winner
    def playGame(self):
        state = startState();
        while not isEnd(state):
            if player(state) == 1:
                action = Agent1.getAction(state);
            elif player(state) == 2:
                action = Agent2.getAction(state);
            state = succ(state, action);

        return 1 if utility(state) > 0 else 2;

    # play n games and return the percentage of times Agent1 won
    def playGames(self, n):
        won = 0.0;
        for i in range(n):
            won += 1 if self.playGame() == 1 else 0;
        return won / n;
