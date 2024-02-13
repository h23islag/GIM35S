import time
TSECS = 0.02

def typewriter_effect(message):
    for c in message:
        print(c, end="")
        time.sleep(TSECS)