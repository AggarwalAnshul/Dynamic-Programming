def printsss(matrix):
    for layer in reversed(matrix):
        printss(layer)
        
def printss(matrix):
    print("  ",end="")
    for index in range(0, len(matrix[0])):
        print(index, end="   ")
    print()
    for index in range(0, len(matrix[0])):
        print("--------",end="")
    print()
    #print("\n------------------------------------------------------")
    index = 0
    for row in matrix:
        print(str(index)+"|",end="   ")
        for col in row:
            print(col, end="   ")
        index+=1
        print()
    print()
