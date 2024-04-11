# given a number if stairs, how many ways
# can a person climb, give that a person
# can only take 1 or 2 steps at a time
import math


def number_of_ways(number_of_stairs):

    if number_of_stairs == 1:
        return 1

    elif number_of_stairs == 2:
        return 2

    else:

        return number_of_ways(number_of_stairs - 1) + number_of_ways(
            number_of_stairs - 2
        )


if __name__ == "__main__":
    print(number_of_ways(2))
