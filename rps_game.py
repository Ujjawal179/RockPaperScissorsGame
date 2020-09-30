#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = input("Rock, paper, scissors? > ").lower()
        if choice == "rock":
            return choice
        elif choice == "paper":
            return choice
        elif choice == "scissors":
            return choice
        else:
            return self.move()


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1s = 0
        self.p2s = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.\nOpponent player played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print(u"\u001b[33m** YOU WIN **\u001b[0m")
            self.p1s += 1
        elif beats(move2, move1):
            print(u"\u001b[33m** OPPONENT PLAYER WINS **\u001b[0m")
            self.p2s += 1
        else:
            print("** TIE **")
        print(u"\u001b[35m"
              f"Your score: {self.p1s}\t Opponent's score: {self.p2s}"
              "\u001b[0m")

    def play_game(self):
        print(u"\u001b[1mGame start!\u001b[0m")
        for round in range(3):
            print(u"\u001b[34m"f"\nRound {round + 1}:\u001b[0m")
            self.play_round()
        print("Game over!")
        game.final_result()

    def final_result(self):
        if game.p1s > game.p2s:
            print(u"\u001b[32m\n** Great your guess is right \n Wow, you won ;-) **\n\u001b[0m")
        elif game.p1s == game.p2s:
            print(u"\u001b[33m\n** IT'S A TIE! **\n\u001b[0m")
        else:
            print(u"\u001b[31m\n** Better luck next time and answer was {n}. \n GAME OVER **\n\u001b[0m")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
