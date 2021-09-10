"""
04 Aug 2020

cd /home/kyawnaing/dailycp/randomized_algos
python3.5  markov_chain.py

"""

from collections import defaultdict
from random import random

def histogram_count(start, no_of_steps, states_prob_list):
    states_prob_dict = translate_into_dict(states_prob_list)
    count_histogram  = defaultdict(int)
    curr_state       = start

    for i in range(no_of_steps):
      count_histogram[curr_state] += 1
      next_state_val= get_next_state(curr_state, states_prob_dict)
      curr_state    = next_state_val

    return count_histogram


def  get_next_state(curr_state, states_prob_dict):
     r = random()
     for end, prob in  states_prob_dict[curr_state].items():
        r-= prob
        if r <= 0:
           return end
    


def translate_into_dict(states_prob_list): 
      d=defaultdict(dict)

      for start, end, prob in  states_prob_list:
          d[start][end] = prob

      return d



if __name__=="__main__": 
 

  states_prob_list = [
   ('a', 'a', 0.9),
   ('a', 'b', 0.075),
   ('a', 'c', 0.025),
   ('b', 'a', 0.15),
   ('b', 'b', 0.8),
   ('b', 'c', 0.05),
   ('c', 'a', 0.25),
   ('c', 'b', 0.25),
   ('c', 'c', 0.5)
  ]

  start = 'a'
  num_of_steps= 5000

  count_histogram = histogram_count(start, num_of_steps, states_prob_list)
  print( count_histogram  )





