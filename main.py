import copy

options = []
for i in range(9):
    options.append([])
    for j in range(9):
        options[i].append([1,2,3,4,5,6,7,8,9])

def removefrom(assignment,i,j,possible):
    print("ORIGINAL", str(i),str(j),str(possible))
    print(assignment)
    print("Now isolating " + str(possible))
    new = copy.deepcopy(assignment)
    new[i][j] = [possible]
    for rows in range(9):
        for cols in range(9):
            if (rows == i or cols == j or (rows//3 == i//3 and cols//3 == i //3)) and not(rows == i and cols == j):
                if possible in new[i][j]:
                    new[i][j].remove(possible)
    print(new)
    return new

def solve(assignment):
    for i,row in enumerate(assignment):
        for j,cell in enumerate(row):
            if len(cell) == 0:
                return False
            elif len(cell) > 1:
                for potentialval in cell:
                    newassignment = removefrom(assignment,i,j,potentialval)
                    ans = solve(newassignment)
                    if ans != False:
                        return ans
    return assignment
                            

sol = solve(options)
print(sol)
