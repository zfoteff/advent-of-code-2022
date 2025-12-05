from typing import List, Tuple


def import_day_1_puzzle_data(data_path: str) -> List[str]:
    with open(data_path) as f:
        data = [datum.strip() for datum in f.readlines()]
        return data


def _adjust_dial_position(
    dial_adjustment_setting: str, dial_location: int
) -> Tuple[str, int]:
    step = (
        int(dial_adjustment_setting[1:]) % 100 * -1
        if dial_adjustment_setting[0] == "L"
        else int(dial_adjustment_setting[1:]) % 100
    )
    if dial_location + step > 99:
        dial_location = 0 - (100 - dial_location) + step
    elif dial_location + step < 0:
        dial_location = 100 - (step + dial_location)
    else:
        dial_location = dial_location + step

    return dial_location


def adjust_dials_and_count_zeros(puzzle_input) -> int:
    dial_position = 50
    counter = 0

    for puzzle_data in puzzle_input:
        dial_position = _adjust_dial_position(puzzle_data, dial_position)

        if dial_position == 0:
            counter += 1

    return counter

    # return sum(
    #     list(
    #         map(
    #             lambda step_value: 1 if step_value[1] == 0 else 0,
    #             list(
    #                 map(
    #                     lambda puzzle_data: _adjust_dial_and_return_position(
    #                         puzzle_data, dial_value
    #                     ),
    #                     puzzle_input,
    #                 )
    #             ),
    #         )
    #     )
    # )


def part_two(puzzle_input) -> int:
    pass


print(
    adjust_dials_and_count_zeros(
        import_day_1_puzzle_data("../data/day-1-puzzle-data.txt")
    )
)
