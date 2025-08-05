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
Complete the login() function so it uses a nested try-except pattern.
Outer try: validate that the email contains an @ symbol; raise a
ValueError if not.
Inner try: convert the pin string to int and compare to 1234.
Print "Login successful" or an appropriate message for each failure.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

def login(email, pin_str):
    try:
        if "@" not in email:
            raise ValueError("Email missing @ symbol")
        try:
            pin = int(pin_str)
            if pin == 1234:
                print("Login successful")
            else:
                print("Incorrect PIN")
        except ValueError:
            print("PIN must be numeric")
    except ValueError as e:
        print("Email error:", e)

login("userexample.com", "abcd")
