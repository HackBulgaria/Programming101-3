# After we have done our warmup problems

## Sum all divisors of an integer

Given an integer, implement a function, called `sum_of_divisors(n)` that calculates the sum of all divisors of `n`.

For example, the divisors of 8 are 1, 2, 4 and 8 and `1 + 2 + 4 + 8 = 15`.
The divisors of 7 are 1 and 7, which makes the sum = 8.

### Signature

```python
def sum_of_divisors(n):
    pass
```

### Test examples

```python
>>> sum_of_divisors(8)
15
>>> sum_of_divisors(7)
8
>>> sum_of_divisors(1)
1
>>> sum_of_divisors(1000)
2340
```

## Check if integer is prime

Given an integer, implement a function, called `is_prime(n)` which returns True if `n` is a prime number.
You should handle the case with negative numbers too.

A prime number is a number, that is divisible only by 1 and itself.

1 is not considered to be a prime number. [If you are curious why, find out here.](http://www.youtube.com/watch?v=IQofiPqhJ_s)

### Signature

```python
def is_prime(n):
    pass
```

### Test examples

```python
>>> is_prime(1)
False
>>> is_prime(2)
True
>>> is_prime(8)
False
>>> is_prime(11)
True
>>> is_prime(-10)
False
```

## Check if a number has a prime number of divisors

Given an integer, implement a function, called `prime_number_of_divisors(n)`, which returns True if the number of `n`'s divisors is a prime number, False otherwise.

For example, the divisors of 8 are 1, 2, 4 and 8, a total of 4. 4 is not a prime number.
The divisors of 9 are 1, 3 and 9, a total of 3. 3 is a prime number.

### Signature

```python
def prime_number_of_divisors(n):
    pass
```

### Test examples

```python
>>> prime_number_of_divisors(7)
True
>>> prime_number_of_divisors(8)
False
>>> prime_number_of_divisors(9)
True
```

## Number containing a single digit?

Implement a function, called `contains_digit(number, digit)` which checks if `digit` is contained in the given `number`.

`digit` and `number` are integers.

### Signature

```python
def contains_digit(number, digit):
    pass
```

### Test examples

```python
>>> contains_digit(123, 4)
False
>>> contains_digit(42, 2)
True
>>> contains_digit(1000, 0)
True
>>> contains_digit(12346789, 5)
False
```

## Number containing all digits?

Implement a function, called `contains_digits(number, digits)` where `digits` is a __list of integers__ and `number` is an integer.

The function should return True if __all__ `digits` are contained in `number`.

### Signature

```python
def contains_digits(number, digits):
    pass
```

### Test examples

```python
>>> contains_digits(402123, [0, 3, 4])
True
>>> contains_digits(666, [6,4])
False
>>> contains_digits(123456789, [1,2,3,0])
False
>>> contains_digits(456, [])
True
```

## Is number balanced?

A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number `1238033` is balanced, because it's left part is `123` and right part is `033`.

We have : `1 + 2 + 3 = 0 + 3 + 3 = 6`.

A number with only one digit is always balanced!

Implement the function `is_number_balanced(n)` that checks if `n` is balanced.

### Signature

```python
def is_number_balanced(n):
    pass
```

### Test examples

```python
>>> is_number_balanced(9)
True
>>> is_number_balanced(11)
True
>>> is_number_balanced(13)
False
>>> is_number_balanced(121)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True

```

## Counting substrings

Implement the function `count_substrings(haystack, needle)`. It returns the count of occurrences of the string `needle` in the string `haystack`.

__Don't count overlapped substings and take case into consideration!__
For overlapping substrings, check the "baba" example below.

### Signature

```python
def count_substrings(haystack, needle):
    pass
```

### Test examples

```python
>>> count_substrings("This is a test string", "is")
2
>>> count_substrings("babababa", "baba")
2
>>> count_substrings("Python is an awesome language to program in!", "o")
4
>>> count_substrings("We have nothing in common!", "really?")
0
>>> count_substrings("This is this and that is this", "this")  # "This" != "this"
2
```

## Zero Insertion

Given an integer, implement the function `zero_insert(n)`, which returns a new integer, constructed by the following algorithm:

* If two neighboring digits are the same (like `55`), insert a 0 between them (`505`)
* Also, if we add two neighboring digits and take their module by 10 (`% 10`) and the result is 0 - add 0 between them.

For example, if we have the number `116457`, result will be: `10160457`:

* 1 and 1 are the same, so we insert 0 between them
* `6 + 4 % 10 = 0`, so we insert 0 between them.


### Examples

```python
>>> zero_insert(116457)
10160457
>>> zero_insert(55555555)
505050505050505
>>> zero_insert(1)
1
>>> zero_insert(6446)
6040406
```

## Sum Numbers in Matrix

You are given a `NxM` matrix  of integer numbers.

Implement a function, called `sum_matrix(m)` that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in Python.

### Examples:

```python
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum_matrix(m)
45
>>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> sum_matrix(m)
0
>>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> sum_matrix(m)
55
```

## Matrix Bombing

You are givn a `NxM` matrix of integer numbers.

We can drop a bomb at any place in the matrix, which has the following effect:

* All of the **3 to 8 neighbours** (depending on where you hit!) of the target are reduced by the value of the target.
* Numbers can be reduced only to 0 - they cannot go to negative.

For example, if we have the following matrix:

```
10 10 10
10  9  10
10 10 10
```

and we drop bomb at `9`, this will result in the following matrix:

```
1 1 1
1 9 1
1 1 1
```

Implement a function called `matrix_bombing_plan(m)`.

The function should return a dictionary where keys are positions in the matrix, represented as tuples, and values are the total sum of the elements of the matrix, after the bombing at that position.

The positions are the standard indexes, starting from `(0, 0)`

For example if we have the following matrix:

```
1 2 3
4 5 6
7 8 9
```

and run the function, we will have:

```python
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}
```

We can see that if we drop the bomb at `(1, 1)` or `(2, 1)`, we will do the most damage!

