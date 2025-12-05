from typing import List, Tuple

import re

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


def import_puzzle_data(data_path) -> List[str]:
    with open(data_path) as f:
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


def determine_sum_of_game_ids_with_valid_games(games: List[Game]) -> int:
    """Determine which games in the provided puzzle input meet the provided set of cubes"""
    return sum(list(map(lambda game: is_valid_game(game), games)))


def determine_minimum_amount_of_cubes_for_valid_game(games: List[Game]) -> int:
    """Determine the minimum amount of cubes required to make the game valid"""
    return sum(list(map(lambda game: get_power_of_minimum_cube_set(game.games), games)))
