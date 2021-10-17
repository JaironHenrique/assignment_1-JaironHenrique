'''
Testes para o exercício 3 da lista 1.
Tempo de execução do teste: <1sec
'''

import numpy as np

from exercises import exercise3


def test3():
    for t in range(1, 11):
        size = t * 10000
        arr = np.zeros((t, size))
        for col in range(t):
            arr[col] = np.random.normal(t, col, size=size)
        index = np.random.randint(0, t)
        arr[index] = np.random.normal(t, t, size=size)

        result = np.delete(arr, index, 0)
        output = exercise3(arr)
        assert (result.shape == output.shape
                and np.all(np.equal(result, output)))
