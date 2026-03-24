# write a function to square a given number

def getSquare(x):
    return x*x 

getDouble = lambda x:x+x 


n = 4
print(getSquare(n))
print(getDouble(n))

marks = [78,39,42,91,63,47]

# passing score is 45
# find all pass students
# find all fail students
def getPassStudents(marks):
    list = []
    for mark in marks:
        if(mark >= 45):
            list.append(mark)
            
    return list 

print(getPassStudents(marks))

failStudents = list(filter(lambda mark: mark<45, marks))

print(failStudents)