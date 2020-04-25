import vector
import numpy as np


def run_few(seed):

    """
    Runs a function glass with each element of the input list with seeds.
    """

    number = 0
    for seed in seed:
        glass(seed, number)
        number += 1

def glass(seed, number):

    """
    Using the input seed, randomly generates the coordinates
    of the vectors and builds a drawing using methods from Glass.
    """

    seed = seed

    width = 1000
    height = 1000

    save = np.random.seed(seed)
    amount = np.random.randint(0, 100)

    center_x = np.random.uniform(0, width)
    center_y = np.random.uniform(0, height)

    x2 = np.random.uniform(0, width, size=(amount, 1))
    y2 = np.random.uniform(0, height, size=(amount, 1))

    s = vector.Glass()

    s.create(width=width, height=height)


    for attempt in range(amount):
        s.line(x1=center_x,y1=center_y,x2=x2[attempt][0],y2=y2[attempt][0])

    s.finish()

    name = 'img/glass' + f'{number}' + '.svg'
    s.save(name)

run_few([1, 10, 100, 1000, 10000, 100000])
# run_few([78, 45, 32, 97, 65, 61])