# the mathematical formulae for factorial
# is; n! = n*(n-1)*(n-2)...*1


def factorials(n):
    res = 1
    expr = ""

    if n == 0:
        print(1)

    else:
        factorial_range = range(n, 0, -1)

        for i in factorial_range:
            expr += "*{}".format(i) if i != n else "{}".format(i)
            res = res * i

    return n, expr, res


if __name__ == "__main__":
    (number, expression, result) = factorials(1)
    print("Factorial of {} is {} = {}".format(number, expression, result))
