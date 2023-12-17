#!/usr/bin/env python


from time import perf_counter
from typing import List, Tuple

import re

"""
--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""
CUBE_SET = (12, 13, 14)


class Game:
    def __init__(self, game_id: str, game_string: str):
        self.__id = int(re.sub("[a-zA-Z]", "", game_id).strip())
        self.__games = list(
            map(
                lambda game_string: self._create_game_tuple(game_string),
                [game.split(",") for game in game_string.split(";")],
            )
        )

    def _create_game_tuple(self, cube_set_strings) -> Tuple:
        color = [0, 0, 0]

        for cube_set in cube_set_strings:
            if "red" in cube_set:
                color[0] = int(re.sub("[a-zA-Z]", "", cube_set).strip())
            if "green" in cube_set:
                color[1] = int(re.sub("[a-zA-Z]", "", cube_set).strip())
            if "blue" in cube_set:
                color[2] = int(re.sub("[a-zA-Z]", "", cube_set).strip())

        return tuple(color)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def games(self) -> List[Tuple]:
        return self.__games


def import_puzzle_data() -> List[str]:
    """Import puzzle data in a format best suited for the code challenge"""
    with open("puzzle-data.txt") as f:
        return [datum.strip().replace("\n", "") for datum in f.readlines()]


def is_valid_game(game: Game, cube_set: Tuple = CUBE_SET) -> int:
    """Determine if a game is valid.
    A game is valid if the each cube does not exceed its amount in the cube set, and
    the total amount of cubes in each game does not exceed the total amount in the cube set

    return the game id if valid game, 0 otherwise
    """
    r, g, b = cube_set
    cube_set_total_cubes = r + g + b

    for cubes in game.games:
        R, G, B = cubes
        if (R + G + B) > cube_set_total_cubes:
            return 0
        if R > r:
            return 0
        if G > g:
            return 0
        if B > b:
            return 0

    return game.id


def get_power_of_minimum_cube_set(cube_sets: List[Tuple]) -> int:
    """Determine the minimum amount of cubes required to make a game valid, given a game's cube set"""
    minimum_valid_cube_set = [0, 0, 0]

    for cubes in cube_sets:
        R, G, B = tuple(cubes)
        if R > minimum_valid_cube_set[0]:
            minimum_valid_cube_set[0] = R
        if G > minimum_valid_cube_set[1]:
            minimum_valid_cube_set[1] = G
        if B > minimum_valid_cube_set[2]:
            minimum_valid_cube_set[2] = B

    r, g, b = tuple(minimum_valid_cube_set)
    return r * g * b


def determine_sum_of_game_ids_with_valid_games(
    games: List[Game], cube_set: Tuple = CUBE_SET
) -> int:
    """Determine which games in the provided puzzle input meet the provided set of cubes"""
    return sum(list(map(lambda game: is_valid_game(game), games)))


def determine_minimum_amount_of_cubes_for_valid_game(games: List[Game]) -> int:
    """Determine the minimum amount of cubes required to make the game valid"""
    return sum(list(map(lambda game: get_power_of_minimum_cube_set(game.games), games)))


def main():
    start_time = perf_counter()

    # --- Load Puzzle Data ---
    puzzle_data = import_puzzle_data()
    games = (data.strip().split(":") for data in puzzle_data)
    game_list = [Game(game_id, game_string) for game_id, game_string in games]
    puzzle_load_time = perf_counter() - start_time

    # --- Part 1 ---
    part_one_start_time = perf_counter()
    part_one_result = determine_sum_of_game_ids_with_valid_games(game_list)
    part_one_end_time = perf_counter() - part_one_start_time

    # --- Part 2 ---
    part_two_start_time = perf_counter()
    part_two_result = determine_minimum_amount_of_cubes_for_valid_game(game_list)
    part_two_end_time = perf_counter() - part_two_start_time

    elapsed_time = perf_counter() - start_time

    print(
        f"Part one result [{part_one_end_time:.5f} ms]: {part_one_result}"
        + f"\nPart two result [{part_two_end_time:.5f} ms]: {part_two_result}"
        + f"\n\nLoaded puzzle data: {puzzle_load_time:.5f} ms.\nTotal elapsed time: {elapsed_time:.5f} ms"
    )


if __name__ == "__main__":
    main()
