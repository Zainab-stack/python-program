#ATM machine

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"

    def authenticate(self):
        user_pin = input("Enter your 4-digit PIN: ")
        if user_pin == self.pin:
            return True
        else:
            print("Invalid PIN. Try again.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: $"))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

    def deposit(self):
        amount = float(input("Enter deposit amount: $"))
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")


def main():
    atm = ATM(balance=1000)  # Initial balance

    while True:
        print("\nATM Menu:")
        print("1. Authenticate")
        print("2. Check Balance")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if atm.authenticate():
                print("Authenticated successfully.")
        elif choice == "2":
            atm.check_balance()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            atm.deposit()
        elif choice == "5":
            print("Thank you for using our ATM.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
