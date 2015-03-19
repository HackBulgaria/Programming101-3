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
