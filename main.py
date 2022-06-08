#adar katzir 209502293
import math

def f(x):
    return math.sin(2*math.e**(-2*x))/(2*x**3+5*x**2-6)



def simpson(ll, ul, n):

    h = (ul - ll) / n

    x = list()
    fx = list()

    i = 0
    while i <= n:
        x.append(ll + i * h)
        fx.append(f(x[i]))
        i += 1

    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
        i += 1
    res = res * (h / 3)
    return res


if __name__ == "__main__":
    lower_limit = -0.5
    upper_limit = 0.5
    n = 10
    epsilon = 1e-6

    temp_return_val = simpson(lower_limit, upper_limit, n)

    while epsilon >= 1e-6:
        print(f"n = {n}, Answer = {temp_return_val}")
        n *= 2
        return_val = simpson(lower_limit, upper_limit, n)
        epsilon = abs(temp_return_val - return_val)
        if epsilon >= 1e-6:
            temp_return_val = return_val
        else:
            n /= 2

    print(
        f"Section [{lower_limit}, {upper_limit}] is divided into n = {int(n)} "
        f"equal sections in order to achieve the accuracy of 0.0001")
    print(f"Answer = {temp_return_val}")
