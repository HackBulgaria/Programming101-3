# 15 warm-up problems

In a file, called `warmup.py`, code the solutions to the following problems:

The solutions should be written in Python 3.

## Factorial

Implement a function that calculates `n!`, by a given integer `n`.

### Signature

```python
def factorial(n):
    pass
```

### Test examples

```python
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(5)
120
```


## First nth members of Fibonacci

The most annoying problem of all. 

Implement a function, called `fibonacci(n)` that returns a list with the first `n` members of the Fibonacci sequence.

### Signature

```python
def fibonacci(n):
    pass
```

### Test examples

```python
>>> fibonacci(1)
[1]
>>> fibonacci(2)
[1, 1]
>>> fibonacci(3)
[1, 1, 2]
>>> fibonacci(10)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

## Sum all digits of a number

Given an integer, implement a function, called `sum_of_digits(n)` that calculates the sum of `n`'s digits.

If a negative number is given, our function should work as if it was positive.

For example, if `n` is `1325132435356`, the digit's sum is 43.
If `n` is -10, the sum is 1 + 0 = 1.

Keep in mind that in Python, there is a special operator for integer division!

```python
>>> 5 / 2
2.5
>>> 5 // 2
2
```

### Signature

```python
def sum_of_digits(n):
    # implementation
```

### Test examples

```python
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1
```

## Factorial Digits

Implement a function `fact_digits(n)`, that takes an integer and returns the sum of the factorials of each digit of `n`.

For example, if `n = 145`, we want `1! + 4! + 5!`

### Signature

```python
def fact_digits(n):
    pass
