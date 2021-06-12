import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  
    for i in range(0,100):
        print(random.randint(1,6)+random.randint(1,6))
