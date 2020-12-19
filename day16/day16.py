import re
import math
from itertools import takewhile
from collections import defaultdict, Counter


def part1(rules, nearby):
    ranges = re.findall("\d+-\d+", rules)
    ranges = [tuple(map(int, m.split("-"))) for m in ranges]
    error_rate = 0
    valid_tickets = []
    for l in nearby:
        for v in l.split(","):
            if not any(l <= int(v) <= h for l, h in ranges):
                error_rate += int(v)
            else:
                valid_tickets.append(l)

    return error_rate, valid_tickets


def deduce_mapping(fields):
    fields = fields.copy()
    mapping = dict()
    while fields:
        discard = set()
        for field, matches in fields.items():
            counter = Counter(matches)
            common = counter.most_common()
            max_k, max_v = common[0]
            candidates = list(takewhile(lambda x: x[1] >= max_v, common))

            # if we only have 1 candidate for this field, we assign it
            if len(candidates) == 1:
                mapping[field] = max_k
                discard.add(max_k)

        # remove categories and field ids that are assigned
        fields = {
            k: [v for v in l if v not in discard]
            for k, l in fields.items()
            if k not in mapping
        }

    return mapping


def part2(rules, mine, nearby):
    ranges = dict()
    for l in rules.split("\n"):
        k, r = l.split(": ")
        r1, r2 = r.split(" or ")
        r1 = tuple(map(int, r1.split("-")))
        r2 = tuple(map(int, r2.split("-")))
        ranges[k] = (r1, r2)

    fields = defaultdict(list)
    for n in nearby:
        for i, v in enumerate(map(int, n.split(","))):
            for r, ((l1, h1), (l2, h2)) in ranges.items():
                if l1 <= v <= h1:
                    fields[i].append(r)
                elif l2 <= v <= h2:
                    fields[i].append(r)

    mapping = deduce_mapping(fields)
    departure_ids = [f for f, name in mapping.items() if name.startswith("departure")]
    mine = list(map(int, mine.split(",")))
    return math.prod(v for idx, v in enumerate(mine) if idx in departure_ids)


def main():
    with open("input") as f:
        rules, mine, nearby = f.read().strip().split("\n\n")
        mine = mine.split("\n")[1]
        nearby = nearby.split("\n")[1:]

    error_rate, valid_tickets = part1(rules, nearby)
    print(error_rate)
    print(part2(rules, mine, valid_tickets))


if __name__ == "__main__":
    main()
