from math import *
from random import *
import numpy as np

#-------------------------------------------

def genererA(n):
    A = np.random.randint(10, size=(n, n))
    print("\nA=\n", A)
    return A

def jacobi_MN(A):
    M = np.zeros(A.shape)
    N = -A
    for i in range(A.shape[0]):
        M[i,i] = A[i, i]
        N[i, i] = 0
    '''print("\nM=\n", M)
    print("\nN=\n", N)'''
    return M, N

def gs_MN(A):
    M = A
    N = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(i+1, A.shape[0]):
            N[i, j] = -A[i, j]
            M[i, j] = 0    
    '''print("\nM=\n", M)
    print("\nN=\n", N)'''
    return M, N

def converge(M, N):
    B = np.linalg.inv(M) @ N #matrice d'itération
    vp = np.linalg.eigvals(B)
    ray_spec =abs(max(vp))
    return ray_spec

#initialisation
'''A = genererA(3)'''
A = np.array([[1, 2, -2], [1, 1, 1], [2, 2, 1]])
print("\nA=\n", A)

#par jacobi
M, N = jacobi_MN(A)
ray_spec = converge(M, N)
print("\np(J) = ", ray_spec)

#par gauss-seidel
M, N = gs_MN(A)
ray_spec = converge(M, N)
print("\np(G) = ", ray_spec)

print("\nAu vu des valeurs de rayon spectral, on en déduit quelle(s) méthode(s) converge(nt)")










