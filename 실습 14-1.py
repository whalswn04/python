def infinite_generator():
    num = 0
    while True:
        yield num
        num += 1

def coroutine_multiplier():
    while True:
        value = yield
            print(f"Received: {value}, Processed: {value * 2}")

gen = infinite_generator()
co = coroutine_multiplier()
next(co)

for _ in range(10):
    value = next(gen)
    co.send(value)
