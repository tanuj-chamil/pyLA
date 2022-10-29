from matrix import Matrix as mtx
import gaussElimination as g

mtxA = mtx([[0.02,0.01,0,0,0.02],
            [1,2,1,0,1],
            [0,1,2,1,4],
            [0,0,100,200,800]])

mtxB = mtx([[1,1,1.1],[1,1,1]])

print(g.forwardElimination(mtxA))