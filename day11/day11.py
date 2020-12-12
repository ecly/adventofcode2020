import sys
from itertools import count


def process(grid, tolerance, directional=False):
    state = grid.copy()

    while True:
        read_copy = state.copy()

        for (x, y), v in state.items():
            adj = 0
            for dx, dy in [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]:
                it = count(1) if directional else [1]
                for m in it:
                    seat = (x + m * dx, y + m * dy)
                    seat_v = read_copy.get(seat, "L")
                    if seat_v == "L":
                        break
                    if seat_v == "#":
                        adj += 1
                        break

            if v == "L" and not adj:
                state[x, y] = "#"

            if v == "#" and adj >= tolerance:
                state[x, y] = "L"

        if read_copy == state:
            return sum(v == "#" for v in state.values())


def part1(grid):
    return process(grid, 4)


def part2(grid):
    return process(grid, 5, True)


def main():
    grid = dict()
    for i, line in enumerate(sys.stdin):
        for j, c in enumerate(line.strip()):
            grid[i, j] = c

    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main()
