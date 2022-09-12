import copy
filled = []
options = []
for i in range(9):
    filled.append([])
    options.append([])
    for j in range(9):
        filled[i].append(False)
        options[i].append([1,2,3,4,5,6,7,8,9])

def removefrom(assignment,i,j,possible):
   # print("GOT" + str(possible) +" "+ str(i) +" "+ str(j))
   # print(assignment)

    new = copy.deepcopy(assignment)
    new[i][j] = [possible]
    for rows in range(9):
        if possible in new[rows][j] and rows!= i:
            new[rows][j].remove(possible)
    for cols in range(9):
        if possible in new[i][cols] and cols != j:
            new[i][cols].remove(possible)


    for rows in range(9):
        for cols in range(9):
            if ((rows//3 == i//3 and cols//3 == j //3)) and not(rows == i and cols == j):
                if possible in new[rows][cols]:
                    new[rows][cols].remove(possible)
    #print("NOW")
    #print(new)
    return new

def solve(assignment,completed):
    cancont = False
    for row in assignment:
        for cell in row:
            if len(cell) == 0:
                return False
    for row in completed:
        for item in row:
            if item == False:
                cancont = True
    if cancont == False:
        return assignment
    for i,row in enumerate(assignment):
        for j,cell in enumerate(row):
            if len(cell) > 1:
                for potentialval in cell:
                    newassignment = removefrom(assignment,i,j,potentialval)
                    completed[i][j] = True
                    ans = solve(newassignment,completed)
                    if ans != False:
                        return ans
    return False








def prettyprint(assignment):
    for row in assignment:
        for col in row:
            print(str(col) + "   |   ", end = "")
        print("\n")    
                                  

sol = solve(options,filled)
print(sol)
