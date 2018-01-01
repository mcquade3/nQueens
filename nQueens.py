"""
Mike McQuade
nQueens.py
"""

def inputPerm(perm):
    n = len(perm)
    if safe(perm): printBoard(perm,n)
    else: print("No solution")

def safe(perm):
    if len(perm) == 1: return True
    else:
        if compare(perm[0],perm[1:]): return safe(perm[1:])
        else: return False

def compare(spot,perm,x=1):
    if perm == []: return True
    else:
        if abs(spot - perm[0]) != x: return compare(spot,perm[1:],x+1)
        else: return False

def printBoard(positions,n):
    if positions == []: pass
    else:
        preLoop(positions[0])
        print("|Q",end="")
        postLoop(positions[0],n)
        print('|')
        printBoard(positions[1:],n)

def preLoop(boardSpot,spot=1):
    if spot >= boardSpot: pass
    else:
        print("|-",end="")
        preLoop(boardSpot,spot+1)

def postLoop(boardSpot,n):
    if boardSpot >= n: pass
    else:
        print("|-",end="")
        postLoop(boardSpot+1,n)

def main():
    inputPerm([4,6,1,4])
    
main()
