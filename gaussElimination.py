from matrix import Matrix as m

def forwardElimination(mat):
    for i in range(1,mat.dimN):
        for j in range(i+1,mat.dimN+1):
            #mat = scaledPartialPivot(mat,i,i)
            mat = partialPivot(mat,i,i)
            mat = mat.rowOp(1,j,-(mat.getElement(j,i)/mat.getElement(i,i)),i,j)
    return mat

def partialPivot(mat,row,col):
    max = row
    for i in range(row+1,mat.dimN+1):
        if mat.getElement(i,col) > mat.getElement(max,col):
            max = i
    return mat.rowSwap(row,max)

def scaledPartialPivot(mat,row,col):
    max_row = row
    for i in range(row+1,mat.dimN+1):
        if (mat.getElement(i,col)/max(mat.getRow(i))) > (mat.getElement(max_row,col)/max(mat.getRow(max_row))):
            max_row = i
    return mat.rowSwap(row,max_row)