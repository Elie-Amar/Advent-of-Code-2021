# 2
input = []
with open('input.txt') as f:
    input = f.readlines()

input_test = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def do(input):
    store = {"forward": 0, "down": 0, "up": 0}
    for i in input:
        dir, n = i.split(" ")
        store[dir] += int(n)

    store["depth"] = store.get("down", 0) - store.get("up", 0)
    store["res"] = store.get("forward", 0) * store.get("depth", 0)
    return store.get("res", 0)


def do2(input):
    store = {"forward": 0, "down": 0, "up": 0, "depth": 0}
    for i in input:
        dir, n = i.split(" ")
        n = int(n)
        store[dir] += n
        if dir == "forward":
            # store["aim"] = store.get("down", 0) - store.get("up", 0)         # is commented because unnecessary
            store["depth"] += n * (store.get("down", 0) - store.get("up", 0))  # forward * aim

    store["res"] = store.get("forward", 0) * store.get("depth", 0)
    return store.get("res", 0)


assert 150 == do(input_test)
print(do(input))

assert 900 == do2(input_test)
print(do2(input))
