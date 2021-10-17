'''
Testes para o exercício 4 da lista 1.
Tempo de execução do teste: ~45sec
'''

import numpy as np

from exercises import exercise4


def test4():
    for t in range(1, 11):
        size = t * 100
        img = np.random.randint(0, 3, (size, size, 3)) * 128 - 1
        img[img == -1] = 0
        result_0 = []
        result_1 = []
        for i in range(1, size - 1):
            for j in range(size):
                if np.all(img[i,j] == np.array([255, 0, 0])) \
                   and np.all(img[i-1,j] == np.array([0, 255, 0])) \
                   and not np.all(img[i+1,j] == np.array([0, 0, 255])):
                    result_0.append(i)
                    result_1.append(j)

        result = np.array(result_0), np.array(result_1)
        result = np.sort(np.rec.fromarrays(result))
        result_0, result_1 = tuple(zip(*tuple(result))) \
            if result.size > 0 else ((), ())
        result_0, result_1 = np.array(result_0), np.array(result_1)
        output = exercise4(img)
        output = np.sort(np.rec.fromarrays(output))
        output_0, output_1 = tuple(zip(*tuple(output))) \
            if output.size > 0 else ((), ())
        output_0, output_1 = np.array(output_0), np.array(output_1)
        assert (result_0.shape == output_0.shape
                and result_1.shape == output_1.shape
                and np.all(np.equal(result_0, output_0))
                and np.all(np.equal(result_1, output_1)))
