input = []
with open('input.txt') as f:
    input = [int(lines) for lines in f.readlines()]

input_test_1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input_test_2 = [607, 618, 618, 617, 647, 716, 769, 792]


def do(input, step):
    res = 0
    for i in range(step, len(input)):
        res += 1 if input[i] > input[i-step] else 0
    return res


# Part 1
assert 7 == do(input_test_1, 1)
print(do(input, 1))

# Part 2
assert 5 == do(input_test_2, 3)
print(do(input, 3))
