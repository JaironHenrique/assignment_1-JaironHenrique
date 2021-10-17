'''
Testes para o exercício 1 da lista 1.
Tempo de execução do teste: <1sec
'''

import numpy as np

from exercises import exercise1


def test1():
    date0 = np.datetime64('0000-01-01')
    for t in range(1, 11):
        size = t * 10000
        dates = np.arange(date0 + size, date0 + 2 * size)
        date = date0 + size + np.random.randint(size)

        result = np.concatenate(
            (np.arange(date, date0 + size - 1,
                       -7)[::-1], np.arange(date + 7, date0 + 2 * size, 7)))
        output = exercise1(dates, date)
        assert (result.shape == output.shape
                and np.all(np.equal(result, output)))
