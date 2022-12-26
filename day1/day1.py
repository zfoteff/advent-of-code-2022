__author__ = 'zfoteff'

import time
from sys import exit
from typing import List

"""Advent of Code day 1
The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the 
Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking 
inventory of their supplies. One important consideration is food - in particular, the number of 
Calories each Elf is carrying (your puzzle input).
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, 
etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the 
previous Elf's inventory (if any) by a blank line. For example, suppose the Elves finish writing their 
items' Calories and end up with the following list:
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
This list represents the Calories of the food carried by five Elves:
The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to 
know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this 
is 24000 (carried by the fourth Elf).
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying 
the most Calories of food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the 
top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they 
still have two backups.
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 
11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three 
elves is 45000.
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""


def load_puzzle_data() -> List[List[int]]:
    """Read puzzle data from the data.txt file. Split the inputs into strings of digits seperated by 
    the blank lines in the input file, and store each string of digits in a list.
    Returns:
        List[List[str]]: List of each individual elf's food item calories  
    """
    try:
        with open("data.txt") as f:
            # Split data into digit strings seperated by blank lines, then split those strings into lists of digits
            print("[+] Loaded puzzle data")
            return [list(map(int, datum.split('\n'))) for datum in f.read().split("\n\n")]
    except FileNotFoundError as e:
        print(f"[-] Failed to load puzzle data. Reason: {str(e)}")
        exit(0)

def find_top_three_largest_amounts_of_calories_sum(puzzle_data: List[List[int]]) -> int:
    puzzle_data_sums = [sum(item) for item in puzzle_data]

    top_calories = list()    
    while len(top_calories) < 3:
        max_value = max(puzzle_data_sums)
        top_calories.append(max_value)
        puzzle_data_sums.pop(puzzle_data_sums.index(max_value))

    return sum(top_calories)


def main() -> None:
    puzzle_data = load_puzzle_data()
    # Part 1
    max_calories = max(map(sum, puzzle_data))
    print(f"[+] The biggest mule elf is carrying {max_calories} calories")
    top_3_most_calories = find_top_three_largest_amounts_of_calories_sum(puzzle_data)
    print(f"[+] The top three mule elves are carrying {top_3_most_calories} calories")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - start_time
    print(f"[+] Completed in {elapsed_time:.3f} seconds")