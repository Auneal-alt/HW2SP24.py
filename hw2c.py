import numpy as np


def GaussSeidel(Aaug, x, Niter=15):
    """Gauss-Seidel method for solving a system of equations
    :param Aaug: The augmented matrix from Ax=b -> [A|b]
    :param x:  An initial guess for the x vector. if A is nxn, x is nx1
    :param Niter:  Number of iterations to run the GS method
    :return: the solution vector x
    """

    A = Aaug[:, :-1]
    b = Aaug[:, -1]
    N = len(b)

    for _ in range(Niter):
        for i in range(N):
            sigma = sum(A[i, j] * x[j] for j in range(N) if j != i)
            x[i] = (b[i] - sigma) / A[i, i]

    return x


def MakeDiagDom(A):
    """Reorders the rows of matrix A to put the largest absolute values along the diagonal.
    Parameters:A: The matrix to sort
    Returns:The sorted matrix
    """
    n = len(A)
    sorted_indices = np.argsort(np.abs(A), axis=1)[:, ::-1]

    sorted_A = np.array([A[i, sorted_indices[i]] for i in range(n)])

    return sorted_A


def main():
    """Function to solve linear algebra by running the functions GaussSeidel and makeDiagDom"""
    # Problem 1 Array 3 algebra wih 3 unknowns, 4th number of each row is what the equation equals
    Aaug1 = np.array([[3, 1, -1, 2],
                      [1, 4, 1, 12],
                      [2, 1, 2, 10]])

    x1 = np.zeros(len(Aaug1[0]) - 1)
    Aaug1_diag_dom = MakeDiagDom(Aaug1)
    solution1 = GaussSeidel(Aaug1_diag_dom, x1)
    print("Solution for Problem 1:", solution1)

    # Problem 2 Array 4 algebra equations with 4 unknowns with 5th value being what its equal to
    Aaug2 = np.array([[1, -10, 2, 4, 2],
                      [3, 1, 4, 12, 12],
                      [9, 2, 3, 4, 21],
                      [-1, 2, 7, 3, 37]])

    x2 = np.zeros(len(Aaug2[0]) - 1)
    Aaug2_diag_dom = MakeDiagDom(Aaug2)
    solution2 = GaussSeidel(Aaug2_diag_dom, x2)
    print("Solution for Problem 2:", solution2)


if __name__ == "__main__":
    main()
