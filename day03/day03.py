import sys


def count_trees(grid, dx, dy):
    x = 0
    y = 0
    trees = 0
    max_x = len(grid[0])
    while y < len(grid):
        if grid[y][x % max_x] == "#":
            trees += 1

        x += dx
        y += dy

    return trees


def part1(grid):
    return count_trees(grid, 3, 1)


def part2(grid):
    product = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        product *= count_trees(grid, dx, dy)

    return product


def main():
    grid = sys.stdin.read().strip().split("\n")
    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main()
