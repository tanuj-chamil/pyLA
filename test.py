from matrix import Matrix as mtx

mtxA = mtx([[1,2,5.222],[5,6,7/2]])
mtxB = mtx([[1,1,1.1],[1,1,1]])

print(mtxA)
print(mtxA.rowOp(1,1,1,-1,2))
print(mtxA.rowSwap(1,2))
print(mtxA.rowScale(2,10))