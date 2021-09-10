"""
10 Aug 2020
cd /home/hmk/dailycp/advanced_algos
python3.5  hierholzer.py

"""

from itertools import product


def create_graph(C, k):
    vertices = product(C, repeat = k-1) # [(0, 0) (0, 1) (1, 0) (1, 1)] # <class 'itertools.product'> 
    #                                   # print(type(v)) --> <class 'tuple'>
    edges = {}
    li=[]

    for v in vertices:   
        edges[v] = [ v[1:] + tuple(char) for char in C  ]
    return edges
  

def find_cycle(graph):
    cycle =  []
    before = after = []
    start = list(graph)[0] #     start =   ('0', '0') # ('0', '1') # ('1', '0') #  ('1', '1') # 
    print ("START = ", start, type(start), "\n") # ('1', '0') <class 'tuple'>
    count=0

    while graph: # i.e. len(graph) > 0

       if cycle:
          start = next(vertex for vertex in cycle if vertex in graph)   
          print("start = ", start)
          
          idx = cycle.index(start)
          before = cycle[:idx]
          after =  cycle[idx + 1 :]   
    
       cycle = [start]
       prev = start


       while True:
           curr = graph[prev].pop() # rihgt-most element           
           if not graph[prev]: # i.e. len(graph[prev]) == 0
              graph.pop(prev)      

           cycle.append(curr)                 
           if start == curr : break
           
           prev = curr
       print(cycle)
       cycle = before + cycle + after
       print(cycle, "\n\n")
       # count+=1; print ("*********************", count)
    return cycle  

           
###################################################################################

if __name__=="__main__":  
  C = ["0", "1"]

  k = 3
  graph = create_graph(C, k)  
  # print(g)


  cycle = find_cycle(graph) 
  # print(cycle)

  # for c in cycle[:-1]:
  #    print( c[-1] )
  print(     "".join(  c[-1] for c in cycle[:-1])    )    
   
"""
graph = edges = with 4 vertices
 {('1', '0'): [('0', '0'), ('0', '1')], 
  ('0', '0'): [('0', '0'), ('0', '1')], 
  ('0', '1'): [('1', '0'), ('1', '1')], 
  ('1', '1'): [('1', '0'), ('1', '1')]}



"""

"""
(1) START =  ('1', '0') <class 'tuple'> 

000 10 111



(2) START =  ('0', '1') <class 'tuple'> 

1000 111 0


(3) START =  ('1', '1') <class 'tuple'> 

1000 10 11


(4) START =  ('0', '0') <class 'tuple'> 

00 111 010


"""


"""
START =  ('0', '0') <class 'tuple'> 

[('0', '0'), ('0', '1'), ('1', '1'), ('1', '1'), ('1', '0'), ('0', '1'), ('1', '0'), ('0', '0')]
[('0', '0'), ('0', '1'), ('1', '1'), ('1', '1'), ('1', '0'), ('0', '1'), ('1', '0'), ('0', '0')] 


start =  ('0', '0')
[('0', '0'), ('0', '0')]
[('0', '0'), ('0', '0'), ('0', '1'), ('1', '1'), ('1', '1'), ('1', '0'), ('0', '1'), ('1', '0'), ('0', '0')] 


00 111 010

"""

