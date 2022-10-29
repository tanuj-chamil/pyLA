from matrix import Matrix as mtx

mtxA = mtx([[1,2,5],[5,6,8/2],[5,6,7]])
mtxB = mtx([[1,1,1.1],[1,1,1]])

print(mtxA)
print(mtxA.rowOp(1,10,1,-1,2))
print(mtxA.rowSwap(1,2))
print(mtxA.rowScale(2,10))
print(mtxA.__repr__())