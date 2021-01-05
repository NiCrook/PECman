# PECman - Poker Equity Calculator

Basic poker equity calculator that takes the user's number of outs and the chance they believe their opponent will fold and provides the natural, fold, and total, equity.


# Status
v1.05
Under Construction

# Demo
placeholder

# Built With
Python

# Code Peek
```
def validate(self, new_char):
    if not new_char:
        self.entered_fold = 0
        self.entered_call = 0
        self.entered_bet = 0
        self.entered_raise = 0
        return True
```

# Usage
With Python installed, copy PECman.py onto your machine and run in your desired virtural environment. A window should pop up with two buttons "PEC" and "RNG". The user will then be guided with questions and entry fields. The order must be kept, otherwise, the calculations will be equated incorrectly. 

# Contribute
I am unsure why this is broken and the order must be preserved as such. If you know any reason why, please, let me know!

# License
MIT @ Nicholas Crook
