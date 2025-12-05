from typing import Callable
from time import perf_counter

SPACER = "=" * 16


def timed_advent_of_code_runner(
    name: str,
    data_path: str,
    part_one_function: Callable[..., int],
    part_two_function: Callable[..., int],
    import_puzzle_function: Callable[..., int],
) -> None:
    start_time = perf_counter()

    puzzle_data_start_time = perf_counter()

    try:
        puzzle_data = import_puzzle_function(data_path)
    except FileNotFoundError:
        puzzle_load_time = perf_counter() - puzzle_data_start_time
        print(f"{SPACER} Unable to load puzzle data for {name} {SPACER}")
        return

    puzzle_load_time = perf_counter() - puzzle_data_start_time

    part_one_start_time = perf_counter()
    part_one_result = part_one_function(puzzle_data)
    part_one_end_time = perf_counter() - part_one_start_time

    part_two_start_time = perf_counter()
    part_two_result = part_two_function(puzzle_data)
    part_two_end_time = perf_counter() - part_two_start_time

    elapsed_time = perf_counter() - start_time

    result_message = f"""
Part one result [{part_one_end_time*1000:.4f} ms]: {part_one_result}
Part two result [{part_two_end_time*1000:.4f} ms]: {part_two_result}

Loaded puzzle data: {puzzle_load_time*1000:.4f} ms
Total elapsed time: {elapsed_time*1000:.4f} ms
    """
    print(f"{SPACER} {name} {SPACER}\n{result_message}")
