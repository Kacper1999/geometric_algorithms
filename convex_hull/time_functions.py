import time


def time_func(function, *arguments):
    start_time = time.time()
    function(*arguments)
    return time.time() - start_time
