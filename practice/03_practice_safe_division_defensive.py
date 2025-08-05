'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Complete two versions of a divide function below.
1. divide_defensive(a, b) should return None if b is zero (defensive
   programming).
2. divide_try(a, b) should use try-except to catch ZeroDivisionError.

Fill in the missing code so the
output is:

defensive: None
try/except: Cannot divide by zero.
'''

def divide_defensive(a, b):
    # TODO: add defensive check
    pass

def divide_try(a, b):
    # TODO: add try-except around a / b
    pass


print("defensive:", divide_defensive(10, 0))
print("try/except:", divide_try(10, 0))
