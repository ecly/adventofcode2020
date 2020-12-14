from collections import defaultdict


def part1(lines):
    memory = defaultdict(lambda: ["0" for _ in range(36)])
    mask = "X" * 36
    for l in lines:
        if l.startswith("mask"):
            mask = l.split(" = ")[1]
        else:
            mem, v = l.split(" = ")
            m_addr = int(mem[4:-1])
            current = memory[m_addr]
            binary = f"{int(v):036b}"
            for idx, (m, b) in enumerate(zip(mask, binary)):
                if m != "X":
                    current[idx] = m
                    continue

                current[idx] = b

    total = 0
    for v in memory.values():
        total += int("".join(v), base=2)

    return total


def get_floating_addresses(addr):
    addrs = [[]]
    for c in addr:
        floating_copies = []
        for a in addrs:
            if c in "10":
                a.append(c)
            else:
                float_copy = a.copy()
                a.append("0")
                float_copy.append("1")
                floating_copies.append(float_copy)

        addrs.extend(floating_copies)

    return [int("".join(c), base=2) for c in addrs]


def part2(lines):
    memory = dict()
    mask = "X" * 36
    for l in lines:
        if l.startswith("mask"):
            mask = l.split(" = ")[1]
        else:
            mem, value = l.split(" = ")
            m_addr = int(mem[4:-1])
            b_addr = f"{int(m_addr):036b}"
            masked_addr = list(b_addr)
            for idx, (m, b) in enumerate(zip(mask, b_addr)):
                if m == "0":
                    masked_addr[idx] = b
                if m in "1X":
                    masked_addr[idx] = m

            for addr in get_floating_addresses(masked_addr):
                memory[addr] = int(value)

    return sum(memory.values())


def main():
    with open("input") as f:
        lines = f.read().splitlines()

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
