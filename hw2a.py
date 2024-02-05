from math import sqrt, pi, exp


def Probability(PDF, args, c, GT=True):
    """function to calculate the probability that xis >c
    :param PDF: the probability density function to be integrated
    :param args: a tuple with (mean , standard deviation)
    :param c: value for which we ask the probability question
    :param GT: boolean deciding if we want probability x>c (True) or x<c (False)
    :return: probability value
    """
    mu, sig = args
    p = Simpson(PDF, (mu, sig, mu - 5*sig, 0))
    return p


def GNPDF(args):
    """ Here is where we define gaussian Normal Probability Density Function Need population mean(mu)
    and standard deviation(sig) to calculate at any value of x"""

    x, mu, sig = args

    fx = (1/(sig*sqrt(2*pi)))*(exp(-0.5 * (((x-mu)/sig)**2)))
    return fx


def Simpson(fx, args, npoints=20):
    """This function utilizes the Simpson 1/3 rule for integrating"""
    # Simpsons rule: Integral(a-b)f(x) = h/3[f(x0)+4f(x1)+2f(x2)+4f(x3)+...+f(xn)]

    mu, sig, a, c = args
    # a is left limit, c = b or right limit
    h = (c - a) / npoints
    x_values = [a + i * h for i in range(npoints + 1)]
    fx_values = [fx((xi, mu, sig)) for xi in x_values]

    # Sum the even and odd values of fx as prescribed by Simpson's 1/3 rule
    area = (h / 3) * (fx_values[0] + 4 * sum(fx_values[i] for i in range(1, npoints, 2))
                      + 2 * sum(fx_values[i] for i in range(2, npoints - 1, 2)) + fx_values[npoints])

    return area


def Testmain():
    """test function for previous functions"""

    fx = GNPDF((0, 0, 1))
    print("p={:0.5f}".format(fx))

    p = Simpson(GNPDF, (0, 1, -5, 0))
    print("p={:0.5f}".format(p))

    p1 = Probability(GNPDF, (0, 1), 0, True)
    print("p1={:0.5f}".format(p1))

    mu = float(input("Population mean? "))
    sig = float(input("Standard deviation?"))
    c = float(input("c value?"))
    GT = True if input("Probability greater than c?").lower() in ["y", "yes", "true"] else "False"

    print("P(x"+(">" if GT else "<") + c + " | "+mu+", "+sig + ") ")


def main():
    """ main function using the probability function to find the probabilities of x being within a sepcified range"""

    mu1, sig1 = 100, 12.5
    c1 = 105
    p1 = Probability(GNPDF, (mu1, sig1), c1, GT=False)
    print("P(x<{:.2f}|N({},{})) = {:0.2f}".format(c1, mu1, sig1, p1))

    # Example 2
    mu2, sig2 = 100, 3
    c2 = mu2 + 2 * sig2
    p2 = Probability(GNPDF, (mu2, sig2), c2, GT=True)
    print("P(x>{}|N({},{})) = {:0.2f}".format(c2, mu2, sig2, p2))


if __name__ == "__main__":
    main()
    Testmain()
