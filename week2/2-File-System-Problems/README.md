# Problems with files

## Implement the cat command - Print file contents

In Linux, there is a very useful command, called `cat`:

```
$ cat file.txt
This is some file
And cat is printing it's contents
```

Implement a Python script, called `cat.py` that takes one argument - a filename and prints the contents of that file to the console.

### Boilerplate

```python
# cat.py
import sys


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

If we have `file.txt` in the same directory with `cat.py`, and `file.txt` is with the following text:

```
Python is an awesome language!
You should try it.
```

This is the result:
```
$ python3.4 cat.py file.txt
Python is an awesome language!
You should try it.
```

## Cat multiple files

Implement a Python script, called `cat2.py` that takes multiple arguments - file names and prints the contents of all files to the console, in the order of the arguments.

__The number of the files that are given as arguments is unknown.__

There should be a newline between every two files that are printed.

### Boilerplate

```python
# cat2.py
import sys


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

If we have two files - `file1.txt` and `file2.txt` in the same directory with `cat2.py` and:

__file1.txt:__
```
Python is an awesome language!
You should try it.
```

__file2.txt:__
```
Also, you can use Python at a lot of different places!
```


This is the result:
```
$ python3.4 cat2.py file1.txt file2.txt
Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!
```

## Generate file with random integers

Implement a Python script, called `generate_numbers.py` that takes two arguments - a `filename` and an integer `n`.

The script should create a file with the `filename` and print `n` random integers, separated by `" "`.

For random integers, you can use:

```python
from random import randint
print(randint(1, 1000))
```

### Boilerplate

```python
# generate_numbers.py
import sys
from random import randint


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

```
$ python3.4 generate_numbers.py numbers.txt 100
$ cat numbers.txt
612 453 555 922 120 840 173 98 994 461 392 739 982 598 610 205 13 604 304 591 830 313 534 47 945 26 975 338 204 51 299 611 699 712 544 868 2 80 472 101 396 744 950 561 378 553 777 248 53 900 209 817 546 12 920 219 38 483 176 566 719 196 240 638 812 630 315 209 774 768 505 268 358 39 783 78 94 293 187 661 743 89 768 549 106 837 687 992 422 30 897 174 844 148 88 472 808 598 341 749
```

## Sum integers from file

Implement a Python script, called `sum_numbers.py` that takes one argument - a `filename` which has integers, separated by `" "`.

The script should print the sum of all integers in that file.

### Examples

If we use the generated file from Problem 3:

```
$ python3.4 sum_numbers.py numbers.txt
47372
```

## Implement an alternative to du -h command

In linux, if we want to know the size of a directory, we use the `du` command. For example:

```
$ du -hs /home/radorado/code
2,3G  /home/radorado/code
```

* `-h` flag is for "human readable" which means we get the size in gigabytes, not bytes.
* `-s` flag is for silent. We don't want to print every file that we go through.

In a file called `duhs.py`, implement the logic of `du -hs /some/path`, where `/some/path` is obtained as an argument to the file.

Example usage:

```
$ python3.4 duhs.py /home/radorado/code
/home/radorado/code size is: 2.3G
```

**THIS IS NOT THE SOLUTION WE WANT:**

```python
from subprocess import call
import sys

path = sys.argv[1]

call(["du", "-s", "-h", path])
```

### Hints

* Check the [`os`](https://docs.python.org/3.4/library/os.html) python module.
* Many of the methods raise errors. In order to deal with an error you can do the following things:

```python
try:
    os.something(path)
except FileNotFoundError as error:
    print(error)
```

WHen you `except` the error, it wont crash your program.
