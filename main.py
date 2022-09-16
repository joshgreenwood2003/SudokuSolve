import copy
options = [[[j+1 for j in range(9)] for n in range(9)] for i in range(9)]
filled = [[False for n in range(9)] for i in range(9)]







def assign(assignment,i,j,value):
    assignment[i][j] = [value] #set value
    #set rows and cols
    for iter in range(9):
        if value in assignment[iter][j] and iter!= i:
            assignment[iter][j].remove(value)
            if len(assignment[iter][j]) == 0:
                return False
        if value in assignment[i][iter] and iter != j:
            assignment[i][iter].remove(value)
            if len(assignment[i][iter]) == 0:
                return False 

    modi = i//3
    modj = j//3
    for rows in range(modi*3,modi*3+3):
        for cols in range(modj*3,modj*3 + 3):
            if not(rows == i and cols ==j):
                if value in assignment[rows][cols]:
                    assignment[rows][cols].remove(value)
                    if len(assignment[rows][cols]) == 0:
                       return False

    #for rows in range(9):
    #    for cols in range(9):
    #        if ((rows//3 == i//3 and cols//3 == j //3)) and not(rows == i and cols == j):
    #            if value in assignment[rows][cols]:
    #                assignment[rows][cols].remove(value)
    #                if len(assignment[rows][cols]) == 0:
    #                   return False
    return assignment


def solve(assignment,completed):
    for i,row in enumerate(assignment):
        for j,cell in enumerate(row):
            if completed[i][j]== False:
                for potentialval in cell: 
                    tempcompleted = copy.deepcopy(completed)
                    tempcompleted[i][j] = True
                    partialsol = assign(copy.deepcopy(assignment),i,j,potentialval)
                    if partialsol != False:
                        ans = solve(partialsol,tempcompleted)
                        if ans != False:
                            return ans
                return False
    return assignment
   






#initial = ["1-8------","-3--6---7","--7-5-1--","-7-5---2-","-4--9---3","---------","48-2--3--","---8----1","-5-4----9"]
initial = ["-2---96--","58--62---","7-6-3--19","472---56-","95-6--342","-38--41-7","817--5--6","3--7----1","----9--7-"]
for i,row in enumerate(initial):
    for j,c in enumerate(row):
        if c != "-":
            filled[i][j] = True
            options = assign(copy.deepcopy(options),i,j,int(c))

                     

sol = solve(options,filled)



def prettyprint(assignment):
    for row in assignment:
        for col in row:
            print(str(col) + "   |   ", end = "")
        print("\n")    
   


prettyprint(sol)
