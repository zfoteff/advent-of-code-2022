#!/usr/bin/env python3.11

from typing import List, Tuple


def import_puzzle_data(data_path: str) -> List[Tuple[str, ...]]:
    with open(data_path) as f:
        return [datum for datum in f.readlines()]


def part_one(puzzle_input: List[str]) -> int:
    return 0


def part_two(puzzle_input: List[str]) -> int:
    return 1
