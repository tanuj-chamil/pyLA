from matrix import Matrix as m

def forwardElimination(mat):
    for i in range(1,mat.dimN):
        for j in range(i+1,mat.dimN+1):
            mat = mat.rowOp(1,j,-(mat.getElement(j,i)/mat.getElement(i,i)),i,j)
    return mat