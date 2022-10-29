from matrix import Matrix as mtx
import gaussElimination as g

mtxA = mtx([[1,2,3,1,15],
            [-1,-3,3,1,3],
            [6,2,3,1,20],
            [1,1,1,1,7]])

mtxB = mtx([[1,1,1.1],[1,1,1]])

print(g.forwardElimination(mtxA))