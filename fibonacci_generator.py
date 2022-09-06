from time import sleep
def fibonacci_generator(limit: int = 1000):
    a, b = 0, 1
    while b < limit :
        yield a
        a, b = b, a + b

def run():
    for element in fibonacci_generator():
        print(element)
        sleep(1)


if __name__ == '__main__':
    run()