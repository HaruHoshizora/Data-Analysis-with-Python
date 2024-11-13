import numpy as np

def calculate(list):
    a = 0
    array = np.array([
        [list[a], list[a + 1], list[a + 2]],
        [list[a + 3], list[a + 4], list[a + 5]],
        [list[a + 6], list[a + 7], list[a + 8]]
    ])
    calculations = {}
    calculations['mean'] = [array.mean(axis=0)], [array.mean(axis=1)], [array.mean()]
    calculations['variance'] = [array.var(axis=0)], [array.var(axis=1)], [array.var()]
    calculations['standard deviation'] = [array.std(axis=0)], [array.std(axis=1)], [array.std()]
    calculations['max'] = [array.max(axis=0)], [array.max(axis=1)], [array.max()]
    calculations['min'] = [array.min(axis=0)], [array.min(axis=1)], [array.min()]
    calculations['sum'] = [array.sum(axis=0)], [array.sum(axis=1)], [array.sum()]
    calculations = {key: [val[0][0].tolist(), val[1][0].tolist(), val[2][0].tolist()] for key, val in calculations.items()}
    return calculations
