# Some serious problems reside here!

## Count words

Given a list of strings, implement a function, called `count_words(arr)` which returns a dictionary of the following kind:

```python
{ "word" : count }
```

Where `count` is the count of occurrences of the __word__ in the list `arr`.


### Signature

```python
def count_words(arr):
    pass
```

### Test examples

```python
>>> count_words(["apple", "banana", "apple", "pie"])
{'apple': 2, 'pie': 1, 'banana': 1}
>>> count_words(["python", "python", "python", "ruby"])
{'ruby': 1, 'python': 3}
```

## Unique words

Implement a function, called `unique_words_count(arr)` which returns the number of different words in `arr`.

`arr` is a list of strings.

### Signature

```python
def unique_words_count(arr):
    pass
```

### Test examples

```python
>>> unique_words_count(["apple", "banana", "apple", "pie"])
3
>>> unique_words_count(["python", "python", "python", "ruby"])
2
>>> unique_words_count(["HELLO!"] * 10)
1
```

## NaN Expand

In most programming languages, `NaN` stands for `Not a Number`.

If we take a look at the following JavaScript code:

```javascript
typeof NaN === 'number' // true
```

We will see that in JavaScript, `NaN` stands for `Not a NaN`, which is recursive by nature.

Implement a Python function, called `nan_expand(times)`, which returns the expansion of `NaN` (In JavaScript terms :P) that many `times`.

For example:

* If we expand `NaN` once (`times=1`), we will have `"Not a NaN"`
* If we expand `NaN` twice (`times=2`), we will have `"Not a Not a NaN"`
* If `times=3`, we have `"Not a Not a Not a NaN"`
* And so on ...

### Examples

```python
>>> nan_expand(0)
""
>>> nan_expand(1)
"Not a NaN"
>>> nan_expand(2)
"Not a Not a NaN"
>>> nan_expand(3)
"Not a Not a Not a NaN"
```

## Iterations of NaN Expand

Implement a function, called `iterations_of_nan_expand(expanded)` that takes a string `expanded`,
which is an unkown iteration of NaN Expand (check the problem for more information)

The function should return the number of iterations that have been made, in order to get to `expanded`.

For example, if we have `"Not a Not a Not a NaN"` - this is the 3rd iteration of `NaN`.

**If `expanded` is not a valid NaN expand string, the function should return false! (This is the hard part)**

### Examples

```python
>>> iterations_of_nan_expand("")
0
>>> iterations_of_nan_expand("Not a NaN")
1
>>> iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
10
>>> iterations_of_nan_expand("Show these people!")
False
```

## Integer prime factorization

Given an integer `n`, we can factor it in the following form:

```
n = p1^a1 * p2^a2 * ... * pn^an
```

Where each `p` is a prime number and each `a` is an integer and `p^a` means `p` to the power of `a`.

