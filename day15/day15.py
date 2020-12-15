from collections import defaultdict


def memory_game(ns, x):
    memory = defaultdict(list)
    for idx, n in enumerate(ns):
        memory[n].append(idx)

    last = ns[-1]
    for idx in range(len(ns), x):
        x = memory.get(last)
        if x is None or len(x) == 1:
            last = 0
        else:
            last = x[-1] - x[-2]

        memory[last].append(idx)

    return last


def part1(ns):
    return memory_game(ns, 2020)


def part2(ns):
    return memory_game(ns, 30000000)


def main():
    ns = list(map(int, input().split(",")))
    print(part1(ns))
    # takes about 12 seconds with pypy3 on my machine
    print(part2(ns))


if __name__ == "__main__":
    main()
