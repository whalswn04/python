def infinite_generater():
    num=0
    while True:
        yield num
        num += 1

gen = infinite_generater()

for _ in range(10):
    print(next(gen))
