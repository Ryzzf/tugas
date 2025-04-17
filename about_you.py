import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Something to do while we try to recall how we met", 0.13),
        ("Do you think I have forgotten?", 0.12),
        ("Do you think I have forgotten?", 0.12),
        ("Do you think I have forgotten about you?", 0.18),

     
        
    ]

    delays = [3, 1.5, 1.5, 2 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()