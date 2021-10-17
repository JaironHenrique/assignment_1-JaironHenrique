'''
Testes para o exercício 2 da lista 1.
Tempo de execução do teste: <1sec
'''

import numpy as np

from exercises import exercise2


def test2():
    for t in range(1, 111):
        size = t * 10000
        arr = np.arange(0, size, t / 10)
        index = np.random.randint(1, arr.shape[0] - 1)
        arr[index] -= t / 11

        result = ((index - 1) * t / 10, index * t / 10 - t / 11)
        output = exercise2(arr)
        assert (len(result) == len(output)
                and np.all(np.isclose(result, output)))