[This is called prime factorization.](http://mathworld.wolfram.com/PrimeFactorization.html)

Lets see few examples:

```
10 = 2^1 * 5^1
25 = 5^2
356 = 2^2 * 89 ^ 1
```

Implement a function, called `prime_factorization(n)`, which takes an integer and returns a list of tuples `(pi, ai)` that is the result of the factorization.

The list should be sorted in increasing order of the prime numbers.

### Signature

```python
def prime_factorization(n):
    pass
```

### Test examples

```python
>>> prime_factorization(10)
[(2, 1), (5, 1)] # This is 2^1 * 5^1
>>> prime_factorization(14)
[(2, 1), (7, 1)]
>>> prime_factorization(356)
[(2, 2), (89, 1)]
>>> prime_factorization(89)
[(89, 1)] # 89 is a prime number
>>> prime_factorization(1000)
[(2, 3), (5, 3)]
```

## The group function

We are going to implement a very helpful function, called `group`.

`group` takes a list of things and returns a list of group, where each group is formed by all **equal consecutive elements** in the list.


For example:

```python
group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]
group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]]
```

## Longest subsequence of equal consecutive elements

Implement the function `max_consecutive(items)`, which takes a list of things and returns an integer - the count of elements in the longest subsequence of equal consecutive elements.

For example, in the list `[1, 2, 3, 3, 3, 3, 4, 3, 3]`, the result is 4, where the longest subsequence is formed by `3, 3, 3, 3`

### Signature

```python
def max_consecutive(items):
    pass
```

### Test examples

```python
>>> max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])
4
>>> max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
3
```

## Group By

This problem is from the [Python 2013 course in FMI](http://2013.fmi.py-bg.net/).
You can see the original problem statement here - http://2013.fmi.py-bg.net/tasks/2

Implement a function, called `groupby(func, seq)` that returns a dictionary, which keys are determined by the `func` argument.

The values are items from `seq`.

### Signature

```python
def groupby(func, seq):
    pass
```

### Test examples

```python
>>> groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7])
{0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
>>> groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
{'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
>>> groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7])
{0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}
```

## Spam and Eggs

This is a problem from the [Python 2012 course in FMI](http://2012.fmi.py-bg.net/).

You can see the original problem statement here - http://2012.fmi.py-bg.net/tasks/1

Implement a function, called `prepare_meal(number)` that takes an integer and returns a string, generated by the following algorithm:

__Еggs:__

If there is an integer `n`, such that `3^n` divides `number` and `n` is the largest possible,
the result should be a string, containing `n` times `spam`.

For example:

```python
>>> prepare_meal(3)
'spam'
>>> prepare_meal(27)
'spam spam spam'
>>> prepare_meal(7)
''
```

__Spam:__

If number is divisible by 5, add `and eggs` to the result.

For example:

```python
>>> prepare_meal(5)
'eggs'
>>> prepare_meal(15)
'spam and eggs'
>>> prepare_meal(45)
'spam spam and eggs'
```

__Notice that in the first case, there is no "and". In the rest - there is.__

### Signature

```python
def prepare_meal(number):
    pass
```

### Test examples

```python
>>> prepare_meal(5)
"eggs"
>>> prepare_meal(3)
"spam"
>>> prepare_meal(27)
"spam spam spam"
>>> prepare_meal(15)
"spam and eggs"
>>> prepare_meal(45)
"spam spam and eggs"
>>> prepare_meal(7)
""
```

## Reduce file path

A file path in a Unix OS looks like this - `/home/radorado/code/hackbulgaria/week0`

We start from the root - `/` and we navigate to the destination fodler.

But there is a problem - if we have `..` and `.` in our file path, it's not clear where we are going to end up.

* `..` means to go back one directory
* `.`  means to stay in the same directory
* we can have more then one `/` between the directories - `/home//code`

So for example : `/home//radorado/code/./hackbulgaria/week0/../` reduces to `/home/radorado/code/hackbulgaria`.


Implement a function, called `reduce_file_path(path)` which takes a string and returns the reduced version of the path.

* Every `..` means that we have to go one directory back
* Every `.` means that we are staying in the same directory
* Every extra `/` is unnecessary
* Always remove the last `/`

### Signature

```python
def reduce_file_path(path):
    pass
```

### Test examples

```python
>>> reduce_file_path("/")
"/"
>>> reduce_file_path("/srv/../")
"/"
>>> reduce_file_path("/srv/www/htdocs/wtf/")
"/srv/www/htdocs/wtf"
>>> reduce_file_path("/srv/www/htdocs/wtf")
"/srv/www/htdocs/wtf"
>>> reduce_file_path("/srv/./././././")
"/srv"
>>> reduce_file_path("/etc//wtf/")
"/etc/wtf"
>>> reduce_file_path("/etc/../etc/../etc/../")
"/"
>>> reduce_file_path("//////////////")
"/"
>>> reduce_file_path("/../")
"/"
```

## Word from a^nb^n

Implement a function, called `is_an_bn(word)` that checks if the given `word` is from the `a^nb^n for n>=0` language.
Here, `a^n` means a to the power of n - __repeat the character "a" n times.__

Lets see few words from this language:

* for `n = 0`, this is the empty word `""`
* for `n = 1`, this is the word `"ab"`
* for `n = 2`, this is the word `"aabb"`
* for `n = 3`, this is the word `"aaabbb"`
* and so on - first, you repeat the character "a" n times, and after this - repeat "b" n times

The function should return True if the given `word` is from `a^nb^n for n>=0"` for some n.

### Signature

```python
def is_an_bn(word):
    pass
```

### Test examples

```python
>>> is_an_bn("")
True
>>> is_an_bn("rado")
False
>>> is_an_bn("aaabb")
False
>>> is_an_bn("aaabbb")
True
>>> is_an_bn("aabbaabb")
False
>>> is_an_bn("bbbaaa")
False
>>> is_an_bn("aaaaabbbbb")
True
```

## Credit card validation

Implement a function, called `is_credit_card_valid(number)`, which returns True/False based on the following algorithm:

* Each credit card number must contain odd count of digits.
* We transform the number with the following steps (based on the fact that we start from index 0)
  - All digits, read from right to left, at even positions (index), **remain the same.**
  - Every digit, read from right to left, at odd position is replaced by the result, that is obtained from doubling the given digit.
* After the transformation, we find the sum of all digits in the transformed number.
* The number is valid, if the sum is divisible by 10.

For example: `79927398713` is valid, bacause:

* When we double and replace all digits at odd position we get: `7 (18 = 2 * 9) 9 (4 = 2 * 2) 7 (6 = 2 * 3) 9 (16 = 2 * 8) 7 (2 = 2 * 1) 3`
* The sum of all digits of the new number is 70, which is divisible by 10 => the card number is valid.

More examples:

* `79927398713` is a valid number
* `79927398715` is invalid number

## Goldbach Conjecture

Implement a function, called `goldbach(n)` which returns a list of tuples, that is the goldbach conjecture for the given number `n`.

The Goldbach Conjecture states:

> Every even integer greater than 2 can be expressed as the sum of two primes.

Keep in mind that there can be more than one combination of two primes, that sums up to the given number.

__The result should be sorted by the first item in the tuple.__

For example:

* `4 = 2 + 2`
* `6 = 3 + 3`
* `8 = 3 + 5`
* `10 = 3 + 7 = 5 + 5`
* `100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53`

### Signature

```python
def goldbach(n):
    pass
```

### Test examples

```python
>>> goldbach(4)
[(2,2)]
>>> goldbach(6)
[(3,3)]
>>> goldbach(8)
[(3,5)]
>>> goldbach(10)
[(3,7), (5,5)]
>>> goldbach(100)
[(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
```

## Magic Square

Implement a function, called `magic_square(matrix)` that checks if the given array of arrays `matrix` is a magic square.

A magic square is a square matrix where the numbers in each row, and in each column, and the numbers in the forward and backward main diagonals, all add up to the same number.

### Signature

```python
def magic_square(matrix):
    pass
```
### Test examples

```python
>>> magic_square([[1,2,3], [4,5,6], [7,8,9]])
False
>>> magic_square([[4,9,2], [3,5,7], [8,1,6]])
True
>>> magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]])
True
>>> magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]])
True
>>> magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]])
False
```

## Friday Years

Have you every wondered how many fridays are there in one year?

The count can be 52 or 53, depending on the weeks of that year (leap or not) and the start of the year.

If an year contains 53 fridays, we call that **"A Friday Year"**

You are to implement a function, called `friday_years(start, end)`, where `start` and `end` are integers, representing years.

The function should return the count of all friday years between `[start, end]`


Examples:

```python
>>> friday_years(1000, 2000)
178
>>> friday_years(1753, 2000)
44
>>> friday_years(1990, 2015)
4
```
