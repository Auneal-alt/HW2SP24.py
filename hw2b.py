from math import cos


def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """Function uses the secant method to find the root of the given function (fcn)
    fcn: the function for which we want to find the root
    x0 and x1: two x values in the neighborhood of the root
    xtol: exit if the |xnewest - xprevious| < xtol
    maxiter: exit if the number of iterations (new x values) equals this number
    return value: the final estimate of the root (most recent new x value)"""
    # Secant Method Equation x(n+1) = xn - {[(fxn)*(xn - xn-1)] / [(fxn) - (fxn-1)]}

    # Asked for help with this keep this section of code so I can review a while loop when I have time

    # Create the starting point of the iterations for the loop, so it begins at 1 instead of 0
    I = 0

    # Use a while loop to attain the values of |x0-x1|<xtol with the iterations(I)<=maxiter
    while abs(x0 - x1) >= xtol and I <= maxiter:
        # Create the equation for the Secant Method
        x2 = x1 - (fcn(x1) * (x1 - x0)) / (fcn(x1) - fcn(x0))
        x0 = x1
        x1 = x2
        # Tell the computer to add to the values of iterations(I) that'll keep count so it doesn't exceed maxiter
        I += 1
        return x2


def main():
    """Main function to find the next x root value in the sequence of fcn(x)"""
    # the 3 functions we want the root of
    def f1(x): return x - 3*cos(x)
    def f2(x): return cos(2 * x) * (x**3)
    # function 2 and function 3 are the same but the maxiter is different for solution 3

    Solution1 = Secant(f1, x0=1, x1=2, maxiter=5, xtol=1e-4)
    print("root for solution 1 is: {:0.6f}".format(Solution1))

    Solution2 = Secant(f2, x0=1, x1=2, maxiter=15, xtol=1e-8)
    print("root for solution 2 is: {:0.6f}".format(Solution2))

    Solution3 = Secant(f2, x0=1, x1=2, maxiter=3, xtol=1e-8)
    print("root for solution 3 is: {:0.6f}".format(Solution3))


if __name__ == "__main__":
    main()
