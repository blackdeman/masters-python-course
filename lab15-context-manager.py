import time


class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, type, value, traceback):
        print "Operation took {0:.2f} seconds".format(time.clock() - self.start)


def do_something():
    time.sleep(3)


with Timer():
    do_something()
