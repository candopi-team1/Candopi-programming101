# CREDIT: Problem-Solving-with-Algorithms-and-Data-Structures-Using-Python\chap04_recursion

from stack import Stack

class Pole:
    def __init__(self, name, stack):
        self.name = name
        self.stack= stack
        
    def display(self):
        print( self.name, " = ", [disk.name for disk in self.stack.items])

class Disk:
    def __init__(self, name):
        self.name = name

# OK         
def hanoi_tower(height, source, target, helper):
    if height >= 1:
        # move the top to helper
        hanoi_tower(height-1, source, helper, target)

        moveDisk(height, source, target)
        
        #move all of helper back to target
        hanoi_tower(height-1, helper, target, source)

# OK too
def hanoi_tower(height, source, target, helper):
    if height == 0: return
    
    # move the top to helper
    # OK hanoi_tower(height-1, source, helper, target)
    hanoi_tower(height-1, source=source, target=helper, helper=target)

    moveDisk(height, source, target, helper) # "helper" is just for show, not functionally needed.
        
    #move all of helper back to target
    # OK hanoi_tower(height-1, helper, target, source)
    hanoi_tower(height-1, source=helper, target=target, helper=source)

                

def moveDisk(height, source, target, helper):
    print( "Moving disk " + str(height) +" from ", source.name, " to ", target.name)
    if not source.stack.isEmpty():
      moved= source.stack.pop()
      target.stack.push(moved)
    
    source.display()
    helper.display()                          # "helper" is just for show, not functionally needed
    target.display()
    print( "")
    

# NOW testing

a= Pole("A", Stack())

# It runs ok, but wrong!
"""
a.stack.push(Disk('frog')) # smallest
a.stack.push(Disk('hen'))
a.stack.push(Disk('goat'))

a.stack.push(Disk('horse'))
a.stack.push(Disk('elephant'))

a.stack.push(Disk('whale')) # largest
"""



a.stack.push(Disk('whale')) # largest
a.stack.push(Disk('elephant'))
a.stack.push(Disk('horse'))
a.stack.push(Disk('goat'))
a.stack.push(Disk('hen'))
a.stack.push(Disk('frog')) # smallest



source_size=a.stack.size()

b= Pole("B", Stack())
c= Pole("C", Stack())


hanoi_tower(source_size, source=a, target=c, helper=b)

while(not c.stack.isEmpty() ) :
       print( c.stack.pop().name )



