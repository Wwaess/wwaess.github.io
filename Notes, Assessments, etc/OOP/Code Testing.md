# Activity One - error detection

Here's some Python code. Comments have been added where there are any errors: 

```py
def factorial (x) 
# This `(x)` should be right after the function name, with no spaces, i.e. `factorial(x)`. 
# It should also have a `:` after it. 
    if x == 1:
        return 1

    else:
        return (x * factorial(x-1))

num = 3
# This is dangerous - the function uses a recursion-to-one definition of factorials, 
# which if used should also ensure that `num` is set to a (positive) integer, 
# to avoid a maximum recursion depth error. 
print("The factorial of", num, "is", factorial(num)) 
```

# Activity Two - commenting and documentation 

The code snippet supplied is missing a lot of indentation; this has been rectified here. 

This code represents a basic calculator, allowing a user to add, subtract, multiply or divide two numbers. This uses a While Loop to allow the user to perform multiple calculations; the user may quit at the end of any calculation when prompted to. 

Comments have been added where applicable to explain the code. 


```py
# Define the basic calculator operations. 
def add(x, y): 
    return x + y 
def subtract(x, y): 
    return x - y 
def multiply(x, y): 
    return x * y 
def divide(x, y): 
    return x / y 

# List them out for the user. 
print("Select operation.") 
print("1.Add") 
print("2.Subtract") 
print("3.Multiply") 
print("4.Divide") 

# Enter the While Loop 
# (I would've started this loop earlier; this isn't my code, 
# so I won't modify it anymore than I already have debugged this)
while True: 
    choice = input("Enter choice(1/2/3/4): ")  
    
    # Collect user inputs
    if choice in ('1', '2', '3', '4'): 
        num1 = float(input("Enter first number: ")) 
        num2 = float(input("Enter second number: ")) 
    
        # Output calculation answer
        if choice == '1': print(num1, "+", num2, "=", add(num1, num2)) 
        elif choice == '2': print(num1, "-", num2, "=", subtract(num1, num2)) 
        elif choice == '3': print(num1, "*", num2, "=", multiply(num1, num2)) 
        elif choice == '4': print(num1, "/", num2, "=", divide(num1, num2)) 

        '''
        This following line has been rewritten: the code snippet supplied had this line instead:
            break the while loop if answer is no next_calculation = input("Let's do next calculation? (yes/no): ") 
        '''
        next_calculation = input("Let's do the next calculation? (yes/no): ")
        if next_calculation == "no": 
            break

    # And should the "Choice" not be any of 1, 2, 3 or 4: 
    else: print("Invalid Input")
```


# Activity Three - Commenting Conventions in Java and Python?

There's a paper [^1] which seeks to determine how one should assess the quality of comments in code. Supposedly it makes reference to aspectual components of guidelines, such as syntax, context and structure to name a few, and asks two core "research questions", or RQs: 
- RQ1 - _Which type of comment conventions are suggested by various style guidelines?_
- RQ2 - _To what extent do developers follow commenting conventions in writing code comments in Java and Python?_

Generally speaking, the paper concludes five core categories that most guidelines have concerning comment-related rules: 
|CATEGORY       |DESCRIPTION                                                        |
|Content        |What information should be included (purpose, usage, limitations)  |
|Writing style  |Grammar, punctuation, capitalisation, tone                         |
|Structure      |Comment section organisation                                       |        
|Formating      |Indentation, spacing, blank lines                                  |
|Syntax         |Symbols and tags used                                              |

The paper however finds that while writing style and content conventions are generally followed, structure conventions are generally violated. It lists as a finding that "style guidelines suggest various comment conventions," but that "developers do not or rarely adopt them while writing comments." 

It also finds that standard guidelines are often less followed, in favour of project-specific class comment conventions; I'd argue it's since they're more tailored to the goal of the code being worked on. 

To this end, I'm similarly not going to change my comments in the previous activity. (I also have a nitpick at "writing style" as a category here - the majority of this description isn't even a matter of conventions, to be honest - that's just the basics of writing, and isn't specific to code-commenting in _any_ case.) In general my aims for comments are as follows:
- add comments to segment what the code does, as per the accompanying documentation (assuming it has been written, or at least outlined). 
- add comments where it's ambiguous what the code does. 
- write them as clear as possible. 
- make them as concise as possible. 

Contextually I'm putting this code snippet into my e-portfolio too, and that's a specific (as opposed to a general) standard to bear in mind - the context. Were this in an actual collaborative development environment, I wouldn't add the comment 
```py
# (I would've started this loop earlier; this isn't my code, 
# so I won't modify it anymore than I already have debugged this)
```
there, since it detracts from the point of the comment - namely to point out the core WHILE loop specified in the documentation. 

# References
[^1]: Pooja Rani, Suada Abukar, Nataliia Stulova, Alexandre Bergel, Oscar Nierstrasz: "Do Comments follow Commenting Conventions? A Case Study in Java and Python" https://arxiv.org/pdf/2108.10766