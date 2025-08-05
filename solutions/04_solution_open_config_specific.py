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
The script tries to load a config.json file. If the file is missing it
should create a default config dictionary instead of crashing. Catch
only FileNotFoundError. Any other exception should still stop the
program.

Note that we haven't covered opening external files yet. But opening
files is a very common place for code to break, so it is good to start thinking
of how to protect your code here.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

import json

try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"theme": "light", "language": "en"}
print("Config loaded:", config)
