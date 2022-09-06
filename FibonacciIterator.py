import time

class FibonacciIterator():

    def __init__(self, limit=1000):
        self.limit = limit
        self.aux = 0

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.aux < self.limit:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration
if __name__ == '__main__':
    fibonacci = FibonacciIterator()

    for element in fibonacci:
        print(element)
        time.sleep(1)

