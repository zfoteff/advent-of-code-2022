#!/usr/bin/python3
import re
from typing import List


def import_puzzle_data(data_path: str) -> List[str]:
    with open(data_path) as f:
        return [datum.strip() for datum in f.readlines()]


def extract_mul_commands(puzzle_data: List[str]) -> int:
    offset = 0
    result = 0
    for message_str in puzzle_data:
        while True:
            # Find index of first mul( in remaining string
            start = message_str.find("mul(", offset, len(message_str))
            if start == -1:
                # If the string contains no more 'mul(' substrings, break
                break

            # Find closing )
            end = message_str.find(")", start, len(message_str))
            if end == -1:
                break

            message = message_str[start : end + 1]
            match = re.match("mul\(\d{,10},\d{,10}\)", message)

            if match is None:
                # If the match is malformed, move the offset forward a single space and continue parsing
                offset = start + 1
            else:
                # If there is a match with mul command, calculate result
                nums = list(map(int, message[4:-1].split(",")))
                result += nums[0] * nums[1]
                offset = end

        # Reset offset to end
        offset = 0
    return result


def part_two(puzzle_data: List[str]) -> int:
    return 0
