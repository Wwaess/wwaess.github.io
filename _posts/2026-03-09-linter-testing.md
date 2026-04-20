---
title: "Linter Testing"
date: 2026-03-09 00:00:00 +0000
categories: [SSDCS]
tags: [SSDCS]
---

For **Unit 6**

This has a bunch of questions involving some python code files in a zip folder. 

# Question 1
```
Run styleLint.py. What happens when the code is run? Can you modify this code for a more favourable outcome? What amendments have you made to the code?
```
The code in question looks like this:
```py
# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON 

def factorial(n):
""" Return factorial of n """
if n == 0:
return 1
else:
return n*factorial(n-1)
```
Doing absolutely nothing to the code, running it has an indentation issue:
`IndentationError: expected an indented block after function definition on line 4`. 

Reindenting the code correctly: 
```py
# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON 

def factorial(n):
""" Return factorial of n """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
``` 
allows the code to run with no error - though as it's just a function definition, nothing is outputted. 


# Question 2
```
pip install pylint

Run
 pylint 
on pylintTest.py

Review each of the code errors returned. Can you correct each of the errors identified by pylint?

Before correcting the code errors, save the pylintTest.py file with a new name (it will be needed again in the next question).
```

The code for pylintTest.py without any further editing is as follows: 
```py
# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html

import string
 
shift = 3
choice = raw_input("would you like to encode or decode?")
word = (raw_input("Please enter text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
  for letter in word:
    if letter == ' ':
      encoded = encoded + ' '
    else:
      x = letters.index(letter) + shift
      encoded=encoded + letters[x]
    if choice == "decode":
      for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
          x = letters.index(letter) - shift
          encoded = encoded + letters[x]

print encoded
```

and running `pylint pylintTest.py` yields the error

`
pylintTest.py:26:1: E0001: Parsing failed: 'Missing parentheses in call to 'print'. Did you mean print(...)? (pylintTest, line 26)' (syntax-error)
`

Correcting this last line to `print(encoded)` and rerunning `pylint` yields a plethora more errors: 

```
************* Module pylintTest
pylintTest.py:5:0: C0303: Trailing whitespace (trailing-whitespace)
pylintTest.py:8:0: C0325: Unnecessary parens after '=' keyword (superfluous-parens)
pylintTest.py:12:0: W0311: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
pylintTest.py:13:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
pylintTest.py:14:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:15:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
pylintTest.py:16:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:17:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:18:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
pylintTest.py:19:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:20:0: W0311: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
pylintTest.py:21:0: W0311: Bad indentation. Found 12 spaces, expected 20 (bad-indentation)
pylintTest.py:22:0: W0311: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
pylintTest.py:23:0: W0311: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
pylintTest.py:24:0: W0311: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
pylintTest.py:26:0: C0304: Final newline missing (missing-final-newline)
pylintTest.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pylintTest.py:1:0: C0103: Module name "pylintTest" doesn't conform to snake_case naming style (invalid-name)
pylintTest.py:6:0: C0103: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:7:9: E0602: Undefined variable 'raw_input' (undefined-variable)
pylintTest.py:8:8: E0602: Undefined variable 'raw_input' (undefined-variable)
pylintTest.py:9:0: C0103: Constant name "letters" doesn't conform to UPPER_CASE naming style (invalid-name)

-----------------------------------
Your code has been rated at 0.00/10
```

In response, I have
- reindented the code correctly (at least, by conforming to the W0311 expectations from the linting)
- added a newline at the end of the code
- renamed the module (i.e. the Python file) from `pylintTest.py` to `pylint_test.py`
- renamed `shift` to `SHIFT`
- renamed `raw_input` to `input` (i.e. the correct way to request a user input in Python)
- renamed `letters` to `LETTERS`

Running `pylint` on this new `pylint_test.py` yields a code rating of `10.00/10`. 

# Question 3
```
(part 1)
pip install flake8
Run

flake8 
on pylintTest.py

Review the errors returned. In what way does this error message differ from the error message returned by pylint?
```

Running `flake8` on the original `pylintTest.py` also calls the print() error: 

