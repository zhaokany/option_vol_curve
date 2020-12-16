from typing import Sequence

from scipy.sparse import diags

import numpy as np
from numpy.linalg import inv


def natural_cubic_spline(xs: Sequence[float], ys: Sequence[float], lmda: float, ys_prior: Sequence):
    n = len(xs)
    h = np.diff(xs)
    h_inverse = 1.0 / h
    main_diag = 2.0 * np.hstack([h_inverse[0], h_inverse[:-1] + h_inverse[1:], h_inverse[-1]])
    diag_rows = [h_inverse, main_diag, h_inverse]
    A = diags(diag_rows, [-1, 0, 1]).toarray()

    h_inverse_squared = h_inverse ** 2
    main_diag = 3.0 * np.hstack([h_inverse_squared[0], -h_inverse_squared[:-1] + h_inverse_squared[1:],
                            -h_inverse_squared[-1]])
    diag_rows = [h_inverse_squared, main_diag, -h_inverse_squared]
    B = diags(diag_rows, [-1, 0, 1]).toarray()

    M = -inv(A) @ B

    H1 = np.zeros((n - 1, n))
    H1[np.arange(n - 1), np.arange(n - 1)] = np.ones(n - 1)
    H1[np.arange(n - 1), np.arange(n - 1) + 1] = np.zeros(n - 1)
    last_row = np.zeros(n)
    last_row[-1] = 1.0
    H1 = np.vstack([H1, last_row])

    H2 = np.zeros((n - 1, n))
    H2[np.arange(n - 1), np.arange(n - 1)] = h * 0.0
    H2[np.arange(n - 1), np.arange(n - 1) + 1] = h * 0.0
    H2 = np.vstack([H2, np.zeros(n)])

    X = H1 + H2 @ M

    scaled_lmda = lmda * (np.sqrt(np.dot(ys, ys)) / np.sqrt(np.dot(ys_prior, ys_prior)))
    solution = inv(X.T @ X) @ X.T @ (ys + scaled_lmda * ys_prior) / (1.0 + scaled_lmda)
    return solution


if __name__ == "__main__":
    xs = np.array([1, 4, 6, 7, 15])
    ys = xs
    ys_prior = xs * 0.001
    lmbda = 0.0001
    solution = natural_cubic_spline(xs, ys, lmbda, ys_prior)
    print(ys)
    print(ys_prior)
    print(solution)