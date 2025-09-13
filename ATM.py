class bank:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def verify_pin(self):
        a = 3
        for i in range(a):
            entered_pin = input("Enter your pin: ")
            if entered_pin == self.pin:
                print("Pin verified successfully")
                return True
            else:
                print(f"Incorrect Pin. Attempts left: {(a - i - 1)}")
        print("Account blocked. Contact Bank")
        return False

    def deposit(self, amount):
        self.balance += amount
        print(f"RS {amount} Deposited.")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"RS {amount} Withdrawn")

    def check_balance(self):
        print(f"Your Balance is: RS {self.balance}")


# Input from user
name = input("Enter your name: ")
pin = input("Set your pin: ")
account = bank(name, pin, balance=10000)

if account.verify_pin():
    print(f"\nWelcome {account.name}!\n")

    # 🏦 ATM-style menu
    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amt = int(input("Enter amount to deposit: "))
            account.deposit(amt)

        elif choice == "2":
            amt = int(input("Enter amount to withdraw: "))
            account.withdraw(amt)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you.")
            break

        else:
            print("Invalid choice. Try again.")
