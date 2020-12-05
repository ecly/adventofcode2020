import math
import sys


def bpart(line, l, h, l_char, h_char):
    for c in line[:-1]:
        d = math.ceil((h - l) / 2)
        if c == l_char:
            h -= d
        elif c == h_char:
            l += d

    return l if line[-1] == l_char else h


def get_seat_id(line):
    row = bpart(line[:7], 0, 127, "F", "B")
    column = bpart(line[7:], 0, 7, "L", "R")
    seat_id = (row * 8) + column
    return seat_id


def part1(lines):
    return max(get_seat_id(l) for l in lines)


def part2(lines):
    seat_ids = {get_seat_id(l) for l in lines}
    min_id = min(seat_ids)
    max_id = max(seat_ids)
    all_ids = set(range(min_id, max_id + 1))
    return (all_ids - seat_ids).pop()


def main():
    lines = sys.stdin.read().strip().split("\n")
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
