def fibonacci(n):
    fib_series = [1, 1]

    if n >= 3:
        for x in range(2, n):
            fib_series.append(fib_series[x - 1] + fib_series[x - 2])

        return fib_series[n - 1]

    elif n == 1 or n == 2:
        return 1


if __name__ == "__main__":
    print(fibonacci(2))
