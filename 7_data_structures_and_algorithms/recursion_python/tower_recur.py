# CREDIT: Problem-Solving-with-Algorithms-and-Data-Structures-Using-Python\chap04_recursion

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from", fp, "to", tp)

# OK too long time # moveTower(30, "A", "B", "C")
# OK too long time # moveTower(20, "A", "B", "C")
moveTower(10, "A", "B", "C")
