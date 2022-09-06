from datetime import datetime


def execution_time(funct):
    """
        *args: to indicate that the function could receive 0 or many parameters without value
        **kwards: to indicate that the function could receive 0 or many parameters with valur by default
    """
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        funct(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time

        print(f'total time: {time_elapsed.total_seconds()}')
    return wrapper
#Creating decorator to execute the execution_time without parameters
@execution_time
def iterator():
    for _ in range(1, 100000000):
        pass

@execution_time
def sum(a:int, b:int):
    return a + b
if __name__ == '__main__':
    iterator()
    sum(5, 5)