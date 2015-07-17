import calendar


def count_words(words):
    return {key: words.count(key) for key in words}


def unique_words(words):
    return len([key for key in count_words(words)])


def unique_words2(words):
    return len(set(words))


def dedup(items):
    found = set()
    result = []

    for item in items:
        if item not in found:
            result.append(item)
            found.add(item)

    return result


def nan_expand(times):
    result = ""
    if times == 0:
        return ""

    for i in range(times):
        result += "Not a "
    result += "NaN"

    return result


def iterations_of_nan_expand(expanded):
    nan_table = {}
    n = len(expanded)

    current_index = 0

    while True:
        current_expand = nan_expand(current_index)
        nan_table[current_expand] = current_index

        if len(current_expand) > n:
            break

    if expanded in nan_table:
        return nan_table[expanded]

    return False


def iterations_of_nan_expand2(expanded):
    if nan_expand(expanded.count("Not a")) == expanded:
        return expanded.count("Not a")
    return False


def is_prime(n):
    if n <= 1:
        return False

    start = 2

    while start < n:
        if n % start == 0:
            return False

        start += 1

    return True


def next_prime(n):
    n += 1

    while not is_prime(n):
        n += 1

    return n


def divide_count(n, k):
    times = 0

    while n != 1 and n % k == 0:
        times += 1
        n = n // k

    return times


def prime_factorization(n):
    result = []

    current_prime = 2

    while n != 1:
        times = divide_count(n, current_prime)

        if times != 0:
            result.append((current_prime, times))
            n = n // current_prime ** times

        current_prime = next_prime(current_prime)

    return result


def counter_of_dividers(n, prime_number):
    divider_counter = 0
    while n % prime_number == 0:
        divider_counter += 1
        n /= prime_number
    return divider_counter


def prime_factorization2(n):
    primes = [x for x in range(2, n+1) if is_prime(x)]
    return [(num, counter_of_dividers(n, num)) for num in primes if counter_of_dividers(n, num) != 0]


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and items[index] == first:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])


def reduce_file_path(path):
    result = []
    parts = [part for part in path.split("/") if part not in [".", ""]]

    while len(parts) != 0:
        part = parts.pop()

        if part == "..":
            if len(parts) != 0:
                parts.pop()
        else:
            result.insert(0, part)

    return "/" + "/".join(result)


def reduce_file_path2(path):
    result = "/"
    folders = [word for word in path.split("/") if word != "" and word != "."]
    l = len(folders)
    locations = [folders[i] for i in range(l - 1) if folders[i] != ".." and i + 1 <= l and folders[i  +1] != ".."]

    if l != 0 and folders[l-1] != "..":
        locations.append(folders[l-1])

    result += "/".join(locations)

    return result


def groupby(func, seq):
    result = {}

    for element in seq:
        if func(element) in result:
            result[func(element)].append(element)
        else:
            result[func(element)] = [element]

    return result


def prepare_meal(number):
    result = ""
    count3 = 0
    while number % 3 == 0:
        count3 += 1
        number /= 3

    result += " ".join(["spam" for i in range(count3)])
    if number % 5 == 0:
        result += " ".join(["eggs" if count3 == 0 else " and eggs"])

    return result


def same_characters(letter, string):
    return all([letter == ch for ch in string])


def is_an_bn(word):
    word_length = len(word)
    if word_length % 2 == 0:
        a = word[: word_length // 2]
        b = word[word_length // 2:]

        return same_characters("a", a) and same_characters("b", b)

    return False


def to_digits(n):
    return [int(x) for x in str(n)]


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def is_credit_card_valid(number):
    s = 0
    numbs = to_digits(number)

    if count_digits(number) % 2 != 0:
        for i in range(len(str(number))):
            if i % 2 == 0:
                s += numbs[i]
            else:
                s += sum(to_digits(numbs[i] * 2))

        return s % 10 == 0

    return False


def goldbach(n):
    primes = [x for x in range(2, n+1) if is_prime(x)]
    combos = []
    for n1 in primes:
        if n1 <= n / 2:
            combos.append([(n1, n2) for n2 in primes if n1 + n2 == n])

    return [combo[0] for combo in combos if combo != []]


def magic_square(matrix):
    s = []

    # Sum of rows:
    for row in matrix:
        s.append(sum(row))
    
    # Sum of columns:
    for i in range(0, len(matrix)):
        s.append(sum([row[i] for row in matrix]))
    
    # Sum of diagonals:
    s.append(sum([matrix[i][i] for i in range(len(matrix))]))

    i = 0
    result = 0
    for j in range(len(matrix) - 1, -1, -1):
        result += matrix[i][j]
        i += 1
    s.append(result)

    return all([s[0] == s[i] for i in range(len(s))])


FRIDAY_INDEX = 4
def friday_years(start, end):
    count_friday_years = 0

    for year in range(start, end):
        count_fidays_in_year = 0
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            for week in month_calendar:
                if week[FRIDAY_INDEX] != 0:
                    count_fidays_in_year += 1

        if count_fidays_in_year == 53:
            count_friday_years += 1

    return count_friday_years
