#Write a python function to determine the
#probability of certain outcomes when rolling dice
'''
Monte Carlo Method:
    - Trial1 (1,3) = 4
    - Trail2 (3,5) = 8
    - Trial3 (2,4) = 6 
What is monte carlo simulation?
    - a millon simulation
Program:
    - input: variable number of arguments for sides of dice
    - table of probability for each possible outcome
        - the outcome is a probability for each possible result
            - so for a two sided dice there is 1/36 probability
            - for a three sided dice there is 1/216 possibilities  
what i will need: 
    - I am trying to get the probability of rolling a value out of n dice and n-sided
    - so if i a 6 sided die and there is 3 of them
        - value 4 = (1,1,2),(2,1,1),(1,2,1)
        - esentially what i am looking for is teh probability of rolling an exact sum out of the 
          set of n s-sided dice:
Solution:
    - using randint to simulate rolling dice because one dice is rolled in the sense of 1/sides

        
'''
from random import randint
from collections import Counter

def roll_dice(*dice,num_trials=100000):
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1
    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice),sum(dice)+1):
        print(f'{outcome}\t{counts[outcome]*100/num_trials :0.2f}%')
