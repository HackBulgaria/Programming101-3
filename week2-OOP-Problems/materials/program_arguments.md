# Program Arguments

When we run our Python scripts with `$ python3.4 script.py`, `script.py` is an argument to the Python program.

We can do the same thing with our Python scripts:

```
$ python3.4 cat.py file.txt
```

Here for example, `file.txt` is an argument to the `cat.py` script.

The simplest way to get your arguments is the following:

```python
# argv.py
import sys

for arg in sys.argv:
    print(arg)
```

Now, if we run the following command on the shell, we will see the output:

```
$ python3.4 argv.py hello.txt program.py script.py
argv.py
hello.txt
program.py
script.py
```

__IMPORTANT:__ In Python, the first argument is always the file name!


