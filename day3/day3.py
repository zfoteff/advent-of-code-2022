__author__ = "zfoteff"

import time
from sys import exit
from typing import List


def load_puzzle_data() -> List[str]:
    try:
        with open("data.txt") as f:
            puzzle_data = f.read().splitlines()
        print(f"[+] Loaded puzzle data")
        return puzzle_data
    except FileNotFoundError as e:
        print(f"[-] Failed to load puzzle data. Reason: {str(e)}")
        exit(0)


def get_item_priority(rucksack_item: str) -> int:
    return (
        ord(rucksack_item) - 38 if rucksack_item.isupper() else ord(rucksack_item) - 96
    )


def count_item_priority(rucksack_items: List[str]) -> int:
    # Part 1
    item_priorities = 0

    for item in rucksack_items:
        midpoint = int(len(item) / 2)
        compartment_1 = set(item[0:midpoint])
        compartment_2 = set(item[midpoint:])

        shared_item = compartment_1 & compartment_2
        if len(shared_item) > 0:
            item_priorities += get_item_priority(shared_item.pop())

    return item_priorities


def count_badge_priority(rucksack_items: List[str]) -> int:
    # Part 2
    badge_priorities = 0
    items = enumerate(rucksack_items)

    for index, _ in items:
        if index % 3 == 0:
            shared_item = (
                set(rucksack_items[index - 3])
                & set(rucksack_items[index - 2])
                & set(rucksack_items[index - 1])
            )
            badge_priorities += get_item_priority(shared_item.pop())

    return badge_priorities


def main() -> None:
    puzzle_data = load_puzzle_data()
    item_priority = count_item_priority(puzzle_data)
    print(f"[+] Item priority sum: {item_priority}")
    badge_priority = count_badge_priority(puzzle_data)
    print(f"[+] Badge priority sum: {badge_priority}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - start_time
    print(f"[+] Completed in {elapsed_time:.3f} seconds")
