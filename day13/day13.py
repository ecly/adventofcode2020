import functools
import math


def get_wait(earliest, schedule):
    min_t = schedule * math.ceil(earliest / schedule)
    return min_t - earliest


def part1(earliest, ids):
    ns = [int(t) for t in ids if t != "x"]
    waits = [(get_wait(earliest, t), t) for t in ns]
    min_wait, min_t = min(waits)
    return min_wait * min_t


def chinese_remainder(n, a):
    """Short implementation of chinese remainder theorem.

    See theorem here:
        https://brilliant.org/wiki/chinese-remainder-theorem/

    For mod_inv in Python 3.8+ see:
        https://stackoverflow.com/a/9758173
    """
    prod = math.prod(n)
    total = sum(y * pow(prod // x, -1, x) * (prod // x) for x, y in zip(n, a))
    return total % prod


def part2(ids):
    ns = [(int(t), int(t) - idx) for idx, t in enumerate(ids) if t != "x"]
    return chinese_remainder([x[0] for x in ns], [x[1] for x in ns])


def main():
    lines = open("input").read().strip().split("\n")
    ids = lines[1].split(",")
    earliest = int(lines[0])
    print(part1(earliest, ids))
    assert part2("17,x,13,19".split(",")) == 3417
    assert part2("67,7,59,61".split(",")) == 754018
    assert part2("67,x,7,59,61".split(",")) == 779210
    assert part2("67,7,x,59,61".split(",")) == 1261476
    assert part2("1789,37,47,1889".split(",")) == 1202161486
    print(part2(ids))


if __name__ == "__main__":
    main()
