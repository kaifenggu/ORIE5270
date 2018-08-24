from scipy.optimize import minimize, rosen
import numpy as np

if __name__ == '__main__':
    N = 1000
    x0_matrix = (np.random.rand(N,3)*2000-1000)
    xa = []
    fa = []
    for i in range(N):
        x0 = x0_matrix[i]
        re = minimize(rosen, x0, method='BFGS')
        xa.append(re.x)
        fa.append(re.fun)
    xa = np.array(xa)
    opt_value = np.min(fa)
    print("optimal value so far:",opt_value)
    for i in range(N):
        if fa[i]==opt_value:
            print("corresponding x values:", xa[i])