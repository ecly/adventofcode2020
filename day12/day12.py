import sys

M = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def part1(lines):
    x, y = 0, 0
    dx, dy = 1, 0
    for l in lines:
        action = l[0]
        c = int(l[1:])
        if action in M:
            dx_, dy_ = M[action]
            x += c * dx_
            y += c * dy_
        elif action in "LR":
            d = c // 90
            for _ in range(d):
                dx, dy = (-dy, dx) if action == "R" else (dy, -dx)
        else:
            x += c * dx
            y += c * dy

    return abs(x) + abs(y)


def part2(lines):
    wx, wy = 10, -1
    x, y = 0, 0
    for l in lines:
        action = l[0]
        c = int(l[1:])
        if action in M:
            dx_, dy_ = M[action]
            wx += c * dx_
            wy += c * dy_
        elif action in "LR":
            d = c // 90
            for _ in range(d):
                wx, wy = (-wy, wx) if action == "R" else (wy, -wx)
        else:
            x += c * wx
            y += c * wy

    return abs(x) + abs(y)


def main():
    lines = sys.stdin.read().strip().split("\n")
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
