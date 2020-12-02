import sys
from collections import namedtuple

ParsedLine = namedtuple("ParsedLine", ["l", "h", "letter", "pw"])


def part1(parsed_lines):
    return sum(p.l <= p.pw.count(p.letter) <= p.h for p in parsed_lines)


def part2(parsed_lines):
    return sum(
        (p.pw[p.l - 1] == p.letter) ^ (p.pw[p.h - 1] == p.letter) for p in parsed_lines
    )


def parse():
    parsed_lines = []
    for line in open("input.txt"):
        criteria, password = line.strip().split(": ")
        interval, letter = criteria.split()
        l, h = map(int, interval.split("-"))
        parsed_lines.append(ParsedLine(l, h, letter, password))

    return parsed_lines


def main():
    parsed_lines = parse()
    print(part1(parsed_lines))
    print(part2(parsed_lines))


if __name__ == "__main__":
    main()
