import re
from operator import add, mul


class C1:
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        return C1(self.n + x.n)

    # use sub for mult for identical precedence
    def __sub__(self, x):
        return C1(self.n * x.n)


class C2(C1):
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        return C2(self.n + x.n)

    # use bitwise and for mult for lower precedence
    def __and__(self, x):
        return C2(self.n * x.n)


def part1(lines):
    total = 0
    for l in lines:
        l = re.sub("(\d)", "C1(\\1)", l.replace("*", "-"))
        total += eval(l).n

    return total


def part2(lines):
    total = 0
    for l in lines:
        l = re.sub("(\d)", "C2(\\1)", l.replace("*", "&"))
        total += eval(l).n

    return total


def main():

    with open("input") as f:
        lines = f.read().splitlines()

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
