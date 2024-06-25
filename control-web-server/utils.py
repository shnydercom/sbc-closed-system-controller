# timer function that accounts for drift: https://stackoverflow.com/a/28034554
import time


def do_every(period_in_s, f, *args):
    def g_tick():
        t = time.time()
        while True:
            t += period_in_s
            result = max(t - time.time(), 0)
            # print(result)
            yield result

    g = g_tick()
    while True:
        # print("do_every while " + str(period_in_s))
        time.sleep(next(g))
        # print("doing" + str(period_in_s))
        f(*args)


# def hello(s):
#    print('hello {} ({:.4f})'.format(s,time.time()))
#    time.sleep(.3)
# do_every(1,hello,'foo')
