## Unit Testing Exercises

These exercises accompany the ISP unit testing presentation:
<https://cpske.github.io/ISP/testing/PythonUnitTesting.pdf>


### 1. Write Tests of `sqrt`

Please do these tests in order.

1. Create a class named `TestMath` in file `test_math.py`. (This is Python's naming convention.)
   ```python
   import unittest

   class TestMath(unittest.TestCase):
       """Test of Python math functions."""

       def test_sqrt(self):
           """Test square root of some typical values."""

   ```

2. Write a `test_sqrt` method containing these (hopefully) passing tests:
   - typical values:  test some values where you know the exact square root.
   - edge case:  the square root 0 should be 0
   - extreme case: the square root of 9.0E+300 should be 3.0E+150
   - extreme case: test the square root of a very small value (e.g 1E-200)

3. Run the tests using `python -m unittest -v test_math.py` (or let PyCharm run them for you).
   - Do the tests **all** run?  all pass?  
   >no
   - If not, review your tests.
   > because my logic error in the last testcase sqrt of 1e-100 shoud equal to 1e-50, I think decimal must be ie-200, when I review it by small decimal and i got it.

4. Write a new test that should **fail**, so you can see the failure message.

5. Write a new test that should **error**, such as `test_sqrt_of_negative_value`.

6. Run the tests again. What is the difference between a "failed" and "error" result?
   >if it Error it will display same as console the message "Error" and if it fail it will be AssertionError

7. Write a new test that *expects* an exception to be thrown.
   ```python
   def test_sqrt_raises_exception(self):
       with unittest.assertRaises(ValueError):
           ...some sqrt() invocation that raises error
   ```

8. Numerical calculations are not always exact. Write a new test of some square roots that are inexact, such as sqrt(2).
   There are 2 ways to specify accuracy to use in the test:
   - **absolute error**: compare results to `n` decimal places
     ```python
     assertAlmostEqual(expected, actual, places=n)
     ```
   - **relative error**: difference between expected and actual result given as a fraction of expected result
      ```python
      assertAlmostEqual(expected, actual, delta=relative_err)
     ```

9.  Commit this file and push to Github.

### 2. Test and Code a `unique` function

In Test Driven Development (TDD) you write unit tests for what the code *should* do **before** writing the code.

The file `listutil.py` contains a `unique` function. The function has not been written yet, but a placeholder is provided so that your unit tests can run without error (but they *will* fail).

Design and implement tests for what `unique` *should* do, then write the code.  **Zero credit** if I detect someone implementing `unique` before writing the tests.

See the vague docstring comments for what unique should do. Here are a few examples:

```python
>>> unique(["a", "c", "c", "b", "c", "a", 10])
['a', 'c', 'b', 10]
>>> unique([])
[]
```

2.1 Write a table of test cases here.  You should try to "partition" the possible inputs into different cases, and write one test for each "partition". Also tests things where a progammer might make a mistake, such as "off by one" error.

| Test Case                     | Expected Result                |
|:------------------------------|:-------------------------------|
| Empty List                    |   Empty List                   |
| No param or param not a list  |   raise TypeError              |
| One element                   |   that element                 |
| Oridinary case that should work | just set|


2.2 Run your tests.  They should run but mostly fail.

2.3 Implement `unique`.  If you find errors in your tests or think of new tests, you can add them now.

Push your files, including this README, to Github.
