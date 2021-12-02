import os
horizontal = 0
depth = 0
aim = 0
instructions = []
print(os.getcwd())
os.chdir("c:/Users/aldal/OneDrive/Masaüstü/Python/Challaneges/AdventOfCode2021/Day02/")
with open("Day02.txt", "r") as f:
    data = f.read()
    data = data.splitlines()

for i in data:
    instructions.append(i.split(" "))
for i in instructions:
    i[1] = int(i[1])


def part1(depth, horizontal):
    for items in instructions:
        if items[0] == "up":
            depth -= items[1]
        elif items[0] == "down":
            depth += items[1]
        elif items[0] == "forward":
            horizontal += items[1]

    print(horizontal*depth)


def part2(depth, horizontal, aim):
    for items in instructions:
        if items[0] == "up":
            aim -= items[1]
        elif items[0] == "down":
            aim += items[1]
        elif items[0] == "forward":
            horizontal += items[1]
            depth += aim*items[1]
    print(horizontal*depth)


part1(depth, horizontal)
part2(depth, horizontal, aim)
