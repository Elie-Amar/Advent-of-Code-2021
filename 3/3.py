# 2

import sys
sys.setrecursionlimit(1007)

input = []
with open('input.txt') as f:
    input = f.readlines()
input = [el.split("\n")[0] for el in input]

input_test = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def count(input, i, res):
    if i == len(input):
        return res
    for y, number in enumerate(input[i]):
        res[y] += number == "1"
    return count(input, i+1, res)


def do(input, i, res):
    c = count(input, i, res)
    final = ""
    inverted = ""
    for y in c:
        final += "1" if c[y] >= len(input) / 2 else "0"
        inverted += "0" if c[y] >= len(input) / 2 else "1"
    return int(final, 2) * int(inverted, 2)


def do2(input, i, res):
    o2 = [*input]
    co2 = [*input]

    for z in range(len(input[0])):
        c1 = count(o2, i, {n: 0 for n in range(len(input[0]))})
        c2 = count(co2, i, {n: 0 for n in range(len(input[0]))})

        final = ""
        inverted = ""
        for uwu in c1:
            final += "1" if c1[uwu] >= len(o2) / 2 else "0"
        for uwu in c2:
            inverted += "0" if c2[uwu] >= len(co2) / 2 else "1"

        y = 0
        o2_to_remove = []
        while(len(o2) > 1 and y < len(o2)):
            word = o2[y]
            if (word[z] != final[z]):
                o2_to_remove.append(word)
            y += 1
        o2 = [el for el in o2 if el not in o2_to_remove]

        y = 0
        co2_to_remove = []
        while(len(co2) > 1 and y < len(co2)):
            word = co2[y]
            if (word[z] != inverted[z]):
                co2_to_remove.append(word)
            y += 1
        co2 = [el for el in co2 if el not in co2_to_remove]
    return int(o2[0], 2) * int(co2[0], 2)


assert 198 == do(input_test, 0, {n: 0 for n in range(len(input_test[0]))})
print("res: ", do(input, 0, {n: 0 for n in range(len(input[0]))}))

assert 230 == do2(input_test, 0, {n: 0 for n in range(len(input_test[0]))})
print("res2: ", do2(input, 0, {n: 0 for n in range(len(input[0]))}))
