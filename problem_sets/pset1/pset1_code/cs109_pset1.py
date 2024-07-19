# Name: Lynn
# Stanford email: Null

"""
*************** IMPORTANT ***************
Do NOT rename this file.
Do NOT rename the play_game function or alter its parameters in any way.

The autograder expects the following:
- Your file should be named cs109_pset1.py
- Your solution should be in a function named play_game:
  - it should take 2 arguments as indicated in the provided starter code.
  - it must return a float

Hints:
- Notice the strict inequality in the looping condition
  (i.e. stop when S > 100, and S > 200)
- The function np.random.randint(low, high) is INCLUSIVE of low
  and EXCLUSIVE of high. Hence, we should have low=1 and high=101.
- Player 2 wins if and only if y > x, not when y >= x.
- Player 2 resumes adding from Player 1's sum.
  Player 2 does NOT start over at 0.

Grading:
- The Gradescope autograder will report your problem score
  (i.e., there are no hidden tests). No partial credit will be given
  if you do not pass the autograder.
- You can submit an unlimited number of times. We will only use
  the score from your most recent submission.
"""

# Do NOT add any import statements
import numpy as np

# Instructions:
# Fill in the following function.
# We will be testing your code by setting several random seeds.
# DO NOT ALTER THIS FUNCTION OUTSIDE THE BEGIN/END CODE MARKERS.
# You may add other helper functions if you wish.
# Do not add or remove parameters to this function.
def play_game(seed: int = 37, ntrials: int = 100000) -> float:
    """
    Plays a game described in the Pset 1 handout ntrials times 
    with a predetermined seed.
    :param seed: seed for the numpy random number generator.
    :param ntrials: the number of trials to run.
    :return: the probability as described in the written pset.
    """
    np.random.seed(seed)

    #################### BEGIN YOUR CODE ####################
    # You MUST use the function np.random.randint from numpy
    # to generate random numbers, NOT random.randint or
    # any other package.
    player_two_win = 0
    
    for _ in range(0, ntrials):
        sum = 0
        
        while(sum <= 100):
            current_int = np.random.randint(1, 100)
            sum += current_int
        player_one_num = current_int
        while(sum <= 200):
            current_int = np.random.randint(1, 100)
            sum += current_int
        player_two_num = current_int
        
        if player_one_num < player_two_num:
            player_two_win += 1

    player_two_win_rate = player_two_win / ntrials

    return player_two_win_rate
    ####################  END YOUR CODE  ####################
