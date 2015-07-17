def fibonacci(n):
    result = []

    a = 1
    b = 1

    while len(result) < n:
        result.append(a)

        next_fib = a + b
        a = b
        b = next_fib


    return result


def factorial(n):
    result = 1

    for x in range(1, n + 1):
        result *= x

    return result


def sum_of_digits(n):
    return sum(to_digits(n))


def to_digits(n):
    return [int(x) for x in str(n)]


# 145  = 1! + 4! + 5!
def factorial_digits(n):
    return sum([factorial(x) for x in to_digits(n)])


def palindrome(obj):
    # list slicing
    return str(obj)[::-1] == str(obj)


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit

    return result


def fibonacci_number(n):
    return to_number(fibonacci(n))


def count_vowels(string):
    vowels = "aeiouyAEIOUY"
    count = 0

    for ch in string:
        if ch in vowels:
            count += 1

    return count

def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    count = 0

    for ch in string:
        if ch in consonants:
            count += 1

    return count


def char_histogram(string):
    result = {}

    for ch in string:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

    return result


def p_score(n):
    if palindrome(n):
        return 1

    s = n + int(str(n)[::-1])

    return 1 + p_score(s)


def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)


def is_hack(n):
    binary_n = bin(n)[2:]

    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))

    return is_palindrome and has_odd_ones


def next_hack(n):
    n += 1

    while not is_hack(n):
        n += 1

    return n
