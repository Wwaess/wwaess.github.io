For **UNIT 6**:

The following code has been asked to be filed under `wallet.py`:

```py
# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# wallet.py
 class InsufficientAmount(Exception):
    pass
  
class Wallet(object):
     def __init__(self, initial_amount=0):
        self.balance = initial_amount
 
    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount
 
    def add_cash(self, amount):
        self.balance += amount
```

and similarly the following code into `test_wallet.py`: 

```py
# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
 # test_wallet.py
 import pytest
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0
 
def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100
 
def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100
 
def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10
 
def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
```

Running these files natively via Visual Studio Code (Python 3.13.5), I did have to reindent the copied code snippets and ensire these files were properly saved (GitHub has been playing around with being difficult to write to for me these past few weeks), and eventually I was able to run `pytest -q test_wallet.py` into a terminal while in the same folder to test `pytest` and get a no-errors output: 

```
5 passed in 0.01s
```

Swapping the `__init__` in the Wallet class in `wallet.py` such that the initial amount is defaulted to `10` does cause an error: 

```h
..F..                                                                                 [100%]
========================================= FAILURES ========================================= 
_______________________________ test_default_initial_amount ________________________________ 

    def test_default_initial_amount():
        wallet = Wallet()
>       assert wallet.balance == 0
E       assert 10 == 0
E        +  where 10 = <wallet.Wallet object at 0x0000022529456660>.balance

test_wallet.py:8: AssertionError
================================= short test summary info ================================== 
FAILED test_wallet.py::test_default_initial_amount - assert 10 == 0
1 failed, 4 passed in 0.07s
``` 

Essentially when `pytest` runs through the definition
```py
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0
```
it comes to a different conclusion to what the `wallet.py` file says, so the assertion fails [AssertionError]. 

Similarly if I run `pytest` but with 

```
    def add_cash(self, amount):
        self.balance -= amount
```
i.e. the `add_cash` function SUBTRACTs money, then the following error occurs:

```h
..F..                                                                                  [100%]
========================================= FAILURES ========================================== 
___________________________________ test_wallet_add_cash ____________________________________ 

    def test_wallet_add_cash():
        wallet = Wallet(10)
        wallet.add_cash(90)
>       assert wallet.balance == 100
E       assert -80 == 100
E        +  where -80 = <wallet.Wallet object at 0x000002619C5EFD90>.balance

test_wallet.py:17: AssertionError
================================== short test summary info ================================== 
FAILED test_wallet.py::test_wallet_add_cash - assert -80 == 100
1 failed, 4 passed in 0.08s
```

