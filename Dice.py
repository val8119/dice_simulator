# V Imports V
import random
import math
import time
import os
import sys
import datetime

# V Variables etc V
command = ""
cmd_split = []
total = 0
count = 0
number = 0
display_average = False
most_rolled = ""
least_rolled = ""
auto_percentage = 0
date_time = ""

dice_count = {
    "(1)": 0,
    "(2)": 0,
    "(3)": 0,
    "(4)": 0,
    "(5)": 0,
    "(6)": 0
}

# V Functions V


def DiceCount():
    if random_num == 1:
        dice_count["(1)"] += 1
    elif random_num == 2:
        dice_count["(2)"] += 1
    elif random_num == 3:
        dice_count["(3)"] += 1
    elif random_num == 4:
        dice_count["(4)"] += 1
    elif random_num == 5:
        dice_count["(5)"] += 1
    elif random_num == 6:
        dice_count["(6)"] += 1


def CalcAvg():
    if total == 0:
        return "NONE"
    else:
        return total / count


def Stats():
    most_rolled = max(dice_count, key=dice_count.get)
    least_rolled = min(dice_count, key=dice_count.get)

    print(f"""
Session statistics:
Count: {count}
Total: {total}
Average: {CalcAvg()}

NUM: ROLLS
(1): {dice_count["(1)"]}
(2): {dice_count["(2)"]}
(3): {dice_count["(3)"]}
(4): {dice_count["(4)"]}
(5): {dice_count["(5)"]}
(6): {dice_count["(6)"]}

{most_rolled} was rolled the most with {dice_count[most_rolled]} rolls
{least_rolled} was rolled the least with {dice_count[least_rolled]} rolls
""")


def HelpMsg():
    print(f"""
Commands:
help - displays commands
stats - current session statistics
reset - reset current session statistics
auto nr y - automatically roll the dice (nr - numer of rolls
                                         y/n - show average)
""")


def SaveAutorollStats(date_time):
    most_rolled = max(dice_count, key=dice_count.get)
    least_rolled = min(dice_count, key=dice_count.get)

    print(f"""Autoroll statistics for {date_time}:
Count: {count}
Total: {total}
Average: {CalcAvg()}

NUM: ROLLS
(1): {dice_count["(1)"]}
(2): {dice_count["(2)"]}
(3): {dice_count["(3)"]}
(4): {dice_count["(4)"]}
(5): {dice_count["(5)"]}
(6): {dice_count["(6)"]}

{most_rolled} was rolled the most with {dice_count[most_rolled]} rolls
{least_rolled} was rolled the least with {dice_count[least_rolled]} rolls

<============================================>
""", file=open("dice_auto.txt", "a"))


def SaveManual(date_time):
    most_rolled = max(dice_count, key=dice_count.get)
    least_rolled = min(dice_count, key=dice_count.get)

    print(f"""Session statistics for {date_time}:
Count: {count}
Total: {total}
Average: {CalcAvg()}

NUM: ROLLS
(1): {dice_count["(1)"]}
(2): {dice_count["(2)"]}
(3): {dice_count["(3)"]}
(4): {dice_count["(4)"]}
(5): {dice_count["(5)"]}
(6): {dice_count["(6)"]}

{most_rolled} was rolled the most with {dice_count[most_rolled]} rolls
{least_rolled} was rolled the least with {dice_count[least_rolled]} rolls

<============================================>
""", file=open("dice_manual.txt", "a"))


# SPACER
# SPACER
# SPACER

print(f"""
Loaded Dice.py | Roll die, show statistics (count, total, average, most and least common number)

Commands:
help - displays commands
stats - current session statistics
reset - reset current session statistics
auto nr y - automatically roll the dice (nr - numer of rolls
                                         y/n - show average)

Would you like to roll the dice? (yes/no/help)""")

while True:
    command = input("> ").lower()

    cmd_split = command.split()

    print(cmd_split)

    if command == "yes":
        random_num = random.randint(1, 6)
        DiceCount()
        count += 1
        total += random_num
        print(f"You rolled {random_num}!")
        print("Would you like to roll the dice again? (yes/no/help)")

    elif command == "no":
        break

    elif cmd_split[0] == "auto":

        if cmd_split[2] == "y":
            display_average = True
        else:
            display_average = False

        for number in range(1, int(cmd_split[1]) + 1):
            auto_percentage = (number / int(cmd_split[1])) * 100

            random_num = random.randint(1, 6)

            DiceCount()

            count += 1
            total += random_num

            if display_average:
                print(
                    f"{round(auto_percentage, 2)}% | Roll number {number}: | Current roll {random_num}| Average: {CalcAvg()}")
            else:
                print(
                    f"{round(auto_percentage, 2)}% | Roll number {number}: | Current roll {random_num}")

        print("Done!")

        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        SaveAutorollStats(date_time)

        print("Autoroll stats saved! ")

    elif command == "stats":
        Stats()

        if count >= 1:
            print("Would you like to roll the dice again? (yes/no/help)")

        else:
            print("Would you like to roll the dice? (yes/no/help)")

    elif command == "help":
        HelpMsg()
        if count >= 1:
            print("Would you like to roll the dice again? (yes/no/help)")

        else:
            print("Would you like to roll the dice? (yes/no/help)")

    elif command == "save":
        print("Would you like to save the current session statistics? (yes/no)")

        command = input("> ").lower()

        if command == "yes":
            now = datetime.datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            SaveManual(date_time)
            print("Session statistics saved!")

        elif command == "no":
            print("Cancelled!")

    elif command == "reset":
        total = 0
        count = 0
        most_rolled = ""
        least_rolled = ""
        auto_percentage = 0

        dice_count = {
            "(1)": 0,
            "(2)": 0,
            "(3)": 0,
            "(4)": 0,
            "(5)": 0,
            "(6)": 0
        }
        print("Current session statistics reset!")

    else:
        print("ERROR: Invalid command")

if count >= 1:
    Stats()

print("Goodbye!")
