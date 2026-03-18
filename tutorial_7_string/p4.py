# email = "brain-mentors@gmail.com"
# email = "brain.mentors@gmail.com"
# email = "_brain.mentors@gmail.com"
email = "@brain.mentors@gmail.com"

""" 
should contain @ only 1
should not start with @
should end with @gmail.com
"""
isValid = True

if ('@' in email)==False:
    isValid = False
elif((email.count('@')==1)==False):
        isValid = False
elif(email.startswith("@")==True):
        isValid = False
elif(email.endswith("@gmail.com")==False):
        isValid = False

if(isValid == True):
    print("valid")
else:
    print("invalid")
    
    
