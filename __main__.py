

def getPozOfBlankSquare(puzzle):
    for pos in puzzle:
        if(puzzle[pos] == ' '):
            return pos
    

def metGoal(puzzle):
    return puzzle[(0,0)] == '1' and puzzle[(1,0)] == '2' and puzzle[(2,0)] == '3' and puzzle[(0,1)] == '4' and puzzle[(1,1)] == '5' and puzzle[(2,1)] == '6'  and puzzle[(0,2)] == '7' and puzzle[(1,2)] == '8' and puzzle[(2,2)] == ' '
    return puzzle[(0,0)] == '1' and puzzle[(1,0)] == '2' and puzzle[(2,0)] == '3' and puzzle[(2,1)] == '4' and puzzle[(0,1)] == '8' and puzzle[(0,2)] == '7'  and puzzle[(1,2)] == '6' and puzzle[(1,1)] == ' '
    return puzzle == {(0,0):'1', (1,0):'2', (2,0): '3',
            (0,1):'8', (1,1):' ', (2,1):'4',
            (0,2):'7', (1,2):'6', (2,2):'5'}
    #puzzle[(0,0)] == '1' and puzzle[(1,0)] == '2' and puzzle[(2,1)] == '3' and puzzle[(0,1)] == '8' and puzzle[(2,1)] == '4' and puzzle[(0,2)] == '7' and puzzle[(1,2)] == '6' and puzzle[(2,2)] == '5' 

def numOfCorrect(puzzle):
    correctPuzzle = {(0,0):'1', (1,0):'2', (2,0): '3', (0,1):'8', (1,1):' ', (2,1):'4', (0,2):'7', (1,2):'6', (2,2):'5'}
    numCorrect = 0
    for pos in correctPuzzle:
        if(puzzle[pos] == correctPuzzle[pos]):
            numCorrect += 1
    return numCorrect

def searchInDirection(puzzle, blankPos, dir):
    swapPos = (blankPos[0] + dir[0], blankPos[1] + dir[1])
    newPuzzle = puzzle.copy()
    if(swapPos in puzzle):
        #swap
        newPuzzle[blankPos] = puzzle[swapPos]
        newPuzzle[swapPos] = ' '
    return (metGoal(newPuzzle), newPuzzle)

def manhattanDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def manhattanDistancePiece(pos, number):
    correctPuzzle = {'1':(0,0), '2':(1,0), '3':(2,0), '8':(0,1), ' ':(1,1), '4':(2,1), '7':(0,2), '6':(1,2), '5':(2,2)} 
    correctPos = correctPuzzle[number]
    return manhattanDistance(pos, correctPos)
    

def manhattanDistanceOfPuzzle(puzzle):
    distance = 0
    for pos in puzzle:
        distance += manhattanDistancePiece(pos, puzzle[pos])
    return distance

def to_hashable(puzzle):
    state = ()
    for y in range(0,3):
        for x in range(0,3):
            state += tuple(puzzle[(x,y)])
    return state

def solve_with_breadth_first(puzzle):
    #every branch is weather the piece moves up,left,down,right
    
    visitedBefore = set([to_hashable(puzzle)])
    queue = [puzzle]
    countAlready = 0
    while(len(queue) > 0):
        
        queue = sorted(queue, key=lambda x: numOfCorrect(x), reverse=True)
        #queue = sorted(queue, key=lambda x: manhattanDistanceOfPuzzle(x), reverse=False)
        # for q in queue:
        #     print(numOfCorrect(q))
        #     print_puzzle(q)
        #     print()
        # print("----------------------------------")
        node = queue.pop(0)
        if(metGoal(node)):
            return (True, node)
        blankPos = getPozOfBlankSquare(node)
        #print_puzzle(node)
        #print_puzzle(node)
        #print(len(queue))
        for move in [(0,1),(0,-1),(1,0),(-1,0)]:
            (solved, updatedPuzzle) = searchInDirection(node, blankPos, move)
            if(solved):
                return (True, updatedPuzzle)
            else:
                #add to queue
                if(not to_hashable(updatedPuzzle) in visitedBefore):
                    queue.append(updatedPuzzle)
                    visitedBefore.add(to_hashable(updatedPuzzle))
                else:
                    countAlready += 1
        
        

    return (False, puzzle)
        
        
    

    
    

def print_puzzle(puzzle):
    print(puzzle[(0,0)]+" "+puzzle[(1,0)] + " " + puzzle[(2,0)])
    print(puzzle[(0,1)]+" "+puzzle[(1,1)] + " " + puzzle[(2,1)])
    print(puzzle[(0,2)]+" "+puzzle[(1,2)] + " " + puzzle[(2,2)])


def main():
    puzzle = {(0,0):'7', (1,0):'5', (2,0): '3',
            (0,1):'1', (1,1):'4', (2,1):' ',
            (0,2):'8', (1,2):'6', (2,2):'2'}

    puzzle1 = {(0,0):'8', (1,0):'1', (2,0): '3',
            (0,1):'7', (1,1):'2', (2,1):'4',
            (0,2):' ', (1,2):'6', (2,2):'5'}

    print(to_hashable(puzzle))
    print_puzzle(puzzle)
    print(metGoal(puzzle))
    (foundSolution, solvedPuzzle) = solve_with_breadth_first(puzzle)
    if(foundSolution):
        print("Found Solution")
        print_puzzle(solvedPuzzle)
    else:
        print("No Solution")


if __name__ == '__main__':
    main()

