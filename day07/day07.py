import sys
from collections import defaultdict


def parse():
    lines = sys.stdin.read().strip().split("\n")
    rules_fwd = defaultdict(list)
    rules_bwd = defaultdict(list)
    for line in lines:
        if not line.strip():
            continue

        bag, rest = line.split(" bags contain ")
        for rule in rest.split(", "):
            if rule == "no other bags.":
                continue

            count, adj1, adj2, _ = rule.split()
            tgt = f"{adj1} {adj2}"
            rules_fwd[tgt].append(bag)
            rules_bwd[bag].append((int(count), tgt))

    return rules_fwd, rules_bwd


def part1(rules):
    seen = set()
    queue = rules["shiny gold"]
    while queue:
        c = queue.pop()
        seen.add(c)
        for color in rules[c]:
            if color not in seen:
                queue.append(color)

    return len(seen)


def count_bags(color, rules):
    count = 0
    for cnt, clr in rules[color]:
        count += cnt
        count += cnt * count_bags(clr, rules)

    return count


def part2(rules):
    return count_bags("shiny gold", rules)


def main():
    rules_fwd, rules_bwd = parse()
    print(part1(rules_fwd))
    print(part2(rules_bwd))


if __name__ == "__main__":
    main()
