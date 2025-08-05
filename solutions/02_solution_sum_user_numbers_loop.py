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
The program should keep asking the user for numbers and add them to a
running total. Typing the letter q should quit. If the user types
anything that is not a number or q, the program currently crashes.
1. Wrap the conversion to int in a try-except block inside the loop.
2. When bad input is given, print "Please enter a number or q." and
   continue the loop.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

total = 0
while True:
    entry = input("Enter a number to add (q to quit): ")
    if entry == "q":
        break
    try:
        total += int(entry)
    except ValueError:
        print("Please enter a number or q.")
print("Final total:", total)
