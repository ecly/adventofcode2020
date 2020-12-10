import sys


OUTLET_RATING = 0


def part1(ratings):
    diffs = [h - l for l, h in zip(ratings, ratings[1:])]
    return sum(d == 1 for d in diffs) * sum(d == 3 for d in diffs)


def part2(ratings, memory=None, offset=0):
    if memory is None:
        memory = dict()

    head, *tail = ratings
    if not tail:
        return 1

    options = 0
    for idx, option in enumerate(tail[:3]):
        if option - head > 3:
            break

        tail_offset = offset + idx + 1
        if tail_offset in memory:
            options += memory[tail_offset]
        else:
            tail_options = part2(tail[idx:], memory, tail_offset)
            options += tail_options
            memory[tail_offset] = tail_options

    return options


def main():
    ratings = list(map(int, sys.stdin.readlines()))
    ratings = sorted([0] + ratings + [max(ratings) + 3])
    print(part1(ratings))
    print(part2(ratings))


if __name__ == "__main__":
    main()
