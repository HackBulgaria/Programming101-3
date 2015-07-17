import copy
import pprint


def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def count_of_divisors(n):
    return sum([1 for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def prime_number_of_divisors(n):
    is_prime(count_of_divisors(n))


def to_digits(n):
    return [int(x) for x in str(n)]


def contains_digit(number, digit):
    return digit in to_digits(number)


def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False

    return True


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit

    return result


def is_number_balanced(n):
    numbs = to_digits(n)
    half = len(numbs) // 2

    left_numbs = numbs[0:half]
    if len(numbs) % 2 == 0:
        right_numbs = numbs[half:]
    else:
        right_numbs = numbs[half + 1:]

    return sum(left_numbs) == sum(right_numbs)


def count_substrings(haystack, needle):
    return haystack.count(needle)


def zero_insert(n):
    result = []
    digits = to_digits(n)

    start = 0
    end = len(digits)

    while start < end - 1:
        x = digits[start]
        y = digits[start + 1]

        result.append(x)

        if (x + y) % 10 == 0 or x == y:
            result.append(0)

        start += 1

    result.append(digits[start])

    return to_number(result)


def sum_matrix(matr):
    result = 0

    for row in matr:
        result += sum(row)

    return result


def sum_matrix2(matr):
    # Using list comprehensions
    return sum([sum(row) for row in matr])


# We are centered at 4.
# How to move to get to 4's neighbors
# 1      2     3
# 8     >4<    7
# 9      5     6
NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 8 and 7
    (-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_bombing_plan(m)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)

if __name__ == '__main__':
    main()

