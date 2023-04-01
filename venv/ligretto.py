import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import seaborn as sns


class ScoreInputTerminal:
    def __init__(self, player_name, round_number):
        self.player_name = player_name
        self.round_number = round_number
        self.score = None
        print(f"Enter score for {self.player_name} in round: {self.round_number}")
        while True:
            score_str = input("Score: ")
            try:
                self.score = int(score_str)
                break
            except ValueError:
                print("Score must be an integer")


class Ligretto:
    def __init__(self):
        self.players = []
        self.round_number = 1

    def add_player(self, name, color):
        self.players.append(Player(name, color))

    def play_round(self):
        for player in self.players:
            score_input_terminal = ScoreInputTerminal(player.name, self.round_number)
            if score_input_terminal.score is None:
                return  # user cancelled input, end the round
            player.add_score(score_input_terminal.score)
        self.round_number += 1

    def plot_scores(self):
        sns.set_style("whitegrid")
        fig, ax = plt.subplots(figsize=(8, 6))
        for player in self.players:
            ax.plot(player.scores, color=player.color, label=player.name, linewidth=2)
        ax.set_xlabel("Round number")
        ax.set_ylabel("Total score")
        ax.set_title("Ligretto Scores")
        ax.legend(loc='best')
        plt.show()


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.scores = [0]

    def add_score(self, score):
        total_score = self.scores[-1] + score  # add new score to previous score
        self.scores.append(total_score)  # append new total score to list

if __name__ == "__main__":
    game = Ligretto()
    while True:
        add_player = input("Do you want to add another player? (y/n)")
        if add_player == "y":
            name = input("Enter player name: ")
            color = input("Enter player color: ")
            game.add_player(name, color)
        else:
            break

    while True:
        game.play_round()
        game.plot_scores()

