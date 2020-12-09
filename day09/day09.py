from itertools import combinations
import sys

PREAMBLE = 25


def part1(numbers):
    for idx in range(PREAMBLE, len(numbers)):
        target = numbers[idx]
        start_idx = max(0, idx - PREAMBLE)
        preamble_range = numbers[start_idx:idx]
        if not any(x + y == target for x, y in combinations(preamble_range, 2)):
            return target


def part2(numbers, target):
    for idx, initial in enumerate(numbers):
        total = initial
        for i in range(idx + 1, len(numbers)):
            total += numbers[i]
            if total == target:
                return numbers[idx + 1] + numbers[i]
            if total > target:
                break


def main():
    numbers = list(map(int, sys.stdin.read().strip().split("\n")))
    target = part1(numbers)
    print(target)
    print(part2(numbers, target))


if __name__ == "__main__":
    main()
