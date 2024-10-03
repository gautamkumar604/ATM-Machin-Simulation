import time

# Make a class ATM for wrap the machine instructions
class ATM:
    def __init__(self,account_holder,balance,pin): # it is class constructor used for hiding the data.
        self.account_holder = account_holder #Public account_holder
        self._balance = balance # protected balance variable
        self.__pin = pin        # private PIN Number
        self._transactions = [] # To store transaction history

    # All function accept a self parameter for access the class constructor variable.
    def account_balance_inquiry(self): # this function is to check current balance in account.
        current_pin = int(input("Enter your 4-digit ATM PIN: "))
        if current_pin == self.__pin:
            print(f"Current Balance :  {self._balance}")
            return
        else:
            print("You are entered wrong PIN, Please try Again")
        return
    
    def cash_withdrawal(self): # this is a balance withdrawal function
        amount = int(input("Enter amount for withdrawal: "))
        current_pin = int(input("Enter your 4-digit ATM PIN: "))
        if current_pin == self.__pin:
            if self._balance > 0 and self._balance >= amount:
                self._balance -= amount
                self._transactions.append(f"withdraw amount: {amount}")
                print("Please wait, processing....\n") # for filling like real
                time.sleep(2) #This function is slow down the process for 2 seconds
                print(f"{amount} withdraw from your account successfully.")
                print(f"Available balance is : {self._balance}\n")
                return # return from the function without checking other instructions
            else:
                print("Your balance is not sufficient,Please check your balance.")
                return
        else:
            print("You are entered wrong PIN, Please try again")
        return

    def cash_deposit(self):
        amount = int(input("Enter amount for Deposit: "))
        current_pin = int(input("Enter your 4-digit ATM PIN: "))
        if current_pin == self.__pin:
            self._balance += amount
            self._transactions.append(f"Deposited amount: {amount}")
            print("Please wait, processing....") # for filling like real
            time.sleep(2) # This function is slow down the process for 2 seconds
            print(f"{amount} Deposited in your account successfully.")
            print(f"Current balance is : {self._balance}")
            return
        else:
            print("You are entered wrong PIN, Please try again")
        return
    
    def pin_change(self):
        print("\n##### Wecome to PIN change sevice #####")
        current_pin = int(input("Enter your old PIN: "))
        if current_pin == self.__pin:
            new_pin = int(input("Enter new 4-digit ATM PIN: "))
            confirm_pin = int(input("Please confirm your new ATM PIN: "))
            if new_pin == confirm_pin:
                self.__pin = confirm_pin
                print("\nYour PIN has been changed successfully.")
                print("Please remmember this PIN.. Thank you")
                return new_pin #return new pin because pin is changed
            else:
                print("The new PIN entries do not match. Please try again.")
                return self.__pin #return old pin because pin is not change. 
        else:
            print("Entered old pin is incorrect, Please try Again")
        return self.__pin #return old pin because pin is not change.
    
    def check_transactions_history(self):
        current_pin = int(input("Enter your ATM PIN: "))
        if current_pin == self.__pin:
            if self._transactions:
                print("")
                for transactions in self._transactions:
                    print(transactions)
                print(f"\nAvailable balance: {self._balance}")
                return
            else:
                print("No any transactions history")
                return
        else:
            print("Entered pin is incorrect, Please try Again")
        return
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def atm_menu():
    # After inserting card into the ATM machine. Machine fetch card user data automatically from the bank server database like name, balance, pin, etc. 
    # Manually enter card user data through the user input because database is not available.
    print("########### Insert your ATM Card ############\n")
    # name = str(input("Enter your name: "))
    # balance = int(input("Enter your account balance: "))
    # setPin =  int(input("Set your 4-digit ATM PIN: "))
    name = "Gautam Kumar"
    balance = 1000
    setPin = 1234
    i = 0 #initialize i variable for give chance to user select correct an option in maximum three attempts.

    atm_user = ATM(name,balance,setPin) #Create an object(atm_user) of ATM class. 
    print(f"Welcome {atm_user.account_holder}") #Print user name at the for welcome
    print("You have been successfully logged into the ATM Menu")
    
    while(True):
        print("""############# Enter your choice #################
        0 = Exit
        1 = Check Balance
        2 = Cash withdrawal
        3 = Cash Deposit 
        4 = Pin Change
        5 = Check Transactions
        """)

        try:
            option = int(input("Select an option (0-5): "))
        except:
            print("!!!You have select the wrong option!!!! \n~Please Choose a correct option(0-5)~\n")

        if option == 1:
            atm_user.account_balance_inquiry()
            break
        elif option == 2:
            atm_user.cash_withdrawal()
            # break
        elif option == 3:
            atm_user.cash_deposit()
            # break
        elif option == 4:
            pin = atm_user.pin_change()
            # print(f"Your new pin number is {pin}")
            break
        elif option == 5:
            atm_user.check_transactions_history()
            break
        elif option == 0:
            print("You have succesfully logged out.\nThanks to use our ATM.")
            break
        else:
            if  option < 0 or option > 5 and i < 3:
                print("~~~ Choose the right one option ~~~\nTry Again")
                i += 1
                continue
            else:
                print("You have Exceeded your maximum attempts limit!\nPrease try after sometimes!")
                break

atm_menu() # starting point of the programme.