# timer function that accounts for drift: https://stackoverflow.com/a/28034554
import time


def do_every(period_in_s, f, *args):
    def g_tick():
        t = time.time()
        while True:
            t += period_in_s
            yield max(t - time.time(), 0)

    g = g_tick()
    while True:
        time.sleep(next(g))
        f(*args)


# def hello(s):
#    print('hello {} ({:.4f})'.format(s,time.time()))
#    time.sleep(.3)
# do_every(1,hello,'foo')
