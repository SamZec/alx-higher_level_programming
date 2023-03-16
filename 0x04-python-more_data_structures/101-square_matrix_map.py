#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        pass

    def _square(ls):
        nls = []
        for i in ls:
            nls.append(i * i)
        return nls
    _matrix = list(map(_square, matrix))
    return _matrix
