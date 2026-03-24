valid_pin = "1234"
balance = 5000
user_pin = None
user_choice = None
is_valid = False 


def checkBal():
    # print("Current balance is Rs",balance,"/-",sep="")
    print(f"Current balance is Rs{balance}/-")

def withdraw(amount):
    global balance  
    
    if amount > balance:
        print("Insufficient Balance")
        return None
    else:
        balance = balance - amount
        return amount

def changePin():
    global valid_pin
    pp = input("Enter previous pin ")
    if pp == valid_pin:
        np = input("Enter new pin ")
        np2 = input("Enter new pin again")
        if(np == np2):
            valid_pin = np 
        else:
            print("Pin does not match")
    else:
        print("Previous pin is not correct.")
        
print("**** Welcome to Famous ATM ****")
while is_valid==False:
    # print("You are not valid user.")
    user_pin = input("Insert PIN: ")
    if user_pin == valid_pin:
        is_valid = True 
         
        while user_choice != "4":
            print("1. Check bal")
            print("2. Withdraw bal")
            print("3. Change pin")
            print("4. Exit")
            user_choice = input("Enter your choice: ") 
            if user_choice == "1":
                # print("asking to check bal")    
                checkBal()  
            elif user_choice == "2":
                # print("asking to withdraw bal")
                amount = int(input("Amount to debit: "))
                debitAmount = withdraw(amount)    
                print(f"Amount Debited: {debitAmount}")  
            elif user_choice == "3":
                # print("asking to change pin")
                changePin()      
            elif user_choice == "4":
                # print("asking to exit")  
                print("Bye Bye")    
            else:
                print("Invalid choice. Try again")      
    else:
        is_valid = False 
        print("Your inserted pin is wrong, Please try again.")
        
