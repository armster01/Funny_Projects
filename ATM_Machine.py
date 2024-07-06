class ATMMachine:
    def __init__(self,pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []
    
    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def balance_inquiry(self):
        if self.check_pin():
            print(f"Your current balance is: ${self.balance}")
            self.transaction_history.append("Balance inquiry")
        else:
            print("Incorrect PIN")

    def cash_withdrawal(self,amount):
        if self.check_pin():
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have withdrawn ${amount}. Your new balance is: ${self.balance}")
                self.transaction_history.append(f"Withdrew ${amount}")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect PIN")

    def cash_deposit(self, amount):
        if self.check_pin():
            self.balance += amount
            print(f"You have deposited ${amount}. Your new balance is: ${self.balance}")
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("Incorrect PIN")
    
    def change_pin(self, new_pin):
        if self.check_pin():
            self.pin = new_pin
            print("Your PIN has been changed successfully")
            self.transaction_history.append("PIN changed")
        else:
            print("Incorrect PIN")

    def show_transaction_history(self):
        if self.check_pin():
            print("Transaction History: ")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("Incorrect PIN")

atm = ATMMachine(pin="2824")

while True:

        print("\n ATM Machine Menu:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")
    
        if choice == "1":
            atm.balance_inquiry()
        
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            atm.cash_withdrawal(amount)

        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            atm.cash_deposit(amount)

        elif choice == "4":
            new_pin = input("Enter new PIN: ")
            atm.change_pin(new_pin)

        elif choice == "5":
            atm.show_transaction_history()

        elif choice == "6":
            print("Thank you for using the ATM. \nHave a good day.")
            break

        else:
            print("Invalid choice. Please try again once more.")
