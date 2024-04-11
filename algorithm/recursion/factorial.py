# the mathematical formulae for factorial
# is; n! = n*(n-1)*(n-2)...*1


# def factorials(n):
#     res = 1
#     expr = ""
#
#     if n == 0:
#         print(1)
#
#     else:
#         factorial_range = range(n, 0, -1)
#
#         for i in factorial_range:
#             expr += "*{}".format(i) if i != n else "{}".format(i)
#             res = res * i
#
#     return n, expr, res

# if __name__ == "__main__":
#     (number, expression, result) = factorials(1)
#     print("Factorial of {} is {} = {}".format(number, expression, result))


# Using Recursion method
def factorials(n):
    re = 1

    if n >= 1:
        return n * factorials(n - 1)

    else:
        return 1


if __name__ == "__main__":
    res = factorials(5)
    print(res)


# 9aae70272ccfb9a26a99ff4c2bbee3c428f1b979
