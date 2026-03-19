rows = 17
cols = int(rows*.7)

for row in range(rows):
    # print(row)
    for col in range(cols):
        # print(row,col, " ", end="", sep="")
        # print(". ", end="")
        # print("* ", end="")
        if(row==0 or row == rows-1 or col==0 or col==cols-1):
            print("* ", end="")
        else:
            # print(row,col, " ", end="", sep="")
            print("  ", end="")

    

    print()
