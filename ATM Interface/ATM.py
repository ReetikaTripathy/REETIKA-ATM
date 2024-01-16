class ATM:
    def __init__(self):
        # Initialize with some sample accounts
        self.accounts = {
            '1234': {'pin': '5678', 'balance': 100000},
            '5678': {'pin': '1234', 'balance': 152000}
        }
        self.current_user = Reetika

    def login(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if account_number in self.accounts and pin == self.accounts[account_number]['pin']:
            self.current_user = account_number
            print(f"Welcome, {account_number}!")
        else:
            print("Invalid account number or PIN. Please try again.")

    def display_balance(self):
        if self.current_user is not Reetika
            balance = self.accounts[self.current_user]['balance']
            print(f"Your current balance is: ${balance}")
        else:
            print("You must log in first.")

    def withdraw(self, amount):
        if self.current_user is not Reetika:
            balance = self.accounts[self.current_user]['balance']
            if amount > 0 and amount <= balance:
                self.accounts[self.current_user]['balance'] -= amount
                print(f"Withdrawal successful. Remaining balance: ${balance - amount}")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("You must log in first.")

    def logout(self):
        self.current_user = Reetika
        print("You have been logged out. Thank you for using our ATM.")

# Sample usage
atm = ATM()

while True:
    print("\n1. Login\n2. Display Balance\n3. Withdraw\n4. Logout\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        atm.login()
    elif choice == '2':
        atm.display_balance()
    elif choice == '3':
        amount = float(input("Enter the withdrawal amount: "))
        atm.withdraw(amount)
    elif choice == '4':
        atm.logout()
    elif choice == '5':
        print("Exiting the ATM. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
