import time


def account_balance_inquiry():
    print(f"Current Balance in your account is  {balance}")

def cash_withdrawal():
    global balance
    try:
        withdraw_amount = int(input("Enter amount for withdraw from your account:-\n\t"))
    except ValueError:
        # Handle the case where input is not a valid integer
        print("Entered amount is not satisfied | Please enter ammount in number format")

    if balance >= withdraw_amount:
        balance -= withdraw_amount
        print("\nWithdrawal is completed")
        print(f"Available balance is {balance}")
    else:
        print("Your account balance is not sufficient | Please check your balance")
        return  # Exit the function if input is invalid
    
def cash_deposit():
    global balance
    try:
        depodit_amount = float(input("Enter amount for depodit in your account:-\n"))
    except ValueError:
        # Handle the case where input is not a valid integer
        print("Entered amount is not satisfied | Please enter ammount in number format")

    balance += depodit_amount
    print(f"\n{depodit_amount} is Deposited in your account successfully")
    print(f"Current balance is {balance}")
    
def pin_change():
    pass
def transaction_history():
    pass

print("Please insert your card\n")
i = 0
pin = 1234
balance = 5000.00
password = int(input("~~~~~~~~~ ENTER YOUR fOUR DIGIT ATM PIN NUMBER ~~~~~~~~~~~ \n"))

# time.sleep(2)

if(pin==password):
    print("you have been logged into the Menu")
    while(True):
        print("""############# Enter your choice #################
        0 = Cancel
        1 = Check Balance
        2 = Cash withdrawal
        3 = Cash Deposit 
        4 = Pin Change
        5 = Check Transactions
        """)
        try:
            option = int(input("Choose any one correct option\n"))
        except ValueError:
            print("!!!You have select the wrong option!!!! \n~Please Choose the correct option~")
        
        if option == 1:
            account_balance_inquiry()
            break
        elif option == 2:
            cash_withdrawal()
            break
        elif option == 3:
            cash_deposit()
            break
        elif option == 4:
            print("Change your pin number")
            break
        elif option == 5:
            print("History")
            break
        elif option == 0:
            print("######### You have succesfully logged out ###########")
            break
        else:
            if  option < 0 or option > 5 and i < 3:
                print("~~~ Choose the right one option ~~~ \n Try Again \n\n")
                i += 1
                continue
            else:
                print("You have Exceeded your maximum attempts limit! \n Prease try after sometimes!")
                break
else:
    print("You are enterd the wrong pin number! \nPlease try Again")
