import numpy as np
from matplotlib import pyplot as plt

def retorno_dtw(referencia, a_ser_comparado):
    '''
    x = np.array([1, 2, 3, 7, 5, 8, 7, 8, 9, 10]).reshape(-1, 1)
    y = np.array([1, 2, 3, 7, 5, 3, 7, 8, 9, 0]).reshape(-1, 1)
    '''
    x = np.array(referencia).reshape(-1, 1)
    y = np.array(a_ser_comparado).reshape(-1, 1)

    from dtw import dtw

    euclidiana = lambda x, y: np.abs(x - y)

    d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=euclidiana)

    print(d)

    plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
    plt.plot(path[0], path[1], 'w')
    plt.show()
