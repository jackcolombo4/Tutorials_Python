##############################################################
# Interact with command line 1
##############################################################
import getpass

# Define the question
question = "Question? (y/n) "

# Loop until a valid answer is entered
while True:
    # Ask the question and get the hidden input
    answer = getpass.getpass(question)
    
    ## Check if the entered answer is valid
    if answer.lower() in ("y", "n"):
        break

    # Clear the line and print the question again, if the answer is invalid
    print("\033[F\033[K", end="")
    print(question, end="")

print(answer)