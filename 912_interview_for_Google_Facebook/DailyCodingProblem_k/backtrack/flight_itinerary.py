"""
06 Aug 2020
cd /home/kyawnaing/dailycp/backtrack
python3.5  flight_itinerary.py

"""

"""
(1) partial solution
(2) validate the solution so far
(3) checks if the solution is complete

 backtrack :: append/add/set value --> remove/pop/reset value
"""


"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
and a starting airport, compute the person's itinerary. 

If no such itinerary exists, return null. All flights must be used in the itinerary.

For example, given the following list of flights:
    HNL -> AKL
    YUL -> ORD
    ORD -> SFO
    SFO -> HNL

and starting airport YUL, you should return YUL -> ORD -> SFO -> HNL -> AKL. 

"""

def get_itinerary(flights, current_itin):
    if not  flights: return current_itin # SUCCESS

    last_stop=current_itin[-1]
    
    for i, (orig, dest) in enumerate(flights):
      current_itin.append(dest)
      print(current_itin)
      if orig == last_stop:
        flights_minus_current= flights[:i] + flights[i+1:]
        return get_itinerary(flights_minus_current, current_itin)

      current_itin.pop() # This dest doen't work, take it out, continue

    return None


if __name__ == "__main__":
    flights1 = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")]
    flights2 = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL"), ("NYC", "MDY")]

    flights3 = [ ("SBG", "YGN"), ("CHK", "SBG"), ("YGN", "OSK"),  
              ("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL"), 
              ("NYC", "MDY"), ("MDY", "CHK"), ("AKL", "NYC")]
    # YUL -> ORD -> SFO -> HNL -> AKL -> NYC -> MDY -> CHK -> SBG -> YGN -> OSK

    flights = [ ("A", "CEN"), ("CEN", "A"), ("B", "CEN"), ("CEN", "B"), ("C", "CEN"), ("CEN", "C"),        ]

    flights = [("C", "CEN"), ("A", "CEN"), ("CEN", "A"), ("B", "CEN"),  ("CEN", "C"), ("CEN", "B"),  ("CEN", "C"), ("C", "CEN"), ("CEN", "C"),        ]

    flights = [("A", "CEN"),  ("CEN", "B"),   ("B", "CEN"),   ("CEN", "C"),             ]  
    # A -> CEN -> B -> CEN -> C ?? # only when I arrange and compact the list !!!! ("",""),

    flights = [("SG","LA"), ("C","CHK"), 
              ("A", "CEN"),  ("MDY","YGN"), ("CEN", "B"),  ("YGN","SG"), ("B", "CEN"),   ("CEN", "C"),  ("CHK","MDY"),
              ("LA","CHK"), ("CHK","A"),
              ]  
   # A -> CEN -> B -> CEN -> C -> CHK -> MDY -> YGN -> SG -> LA -> CHK -> A


    flightsX = [("SG","LA"), ("C","CHK"), ("CHK","A"), # problematic order
               ("A", "CEN"),  ("MDY","YGN"), ("CEN", "B"),  ("YGN","SG"), ("B", "CEN"),  
               ("CEN", "C"),  ("CHK","MDY"), ("LA","CHK"), ]






    source = "YUL"
    source="A"

    itin= get_itinerary(flights, [source])

    if itin:
      print(" -> ".join(itin))
    else:
      print("NO Itinerary")


