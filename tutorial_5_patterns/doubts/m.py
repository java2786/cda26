rows = 8
cols = rows

for row in range(rows):
    # print(row)
    for col in range(cols):
        # print(row,col, " ", end="", sep="")
        # print(". ", end="")
        # print("* ", end="")
        if(col==0 or col == cols -1):
            print("*  ", end="")
        elif(row == col and row <= rows//2):
            print("*  ", end="")
        elif(row+col==rows-1 and row <= rows//2):
            print("*  ", end="")
        else:
            # print(row,col, " ", end="", sep="")
            print(".  ", end="")



    print()
