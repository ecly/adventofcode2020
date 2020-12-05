import re
import sys


REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def part1(passports):
    return sum(not bool(REQUIRED_KEYS - p.keys()) for p in passports)


def part2(passports):
    valid = 0
    for p in passports:
        if REQUIRED_KEYS - p.keys():
            continue

        try:
            assert 1920 <= int(p["byr"]) <= 2002
            assert 2010 <= int(p["iyr"]) <= 2020
            assert 2020 <= int(p["eyr"]) <= 2030
            hgt = p["hgt"]
            if hgt[-2:] == "cm":
                assert 150 <= int(hgt[:-2]) <= 193
            elif hgt[-2:] == "in":
                assert 59 <= int(hgt[:-2]) <= 76
            else:
                continue
            assert re.match(r"^#[0-9a-f]{6}$", p["hcl"])
            assert p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            assert re.match(r"^\d{9}$", p["pid"])

            valid += 1
        except:
            pass

    return valid


def main():
    sections = sys.stdin.read().split("\n\n")
    passports = []
    for section in sections:
        passport = dict()
        for line in section.strip().split("\n"):
            fields = dict(tuple(field.split(":")) for field in line.split())
            passport.update(fields)

        passports.append(passport)

    print(part1(passports))
    print(part2(passports))


if __name__ == "__main__":
    main()