```
.\pylintTest.py:26:2: E999 SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

Correcting that and rerunning `flake8` yields the following errors: 

```yaml
.\pylintTest.py:5:1: W293 blank line contains whitespace
.\pylintTest.py:7:10: F821 undefined name 'raw_input'
.\pylintTest.py:8:9: F821 undefined name 'raw_input'
.\pylintTest.py:12:3: E111 indentation is not a multiple of 4
.\pylintTest.py:14:7: E111 indentation is not a multiple of 4
.\pylintTest.py:16:7: E111 indentation is not a multiple of 4
.\pylintTest.py:17:7: E111 indentation is not a multiple of 4
.\pylintTest.py:17:14: E225 missing whitespace around operator
.\pylintTest.py:19:7: E111 indentation is not a multiple of 4
.\pylintTest.py:23:11: E111 indentation is not a multiple of 4
.\pylintTest.py:24:11: E111 indentation is not a multiple of 4
.\pylintTest.py:26:15: W292 no newline at end of file
```

Like with `pylint`, `flake8` raised concerns about the indentation, about how `raw_input` isn't defined here, and about how there's no newline at the end of the code. 

It differs, however, on the following: 
- it doesn't suggest how _much_ indentation it expected, only that it didn't like indentations that were non-multiples of 4. 
- it had a presentation issue with the lack of whitespaces around the `=` in the line `encoded=encoded + ' '`. 
- it didn't seem to care for how variables were named, nor how the module itself was named. 

---
```
(part 2)

Run flake8 on metricTest.py. Can you correct each of the errors returned by flake8? What amendments have you made to the code?
```

Running `flake8` initially flagged: 
```.\metricTest.py:25:24: E999 SyntaxError: invalid character '–' (U+2013)``` - i.e. this is an _em-dash_. Replacing it with the hyphen-minus (U+002D) resolves this. 

It then flags: 
```.\metricTest.py:13:4: E999 SyntaxError: invalid syntax```
and this is likely because for some reason the line-numbers themselves have found themselves into the code: 

```py

#CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON 

"""
2 Module metricTest.py
3
4 Metric example - Module which is used as a testbed for static
checkers.
5 This is a mix of different functions and classes doing
different things.
6
7 """
8 import random
9
10 def fn(x, y):
11 """ A function which performs a sum """
12 return x + y
13
14 def find_optimal_route_to_my_office_from_home(start_time,
15 expected_time,
16 favorite_route='SBS1K',
17 favorite_option='bus'):
18
...
```

Removing these numbers and rerunning `flake8`: 
```.\metricTest.py:16:2: E999 IndentationError: expected an indented block after function definition on line 15```

and indeed there are actually a lot of indenting issues (which I can't tell whether it was a result of how the code was handled "in transit" to me or if this was deliberate for the purposes of this exercise). Going through the code and reindenting this properly (with minimal code edits), running `flake8` flagged a lot of "errors" about trailing whitespaces, the number of blank lines it expected in given places, and the occasional continuation-line being underindented — this was in reference to parts of the code being written like so: 
```py
            return random.choice(('bus:330','bus:331',':'.
                join((favorite_option,
                    favorite_route))))
```
It was easier to manage if I made the list as "laid-out" as possible, i.e. as follows: 
```py
            return random.choice((
                'bus:330',
                'bus:331',
                ':'.join(
                    (
                        favorite_option,
                        favorite_route
                    )
                )
            ))
```

The edited file, `metric_test.py`, is available in `SSDCS\code snippets`. 

It should be noted that running this updated code through `pylint` results in a code rating of 5.80 out of 10; the readability of this code certainly needs more improvement than implied from the `flake8` testing. 

# Question 4
```

pip install mccabe
Run
mccabe 
on sums.py. What is the result?

Run

mccabe 
on sums2.py. What is the result?

What are the contributors to the cyclomatic complexity in each piece of code?
```

It hasn't been noted in the source for these questions — `mccabe` isn't run directly, instead being run via Python
```c
python -m mccabe .\sums.py
```

Indeed, running `mccabe` with 10 maximum complexity on `sums.py` yields the following: 
```
.\sums.py:7:1: E305 expected 2 blank lines after class or function definition, found 1  
.\sums.py:9:31: W292 no newline at end of file
```





# References
PyPi (2022) `mccabe 0.7.0`. Available at: https://pypi.org/project/mccabe/
