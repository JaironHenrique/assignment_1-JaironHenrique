'''
Lista de Exercícios 1: Numpy.

A lista é composta por 4 funções que deve completa-las como pedido.
Não é permitido importar outras bibliotecas nem utilizar loops, como for, while
ou comprehension lists.
'''

import numpy as np


def exercise1(dates: np.ndarray, date: np.datetime64):
    '''
    Dado o array de datas e uma data,
    retorne um array só com os dias da semana
    iguais ao da data.
    Peso: 2
    Dificuldade: Fácil
    Número aproximado de linhas da solução: 2

    Parameters:
    ----------
        dates : 1D array of np.datetime64
        date  : np.datetime64

    Returns:
    -------
        arr : 2D array of float

    Examples:
    --------
        >>> exercise3(np.arange(np.datetime64('2018-02-01'),
                                np.datetime64('2018-02-25')),
                      np.datetime64('2018-02-01'))
        array(['2018-02-01', '2018-02-08', '2018-02-15', '2018-02-22'],
              dtype='datetime64[D]')
    '''

    return dates[(dates - date).astype(int) % 7 == 0]


def exercise2(arr: np.ndarray):
    '''
    Dado o array retorne os dois valores
    consecutivos de menor diferença.
    Peso: 3
    Dificuldade: Médio
    Número aproximado de linhas da solução: 3

    Parameters:
    ----------
        arr : 1D array of float

    Returns:
    -------
        (float, float)

    Examples:
    --------
        >>> exercise1(np.array([1,2,3,4,5,5.3,6]))
        (5.0, 5.3)
    '''

    shift = np.concatenate((np.array([0]), arr))[:-1]
    maximo = (arr - shift)[1:].argmax()
    return arr[maximo], arr[maximo+1]


def exercise3(arr: np.ndarray):
    '''
    Dado o array remova a coluna de maior desvio padrão
    Peso: 3
    Dificuldade: Médio
    Número aproximado de linhas da solução: 3

    Parameters:
    ----------
        arr : 2D array of float

    Returns:
    -------
        2D array of float

    Examples:
    --------
        >>> exercise2(np.array([[1, 2, 3], [1, 4, 6], [2, 3, 4]]))
        array([[1, 2, 3],
               [2, 3, 4]])
    '''

    return np.delete(arr, (arr.std(axis = 0).argmax()), axis = 0)


def exercise4(img: np.ndarray):
    '''
    Dado o array de imagem em RGB,
    retorne os indices dos pixels vermelhos que
    possuem pixels verdes em cima e não possuem
    pixels azuis em baixo.
    Peso: 2
    Dificuldade: Difícil
    Número aproximado de linhas da solução: 8

    Parameters:
    ----------
        img : 3D array of int

    Returns:
    -------
        tuple of array of int

    Examples:
    --------
        >>> exercise4(np.array([[[255, 255, 255],
                                 [  0, 255, 255],
                                 [  0, 255,   0]],

                                [[255,   0,   0],
                                 [  0, 255, 255],
                                 [255,   0,   0]],

                                [[  0, 255,   0],
                                 [255, 255, 255],
                                 [  0, 255, 255]]]))
        (array([1]), array([2]))
    '''

    pass
