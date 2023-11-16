import time

OFF = "⬜️"  # 0
ON = "⬛️"  # 1


def sliding_window(s: str):
    i = -1
    j = 0
    k = 1
    while j <= (len(s) - 1):
        yield int(s[i % len(s)]), int(s[j % len(s)]), int(s[k % len(s)])
        i += 1
        j += 1
        k += 1


def int_to_8bits(n: int):
    return f"{n:08b}"


def gen_ruleset(rule_no):
    mapping = {}
    bit_str = int_to_8bits(rule_no)
    index = 0
    for a, b, c in reversed(
        [(i, j, k) for i in range(2) for j in range(2) for k in range(2)]
    ):
        mapping[(a, b, c)] = int(bit_str[index])
        index += 1

    return lambda a, b, c: mapping[(a, b, c)]


def update(ruleset, a: int, b: int, c: int):
    return ruleset(a, b, c)


def eca(start, rule_no):
    ruleset = gen_ruleset(rule_no)
    new_start = ""
    for a, b, c in sliding_window(start):
        new_start += str(update(ruleset, a, b, c))
    return new_start


start = "101110111101010101010000010000000001111000"

while True:
    print(start.replace("0", OFF).replace("1", ON))
    start = eca(start, 22)
    time.sleep(0.05)
