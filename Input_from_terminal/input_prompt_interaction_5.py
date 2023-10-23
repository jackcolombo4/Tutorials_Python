##############################################################
# Interact with command line 5
##############################################################
import sys
import getpass

def raw_input2(value="", end="\n"):
    while True:
        sys.stdout.write(value)
        sys.stdout.flush()
        data = getpass.getpass("")
        if data.lower() in ("y", "n"):
            break
        sys.stdout.write("\033[F\033[K" + value)
        sys.stdout.flush()
    return data

answer = raw_input2("Question? (y/n) ")
print("You answered", answer)
