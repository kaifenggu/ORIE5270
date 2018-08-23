from scipy.optimize import minimize, rosen
import numpy as np

if __name__ == '__main__':
    N = 1000
    x0_matrix = (np.random.rand(N,3)*2)
    xa = []
    for i in range(N):
        x0 = x0_matrix[i]
        re = minimize(rosen, x0, method='BFGS')
        xa.append(re.x)
    xa = np.array(xa)
    xaT = xa.T
    xa_average = [np.average(xaT[0]),np.average(xaT[1]),np.average(xaT[2])]
    print(xa_average)