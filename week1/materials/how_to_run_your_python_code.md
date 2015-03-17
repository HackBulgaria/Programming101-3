# How to test your code

For example, lets imagine that we have a file, called `solution.py` with:

```python
def sum(xs):
    result = 0
    
    for x in xs:
        result += x
    
    return result
```

If we want to test that, we have two options

## Option 1 - using REPL

1. Open a Python REPL
2. Load the function in REPL
3. Call the function with test data

In the above example, we will have to do the following:

**In a terminal window, navigate to the folder, where `solution.py` is located. Then start the REPL:**

```python
$ python
Welcome to Python v 3.4 ....
>>> from solution import sum
>>> sum([1, 2, 3])
6
```

We are using the Python syntax for importing functions from other modules.

[**You can check more about that here**](https://docs.python.org/3.4/tutorial/modules.html)


If you introduce changes in the python file, you will have to **reload the module** from REPL.

This is not the easiest thing to do: https://docs.python.org/3.4/library/importlib.html#importlib.reload


## Option 2 - main() function

The biggest weakness of method 1 is the reloading part.

We want to have a quick feedback-loop when testing our programs.

The second option is to introduce the following code to our `solution.py` function:

```python
def main():
    print(sum([1, 2, 3])
    print(sum(range(1, 10)))

if __name__ == "__main__":
    main()
``` 

The magic part is the `if __name__` one.

Lets see what is happening.

To understand, create two files: `one.py` and `two.py` with identical code:

```python
# for one.py and two.py

print(__name__)
```

If you run both files via Python compiler, you will get:

```
$ python one.py
__main__
$ python two.py
__main__
```

`__main__` is the name of the module and one python file is one module.

**The module gets the name `__main__` if it is executed with the Python compiler!**

Now, change the source of `two.py`:

```python
# two.py
import one

print(__name__)

```

If we execute it:

```
$ python two.py
one
__main__
```

The `__name__` of `one.py` is changed to `one`, because it is not executed via the Python compiler, but imported.

This will help us later on, when we introduce tests.

