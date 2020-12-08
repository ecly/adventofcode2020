from collections import Counter
def exec(instructions, early_out=True, max=float("inf")):
    pointer = 0
    acc = 0
    seen = set()
    history = []
    op_cnt = 0
    while pointer < len(instructions):
        if op_cnt >= max:
            return None
        if pointer in seen and early_out:
            break

        op_cnt += 1
        seen.add(pointer)
        ins, cnt = instructions[pointer]
        history.append((pointer, (ins, cnt)))
        if ins == "acc":
            acc += cnt
            pointer += 1
        elif ins == "jmp":
            pointer += cnt
        elif ins == "nop":
            pointer += 1

    return acc, history


with open("input") as f:
    lines = f.read().strip().split("\n")

instructions = [i.split() for i in lines]
instructions = [(ins, int(cnt)) for ins, cnt in instructions]


# part 1
acc, history = exec(instructions)
print(acc)

# part 2
programs = []
for i, (bi, bc) in enumerate(instructions):
    if bi == "acc":
        continue

    copy = instructions.copy()
    copy[i] = ("jmp" if bi == "nop" else "nop", bc)
    programs.append(copy)

for program in programs:
    result = exec(program, early_out=False, max=10000)
    if result:
        acc, _ = result
        print(acc)
        break
