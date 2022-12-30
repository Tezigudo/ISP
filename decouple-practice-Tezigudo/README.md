## Practice Externalizing Data

Use `python-decouple` to externalize hard-coded values
in `announcement.py`.

### Installation

If you do not have `python-decouple` installed, install it using:
```shell
  pip install python-decouple
```

### How to Use decouple

Consider this stupid example:

```python
def showfile(filename):
    with open(filename) as file:
        line = 0
        # display only first few lines
        while line < 10:
            print(file.readline(), end="")
            line += 1

if __name__ == '__main__':
    showfile("README.md")
```

This script contains 2 constants that may change: 1) the filename, 2) number of lines to print (10).

Using Python-decouple you put the data in a file named `.env` and
have python-decouple read them:

File: `.env`
```
# name of the file to show
FILENAME = README.md
# how many lines to show (default is 10)
LINE_COUNT = 5
```
You can use any variable names (left side of `=`) but the names
must match what you use in code.

Then in the Python code use:
```python
from decouple import config


def showfile(filename):
    max_lines = config('LINE_COUNT', cast=int, default=10)
    with open(filename) as file:
        line = 0
        # display only first few lines
        while line < max_lines:
            print(file.readline(), end="")
            line += 1

if __name__ == '__main__':
    FILENAME = config('FILENAME')
    showfile(FILENAME)
```

Things to note are:

1. Cast to the datatype you want.  Default is string.
   ```python
   max_lines = config('LINE_COUNT', cast=int)
   ```
2. Can (and should) supply default values in case some value is not in the '.env' file:
   ```python
   max_lines = config('LINE_COUNT', cast=int, default=10)
   ```
3. In `.env` you can use spaces and blank lines, and do not need to quote strings.

### Reading a List of Values

Suppose we have a list of data values:
```python
fruit = ['Apple', 'Banana', 'Orange']
```

Externalize the names of fruit like this:
```
# .env file
FRUIT = Apple, Banana, Orange
```
and in code use:
```python
from decouple import config, Csv

fruit = config("FRUIT", cast=Csv(), default="Grapes")
```

## Assignment

1. In the code `announcement.py` externalize **five** constants that are data the may change.

2. Put the actual data files in a file named `.env` and commit this file to git. Here's an example:
   ```
   # True if class meeting is online, False if at KU
   CLASS_ONLINE = True
   ```

3. In `announcement.py`, use `decouple.config` to get the data.  Supply sensible default values for all externalized data.
   - For the list of topics, use the default "TBA" ("to be announced").

4. Rerun the code. It should still work.

5. Do this (really *do it*):
   - change the data in `.env` and observe how the output of the program changes
   - comment out (`#`) some values in `.env` and observe that default values are used.

6. Push your work to Github.
