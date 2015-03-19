from copy import deepcopy

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

def is_number_balanced(n):
    numbs = [int(x) for x in str(n)]
    half = len(numbs) // 2
    left_numbs = numbs[0:half]
    if len(numbs) % 2 == 0: right_numbs = numbs[half:]
    else: right_numbs = numbs[half + 1:]

    left_sum = sum(left_numbs)
    right_sum = sum(right_numbs)

    if left_sum == right_sum:
        return True
    return False

def count_substrings(haystack, needle):
    return haystack.count(needle)

def find_neighbours(matrix,row,i,j):
    neighbours = []
    indexes = [-1, 0, 1]
    for r in indexes:
        for c in indexes:
            if i+r >= 0 and i+r <= len(matrix) - 1 and j+c >= 0 and j+c <= len(row) - 1:
                if not (r == 0 and c == 0):
                    neighbours.append([i+r, j+c])
    return neighbours

def bomb_matrix(matrix,row,i,j):
    bombed_matrix = deepcopy(matrix)
    for element in find_neighbours(matrix, row, i,j):
        if matrix[element[0]][element[1]] - matrix[i][j] >= 0:
            bombed_matrix[element[0]][element[1]] = matrix[element[0]][element[1]] - matrix[i][j]
        else:
            bombed_matrix[element[0]][element[1]] = 0
    return bombed_matrix

def matrix_bombing_plan(matrix):
    result = {}
    for row in matrix:
        i = matrix.index(row)
        for coll in row:
            j = row.index(coll)
            result[(i,j)] = sum_matrix(bomb_matrix(matrix,row,i,j))
    return result