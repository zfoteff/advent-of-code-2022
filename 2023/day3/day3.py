#!/usr/bin/env python3
from time import perf_counter
from typing import List

"""
--- Part 1 ---
The engine schematic (your puzzle input) consists of a visual representation of
the engine. There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally, is a "part
number" and should be included in your sum. (Periods (.) do not count as a
symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number
is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all
of the part numbers in the engine schematic?
"""


def import_puzzle_data() -> List[str]:
    """Import puzzle data in a format best suited for the code challenge"""
    with open("puzzle-data.txt") as f:
        return [datum.strip().replace("\n", "") for datum in f.readlines()]


def is_symbol(character: str) -> bool:
    # Determine if a char is a symbol. For this problem, '.' does not count as a symbol
    return not (character.isnumeric() or character.isalpha() or character == ".")


def construct_full_digit(
    symbol_line_number: int, symbol_column_number: int, puzzle_input: List[str]
) -> int:
    # Expand left and right edges of substring until the next character is not a number
    left_edge_offset = 0
    right_edge_offset = 0

    while True:
        left_edge_found = True
        right_edge_found = True

        if puzzle_input[symbol_line_number][
            symbol_column_number - left_edge_offset - 1
        ].isnumeric():
            left_edge_offset -= 1
            left_edge_found = False

        if puzzle_input[symbol_line_number][
            symbol_column_number + right_edge_offset + 1
        ].isnumeric():
            right_edge_offset += 1
            right_edge_found = False

        if left_edge_found and right_edge_found:
            print(puzzle_input[symbol_line_number][left_edge_offset:right_edge_offset])
            return int(
                puzzle_input[symbol_line_number][left_edge_offset:right_edge_offset]
            )


def get_adjacent_numbers_to_symbol(
    symbol_line_number: int, symbol_column_number: int, puzzle_input: List[str]
) -> List[int]:
    adjacents = list()

    if puzzle_input[symbol_line_number - 1][symbol_column_number - 1].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number - 1, symbol_column_number - 1, puzzle_input
            )
        )
    if puzzle_input[symbol_line_number - 1][symbol_column_number].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number - 1, symbol_column_number, puzzle_input
            )
        )
    if puzzle_input[symbol_line_number - 1][symbol_column_number + 1].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number - 1, symbol_column_number + 1, puzzle_input
            )
        )
    if puzzle_input[symbol_line_number][symbol_column_number - 1].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number, symbol_column_number - 1, puzzle_input
            )
        )
    if puzzle_input[symbol_line_number][symbol_column_number + 1].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number, symbol_column_number + 1, puzzle_input
            )
        )
    if puzzle_input[symbol_line_number + 1][symbol_column_number - 1].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number + 1, symbol_column_number - 1, puzzle_input
            )
        )
    if puzzle_input[symbol_line_number + 1][symbol_column_number].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number + 1, symbol_column_number, puzzle_input
            )
        )
    if puzzle_input[symbol_line_number + 1][symbol_column_number + 1].isnumeric():
        adjacents.append(
            construct_full_digit(
                symbol_line_number + 1, symbol_column_number + 1, puzzle_input
            )
        )

    return adjacents


def get_gear_ratios(puzzle_input: List[str]) -> int:
    ratio = 0

    for line_number, line in enumerate(puzzle_input):
        for column_number, character in enumerate(line):
            if is_symbol(character):
                ratio += sum(
                    get_adjacent_numbers_to_symbol(
                        line_number, column_number, puzzle_input
                    )
                )

    return ratio


def main():
    start_time = perf_counter()

    # --- Load Puzzle Data ---
    puzzle_load_start_time = perf_counter()
    puzzle_data = import_puzzle_data()
    puzzle_load_end_time = perf_counter() - puzzle_load_start_time

    # --- Part 1 ---
    part_one_start_time = perf_counter()
    part_one_result = get_gear_ratios(puzzle_data)
    part_one_end_time = perf_counter() - part_one_start_time

    # --- Part 2 ---
    part_two_start_time = perf_counter()
    part_two_result = 0
    part_two_end_time = perf_counter() - part_two_start_time

    elapsed_time = perf_counter() - start_time

    print(
        f"Part one result [{part_one_end_time:.5f} ms]: {part_one_result}"
        + f"\nPart two result [{part_two_end_time:.5f} ms]: {part_two_result}\n"
        + f"\nLoaded puzzle data: {puzzle_load_end_time:.5f} ms."
        + f"\nTotal elapsed time: {elapsed_time:.5f} ms"
    )


if __name__ == "__main__":
    main()
