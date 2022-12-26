__author__ = "zfoteff"

import time
from sys import exit
from typing import List

"""Advent of Code day 2
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack 
storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, 
the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, 
a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper
defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle 
input) that they say will be sure to help you win. "The first column is what your opponent is going 
to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is 
called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and 
Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of 
your scores for each round. The score for a single round is the score for the shape you selected (1 for 
Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if 
the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you 
would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win 
for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss 
for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the 
round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you 
need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so 
the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you 
also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score 
of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes 
exactly according to your strategy guide?
"""


def load_puzzle_data() -> List[str]:
    """Read puzzle input. Outputs the players' moves as a list of strings containing the opponent's 
    move seperated from the player's move by a space

    Returns:
        List[str]: List strings containing the opponent and the player's move
    """
    try:
        with open("data.txt") as f:
            puzzle_data = f.read().splitlines()
        return puzzle_data
    except FileNotFoundError as e:
        print(f"[-] Failed to load puzzle data. Reason: {str(e)}")
        exit(0)


def score_round(opponent_move: str, player_move: str = "", result: str = "") -> int:
    score_guide = {
        "WIN": 6,
        "DRAW": 3,
        "LOSS": 0,
        "ROCK": 1,
        "PAPER": 2,
        "SCISSORS": 3,
    }
    opponent_moves = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
    player_moves = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
    result_options = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}

    if len(result) > 0:
        # The user wants the results found by using the result of the game to determine the player's move
        if opponent_move == 'A':
            if result_options[result] == 'WIN':
                return score_guide[result_options[result]] + score_guide[player_moves['Y']]
            if result_options[result] == 'DRAW':
                return score_guide[result_options[result]] + score_guide[player_moves['X']]
            if result_options[result] == 'LOST':
                return score_guide[result_options[result]] + score_guide[player_moves['Z']]

        if opponent_move == 'B':
            if result_options[result] == 'WIN':
                return score_guide[result_options[result]] + score_guide[player_moves['X']]
            if result_options[result] == 'DRAW':
                return score_guide[result_options[result]] + score_guide[player_moves['Y']]
            if result_options[result] == 'LOST':
                return score_guide[result_options[result]] + score_guide[player_moves['Z']]
        
        if opponent_move == 'C':
            if result_options[result] == 'WIN':
                return score_guide[result_options[result]] + score_guide[player_moves['Z']]
            if result_options[result] == 'DRAW':
                return score_guide[result_options[result]] + score_guide[player_moves['Z']]
            if result_options[result] == 'LOST':
                return score_guide[result_options[result]] + score_guide[player_moves['Z']]

    else:
        # The user wants the results found by comparing two moves and finding the winner
        if opponent_move == "A" and player_move == "Y":
            return score_guide["WIN"] + score_guide[player_moves[player_move]]

        if opponent_move == "A" and player_move == "Z":
            return score_guide["LOSS"] + score_guide[player_moves[player_move]]

        if opponent_move == "B" and player_move == "X":
            return score_guide["LOSS"] + score_guide[player_moves[player_move]]

        if opponent_move == "B" and player_move == "Z":
            return score_guide["WIN"] + score_guide[player_moves[player_move]]

        if opponent_move == "C" and player_move == "X":
            return score_guide["WIN"] + score_guide[player_moves[player_move]]

        if opponent_move == "C" and player_move == "Y":
            return score_guide["LOSS"] + score_guide[player_moves[player_move]]

        # Else, return the score for a draw and the player's corresponding move
        return score_guide["DRAW"] + score_guide[player_moves[player_move]]


def play_rock_paper_scissors(moves_list: List[str]) -> int:
    """_summary_

    Args:
        moves_list (List[str]): _description_

    Returns:
        int: _description_
    """
    total_score = 0
    for move in moves_list:
        round_moves = move.split(" ")
        total_score += score_round(
            opponent_move=round_moves[0], player_move=round_moves[1]
        )
    return total_score


def play_cheater_rock_paper_scissors(moves_list: List[str]) -> int:
    """_summary_

    Args:
        moves_list (List[str]): _description_

    Returns:
        int: _description_
    """
    total_score = 0
    for move in moves_list:
        round_moves = move.split(" ")
        total_score += score_round(opponent_move=round_moves[0], result=round_moves[1])
    return total_score


def main() -> None:
    puzzle_data = load_puzzle_data()
    score = play_rock_paper_scissors(puzzle_data)
    print(f"[+] Tic Tac Toe round one score: {score}")
    cheater_score = play_cheater_rock_paper_scissors(puzzle_data)
    print(f"[+] Tic Tac Toe round two score: {cheater_score}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - start_time
    print(f"[+] Completed in {elapsed_time:.3f} seconds")