```

### Test examples

```python
>>> fact_digits(111)
3
>>> fact_digits(145)
145
>>> fact_digits(999)
1088640
```

## Palindrome

Implement a function, called `palindrome(obj)`, which takes an object (could be anything) and checks if it's string representation is a palindrome.

For example, the integer `121` and the string `"kapak"` are palindromes. The function should work with both.

**Hint - check Python's `[str](https://docs.python.org/3/library/stdtypes.html#str)` function**

### Signature

```python

def palindrome(obj):
    pass
```

### Test examples

```python
>>> palindrome(121)
True
>>> palindrome("kapak")
True
>>> palindrome("baba")
False
```

## Turn a number into a list of digits

Implement a function, called `to_digits(n)`, which takes an integer `n` and returns a list, containing the digits of `n`.

### Signature

```python
def to_digits(n):
    pass
```

### Test examples

```python
>>> to_digits(123)
[1, 2, 3]
>>> to_digits(99999)
[9, 9, 9, 9, 9]
>>> to_digits(123023)
[1, 2, 3, 0, 2, 3]
```

## Turn a list of digits into a number

Implement a function, called `to_number(digits)`, which takes a list of integers - `digits` and returns the number, containing those digits.

### Signature

```python
def to_number(digits):
    pass
```

### Test examples

```python
>>> to_number([1,2,3])
123
>>> to_number([9,9,9,9,9])
99999
>>> to_number([1,2,3,0,2,3])
123023
```

## Fibonacci number

Implement a function, called `fib_number(n)`, which takes an integer `n` and returns a number, which is formed by concatenating the first `n` Fibonacci numbers.

For example, if `n = 3`, the result s `112`

### Signature

```python
def fib_number(n):
    pass
```

### Test examples

```python
>>> fib_number(3)
112
>>> fib_number(10)
11235813213455
```

## Vowels in a string

Implement a function, called `count_vowels(str)`, which returns the count of all vowels in the string `str`.

__Count uppercase vowels aswell!__

The English vowels are `aeiouy`.

### Signature

```python
def count_vowels(str):
    pass
```

### Test examples

```python
>>> count_vowels("Python")
2
>>> count_vowels("Theistareykjarbunga") #It's a volcano name!
8
>>> count_vowels("grrrrgh!")
0
>>> count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
22
>>> count_vowels("A nice day to code!")
8
```

## Consonants in a string

Implement a function, called `count_consonants(str)`, which returns the count of all consonants in the string `str`.

__Count uppercase consonants as well!__

The English consonants are `bcdfghjklmnpqrstvwxz`.

### Signature

```python
def count_consonants(str):
    # Implementation
```

### Test examples

```python
>>> count_consonants("Python")
4
>>> count_consonants("Theistareykjarbunga") #It's a volcano name!
11
>>> count_consonants("grrrrgh!")
7
>>> count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
44
>>> count_consonants("A nice day to code!")
6
```

## Char Histogram

Implement a funcion, called `char_histogram(string)`, which takes a string and returns a dictionary, where each key is a character from `string` and its value is the number of occurrences of that char in `string`.

### Signature

```python
def char_histogram(string):
    pass
```

### Test examples

```python
>>> char_histogram("Python!")
{ 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 }
>>> char_histogram("AAAAaaa!!!")
{ 'A': 4, 'a': 3, '!": 3 }
```

## Palindrome Score

We denote the "Palindrome score" of an integer by the following function:

* `P(n) = 1`, if `n` is palindrome
* `P(n) = 1 + P(s)` where `s` is the sum of `n` and the `reverse of n`

Implement a function, called `p_score(n)`, which finds the palindrome score for n.

Lets see two examples:

* `p_score(121) = 1`, because `121` is a palindrome.
* `p_score(48) = 3`, because: 

1. `P(48) = 1 + P(48 + 84) = 132`
2. `P(132) = 1 + 1 + P(132 + 321 = 363)`
3. `P(363) = 1`.
4. When we return from the recursion, we get 3.

### Signature

```python
def p_score(n):
    pass
```

### Test examples

```python
>>> p_score(121)
1
>>> p_score(48)
3
>>> p_score(198)
6
```

## Increasing sequence?

Implement a function, called `is_increasing(seq)` where `seq` is a list of integers.

The function should return True, if the given sequence is monotonously increasing.

And before you skip this problem, because of the math terminology, let me explain:

**A sequence is monotonously increasing if for every two elements a and b, that are next to each other (a is before b), we have a < b**

For example, `[1,2,3,4,5]` is monotonously increasing, but `[1,2,3,4,5,1]` is not.

### Signature

```python
def is_increasing(seq):
   pass 
```

### Test examples

```python
>>> is_increasing([1,2,3,4,5])
True
>>> is_increasing([1])
True
>>> is_increasing([5,6,-10])
False
>>> is_increasing([1,1,1,1])
False
```

## Descreasing sequence?

Implement a function, called `is_decreasing(seq)` where `seq` is a list of integers.

The function should return True, if the given sequence is monotonously decreasing.

And before you skip this problem, because of the math terminology, let me explain:

**A sequence is monotonously decreasing if for every two elements a and b, that are next to each other (a is before b), we have a > b**

For example, `[5,4,3,2,1]` is monotonously decreasing, but `[1,2,3,4,5,1]` is not.

### Signature

```python
def is_decreasing(seq):
    pass 
```

### Test examples

```python
>>> is_decreasing([5,4,3,2,1])
True
>>> is_decreasing([1,2,3])
False
>>> is_decreasing([100, 50, 20])
True
>>> is_decreasing([1,1,1,1])
False
```

## Hack Numbers

A hack number is an integer, that matches the following criteria:

* The number, represented in binary, is a palindrome
* The number, represented in binary, has an odd number of 1's in it

Example of hack numbers:

* 1 is `1` in binary
* 7 is `111` in binary
* 7919 is `1111011101111` in binary

Implement a function, called `next_hack(n)` that takes an integer and returns the next hack number, that is bigger than `n`


### Signature

```python
def next_hack(n):
    pass
```


### Test examples

```python
>>> next_hack(0)
1
>>> next_hack(10)
21
>>> next_hack(8031)
8191
```
