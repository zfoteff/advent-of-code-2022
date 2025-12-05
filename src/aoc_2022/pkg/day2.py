from typing import List


def import_puzzle_data(data_path) -> List[str]:
    with open(data_path) as f:
        puzzle_data = f.read().splitlines()
    return puzzle_data


def score_round(opponent_move: str, player_move: str = "", result: str = "") -> int:
    score = 0
    score_guide = {
        "WIN": 6,
        "DRAW": 3,
        "LOSS": 0,
        "ROCK": 1,
        "PAPER": 2,
        "SCISSORS": 3,
    }
    player_moves = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
    result_options = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}

    if len(result) > 0:
        # The user wants the results found by using the result of the game to determine the player's move
        if opponent_move == "A":
            if result_options[result] == "WIN":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["Y"]]
                )
            if result_options[result] == "DRAW":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["X"]]
                )
            if result_options[result] == "LOST":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["Z"]]
                )

        if opponent_move == "B":
            if result_options[result] == "WIN":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["X"]]
                )
            if result_options[result] == "DRAW":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["Y"]]
                )
            if result_options[result] == "LOST":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["Z"]]
                )

        if opponent_move == "C":
            if result_options[result] == "WIN":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["X"]]
                )
            if result_options[result] == "DRAW":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["Z"]]
                )
            if result_options[result] == "LOST":
                score = (
                    score_guide[result_options[result]] + score_guide[player_moves["Y"]]
                )

    else:
        # The user wants the results found by comparing two moves and finding the winner
        if opponent_move == "A" and player_move == "Y":
            score = score_guide["WIN"] + score_guide[player_moves[player_move]]
        if opponent_move == "A" and player_move == "Z":
            score = score_guide["LOSS"] + score_guide[player_moves[player_move]]
        if opponent_move == "B" and player_move == "X":
            score = score_guide["LOSS"] + score_guide[player_moves[player_move]]
        if opponent_move == "B" and player_move == "Z":
            score = score_guide["WIN"] + score_guide[player_moves[player_move]]
        if opponent_move == "C" and player_move == "X":
            score = score_guide["WIN"] + score_guide[player_moves[player_move]]
        if opponent_move == "C" and player_move == "Y":
            score = score_guide["LOSS"] + score_guide[player_moves[player_move]]
        else:
            # Else, return the score for a draw and the player's corresponding move
            score = score_guide["DRAW"] + score_guide[player_moves[player_move]]

    return score


def play_rock_paper_scissors(moves_list: List[str]) -> int:
    total_score = 0
    for move in moves_list:
        round_moves = move.split(" ")
        total_score += score_round(
            opponent_move=round_moves[0], player_move=round_moves[1]
        )
    return total_score


def play_cheater_rock_paper_scissors(moves_list: List[str]) -> int:
    total_score = 0
    for move in moves_list:
        round_moves = move.split(" ")
        total_score += score_round(opponent_move=round_moves[0], result=round_moves[1])
    return total_score
