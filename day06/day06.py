from collections import defaultdict
import sys


def part1(groups):
    count = 0
    for group in groups:
        s = set()
        for line in group:
            s.update(list(line))

        count += len(s)

    return count


def part2(groups):
    count = 0
    for group in groups:
        group_size = len(group)
        counter = defaultdict(int)
        for line in group:
            for c in line:
                counter[c] += 1
        count += sum(v == group_size for v in counter.values())

    return count


def main():
    groups = [g.split("\n") for g in sys.stdin.read().strip().split("\n\n")]
    print(part1(groups))
    print(part2(groups))


if __name__ == "__main__":
    main()
