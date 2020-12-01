import itertools
import sys


def part1(numbers):
    for x, y in itertools.combinations(numbers, 2):
        if x + y == 2020:
            return x * y


def part2(numbers):
    for x, y, z in itertools.combinations(numbers, 3):
        if x + y + z == 2020:
            return x * y * z


def main():
    numbers = list(map(int, sys.stdin))
    print(part1(numbers))
    print(part2(numbers))


if __name__ == "__main__":
    main()
