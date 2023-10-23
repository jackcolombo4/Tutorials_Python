##############################################################
# Interact with command line 2
##############################################################
import getpass

question = "Question? (y/n) "
print(question, end='', flush=True)

while True:
    answer = getpass.getpass("")

    if answer.lower() == "y":
        print("You answered yes.")
        break
    elif answer.lower() == "n":
        print("You answered no.")
        break
    else:
        print("\033[F\033[K", end='', flush=True)
        #print("Invalid answer. Please try again.", end='', flush=True)
        print("\033[F\033[K" + question, end='', flush=True)
