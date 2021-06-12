import random

def problem2_4():
    lis=[]
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    for i in range(0,10):
        lis.append(30+random.random()*5)
    print(lis)
