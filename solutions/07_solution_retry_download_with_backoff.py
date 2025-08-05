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
The function download() randomly fails by raising ConnectionError.
Write a wrapper that retries up to 3 times. Wait 1 second between
attempts using time.sleep(). If all retries fail print "Download
failed." otherwise print "Download succeeded."
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

import random, time

def download():
    if random.random() < 0.7:
        raise ConnectionError("Network issue")
    return "file data"

def download_with_retry(max_tries=3):
    for attempt in range(1, max_tries + 1):
        try:
            download()
            print("Download succeeded.")
            return
        except ConnectionError as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(1)
    print("Download failed.")

download_with_retry()
