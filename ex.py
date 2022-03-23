import time
from multiprocessing import Pool


def f(x):
    time.sleep(2)
    print(x*x)

# for item in [1, 2, 3, 4]:
#     f(item)

p = Pool(8)
p.map(f, range(1, 50))
p.close()
p.join()
