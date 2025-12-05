from typing import List


def import_puzzle_data(data_path: str) -> List[str]:
    with open(data_path) as f:
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
