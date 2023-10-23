##############################################################
# Interact with command line 4
##############################################################
import sys, getpass

def raw_input2(value="", end="\n"):
    sys.stdout.write(value)
    sys.stdout.flush()
    data = getpass.getpass("")
    sys.stdout.write(end)
    sys.stdout.flush()
    return data

answer = raw_input2("Question? (y/n) ")
print("You answered", answer)

