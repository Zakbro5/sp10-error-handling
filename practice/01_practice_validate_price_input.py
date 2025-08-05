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
The cashier app below asks a user to enter a price. If the user types
something that cannot be turned into a float, the program crashes.
1. Run the script and note the ValueError.
2. Add a try-except block that catches ValueError and prints
   "Invalid price. Please try again." instead of crashing.
'''

price_input = input("Enter the item price: ")
price = float(price_input)
print("Price recorded:", price)
