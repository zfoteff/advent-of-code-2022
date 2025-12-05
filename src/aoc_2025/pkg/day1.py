from typing import List
from math import floor


def import_puzzle_data(data_path: str) -> List[str]:
    with open(data_path) as f:
        data = [datum.strip() for datum in f.readlines()]
        return data


def adjust_dials_and_count_zeros(puzzle_input) -> int:
    dial_position = 50
    counter = 0

    for dial_adjustment_setting in puzzle_input:
        step = (
            int(dial_adjustment_setting[1:]) * -1
            if dial_adjustment_setting[0] == "L"
            else int(dial_adjustment_setting[1:])
        )

        dial_position = (dial_position + step) % 100

        if dial_position == 0:
            counter += 1

    return counter


def adjust_dials_and_count_passes_over_zero(puzzle_input) -> int:
    dial_position = 50
    counter = 0

    for dial_adjustment_setting in puzzle_input:
        step = (
            int(dial_adjustment_setting[1:]) * -1
            if dial_adjustment_setting[0] == "L"
            else int(dial_adjustment_setting[1:])
        )

        adjustment_result = abs(dial_position + step)

        if adjustment_result > 0:
            counter += floor(adjustment_result / 100)
        elif adjustment_result < 0:
            counter += floor(adjustment_result / 100)

        dial_position = (dial_position + step) % 100
    return counter
