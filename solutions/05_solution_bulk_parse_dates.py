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
The list below mixes date strings and None values. Convert each valid
string to a datetime.date object. Catch ValueError and TypeError so
the loop continues. Collect valid dates in a list called parsed and
print it at the end.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

import datetime as dt

dates = ["2025-01-15", None, "bad", "2025-02-01"]
parsed = []

for d in dates:
    try:
        # this code uses the datetime library to change strings into valid datetimes
        parsed.append(dt.datetime.strptime(d, "%Y-%m-%d").date())
    except ValueError:
        print("Invalid date skipped, not formatted correctly:", d)
    except TypeError:
        print("Invalid date skipped, must be a string datatype:", d)

print(parsed)
