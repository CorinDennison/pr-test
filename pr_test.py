# Author: Corin Dennison
# Date: 3/13/2025
# This program asks the user for input and then prints that many powers of two.

# keeps asking the user for input until they either respond with an integer or quit
# returns None if the user quits, otherwise returns the integer
def get_positive_integer_input(question_string):
    # Ask user for input
    user_input = input(question_string).strip()
    # if the input isn't an integer, keep looping until it is, or they quit
    while not user_input.isdecimal():
        if user_input.lower() in ["q", "quit", "exit"]:
            return None
        print("Positive integers only please.")
        user_input = input(question_string)
    return int(user_input)

# returns some number of powers of two
def powers_of_2(amount):
    # build the list of powers of 2
    p_of_2 = []
    for x in range(1, amount + 1):
        p_of_2.append(2**x)

    return p_of_2

# loop until the user quits
keep_playing = True
while keep_playing:
    amount = get_positive_integer_input("How many powers of two would you like?")
    if amount is not None:
        print(powers_of_2(amount))
        if input("again?").lower() not in ["y", "yes"]:
            # stop playing if the user wants to stop
            keep_playing = False
    else:
        # stop playing if the user refused to give an integer
        keep_playing = False
print("Goodbye!")