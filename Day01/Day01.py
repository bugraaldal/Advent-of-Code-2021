import os
print(os.getcwd())
os.chdir("c:/Users/aldal/OneDrive/Masaüstü/Python/Challaneges/AdventOfCode2021/Day01/")
measurements = []
with open("Day01.txt", "r") as f:
    data = f.read()
    measurements = data.splitlines()
measurements = list(map(int, measurements))


def part1():
    bigger = 0
    for i, measurement in enumerate(measurements):
        if i != 0:
            if measurements[i] > measurements[i-1]:
                bigger += 1
    print(bigger)


def part2():
    bigger = 0
    for i, measurement in enumerate(measurements):
        try:
            if (measurements[i] + measurements[i+1] + measurements[i+2]) < (measurements[i+1] + measurements[i+2] + measurements[i+3]):
                bigger += 1
        except IndexError:
            print(bigger)
            break


part1()
part2()
