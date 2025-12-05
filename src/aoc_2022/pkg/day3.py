from typing import List


def import_puzzle_data(data_path: str) -> List[str]:
    with open(data_path) as f:
        puzzle_data = f.read().splitlines()
    print(f"[+] Loaded puzzle data")
    return puzzle_data


def get_item_priority(rucksack_item: str) -> int:
    return (
        ord(rucksack_item) - 38 if rucksack_item.isupper() else ord(rucksack_item) - 96
    )


def count_item_priority(rucksack_items: List[str]) -> int:
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
