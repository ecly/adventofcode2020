from itertools import product


neighbour_offsets3 = list(product([-1, -0, 1], repeat=3))
neighbour_offsets3.pop(neighbour_offsets3.index((0, 0, 0)))

neighbour_offsets4 = list(product([-1, -0, 1], repeat=4))
neighbour_offsets4.pop(neighbour_offsets4.index((0, 0, 0, 0)))


def get_neighbours3(pos):
    x, y, z = pos
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in neighbour_offsets3]


def get_neighbours4(pos):
    x, y, z, w = pos
    return [(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in neighbour_offsets4]


def new_state(state, active):
    if state:
        return active in (2, 3)

    return active == 3


def solve(grid, neighbours_func):
    state = grid.copy()
    for cycle in range(6):
        read_copy = state.copy()
        positions = set(pos for p in read_copy for pos in neighbours_func(p))
        for pos in positions:
            s = read_copy.get(pos, False)
            ns = neighbours_func(pos)
            active = sum(read_copy.get(n, False) for n in ns)
            state[pos] = new_state(s, active)

    return sum(state.values())


def part1(grid):
    return solve(grid, get_neighbours3)


def part2(grid):
    grid = {(x, y, z, 0): s for (x, y, z), s in grid.items()}
    return solve(grid, get_neighbours4)


def main():
    grid = dict()
    for y, line in enumerate(open("input")):
        for x, c in enumerate(line.strip()):
            grid[(x, y, 0)] = c == "#"

    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main()
