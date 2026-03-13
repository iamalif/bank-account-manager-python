"""
Write a class called BankAccount with private attributes:

account_number
owner_name
balance

Include getter/setter methods. Then create a program where the user can:

Create a new account
Deposit money
Withdraw money (prevent overdraft)
Check balance
List all accounts
"""

class BankAccount:
    """Represents a bank account with private attributes and getter/setter access.

    Uses name mangling (double underscore prefix) to enforce encapsulation,
    so attributes can only be accessed through the defined getter/setter methods.
    """

    def __init__(self, account_number, owner_name, balance=0):
        # Private attributes — accessed via getters/setters to enforce encapsulation
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = balance

    # --- Setters: allow controlled modification of private attributes ---

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_owner_name(self, owner_name):
        self.__owner_name = owner_name

    def set_balance(self, balance):
        # Directly sets the balance; callers are responsible for passing a valid value
        self.__balance = balance

    # --- Getters: allow read access to private attributes ---

    def get_account_number(self):
        return self.__account_number

    def get_owner_name(self):
        return self.__owner_name

    def get_balance(self):
        return self.__balance

    def __str__(self):
        # Human-readable summary of the account, used when printing the object
        return f"Account Number: {self.__account_number}, Owner: {self.__owner_name}, Balance: {self.__balance}"

# --- Input validation helpers ---
# These functions loop until the user provides valid input,
# preventing crashes from bad data types or empty strings.

def get_positive_int(prompt):
    """Repeatedly prompts the user until a non-negative integer is entered."""
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Number needs to be positive.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_positive_float(prompt):
    """Repeatedly prompts the user until a strictly positive float is entered.

    Used for monetary amounts — zero is rejected because depositing or
    withdrawing nothing is not a meaningful operation.
    """
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("Number needs to be positive.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a positive float.")

def get_non_empty_string(prompt):
    """Repeatedly prompts the user until a non-empty string is entered."""
    while True:
        text = input(prompt)
        if text == "":
            print("Invalid input. Text field can not be empty.")
        else:
            return text

# --- Bank operations ---

# Global list that holds all BankAccount objects created during the session
accounts = []

# def find_account(account_number):
#     for account in accounts:
#         if account.get_account_number() == account_number:
#             return account
#         else:
#             return None

def create_account():
    """Prompts the user for account details and adds a new BankAccount to the list.

    Checks for duplicate account numbers before creating to ensure uniqueness.
    """
    account_number = get_positive_int("Enter account number: ")
    owner_name = get_non_empty_string("Enter owner name: ")
    balance = get_positive_float("Enter account balance: ")
    #account_flag = False

    # Reject duplicate account numbers — each account number must be unique
    for account in accounts:
        if account.get_account_number() == account_number:
            print("Account number already in use.")
            return None

    account = BankAccount(account_number, owner_name, balance)

    accounts.append(account)
    print(account)

def deposit_money():
    """Finds the target account and adds the deposit amount to its balance.

    Uses account_flag to track whether the account was found, since breaking
    out of the loop early means we can't rely on the loop completing normally.
    """
    account_number = get_positive_int("Which account to deposit to: ")
    deposit_amount = get_positive_float("How much do you want to deposit: ")
    account_flag = False  # Tracks whether a matching account was found

    for account in accounts:
        if account.get_account_number() == account_number:
            new_balance = account.get_balance() + deposit_amount
            account.set_balance(new_balance)
            print(f"This is your new balance: {new_balance}")
            print(account)
            account_flag = True
            break
        else:
            #print("Account number is incorrect")
            account_flag = False
            continue

    if account_flag == False:
        print("Account number is incorrect.")

def withdraw_money():
    """Withdraws money from an account after user confirmation.

    Prevents overdraft by rejecting withdrawals that exceed the current balance.
    Requires explicit 'yes' confirmation before modifying the account.
    """
    account_number = get_positive_int("Which account to withdraw from: ")
    withdraw_amount = get_positive_float("How much do you want to withdraw: ")
    confirmation = confirm_action()  # Ask the user to confirm before proceeding
    account_flag = False  # Tracks whether a matching account was found

    if confirmation:
        for account in accounts:
            if account.get_account_number() == account_number:
                # Overdraft protection: reject if withdrawal exceeds available balance
                if account.get_balance() < withdraw_amount:
                    print("Insufficient balance")
                    break
                new_balance = account.get_balance() - withdraw_amount
                account.set_balance(new_balance)
                print(f"This is your new balance: {new_balance}")
                print(account)
                account_flag = True
                break
            else:
                #print("Account number is incorrect")
                account_flag = False
        if account_flag == False:
            print("Account number is incorrect.")
    else:
        print("Withdrawal cancelled.")

def check_balance():
    """Looks up and displays the balance for the given account number."""
    account_number = get_positive_int("Enter account number: ")
    account_flag = False  # Tracks whether a matching account was found

    for account in accounts:
        if account.get_account_number() == account_number:
            balance = account.get_balance()
            print(f"This is your balance: {balance}")
            print(account)
            account_flag = True
            break
        else:
            #print("Account number is incorrect")
            account_flag = False
            continue

    if account_flag == False:
        print("Account number is incorrect")

def list_accounts():
    """Prints all accounts, or a message if none have been created yet."""
    if len(accounts) == 0:
        print("No accounts exist.")
    else:
        for account in accounts:
            print(account)

def user_menu():
    """Main interactive loop that displays the menu and routes user choices."""
    while True:
        print("\nEnter 1 to create a new account")
        print("Enter 2 to deposit money")
        print("Enter 3 to withdraw money")
        print("Enter 4 to check balance")
        print("Enter 5 to list all accounts")
        print("Enter 0 to Exit\n")

        choice = get_positive_int("Type your choice and press enter: ")

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 0:
            print("\nGoodbye!")
            break
        else:
            print("\nChoice needs to be between 0 to 5.")

def confirm_action():
    """Prompts the user for a yes/no confirmation and returns a boolean.

    Loops until a valid response is given — accepts any capitalisation of
    'yes' or 'no' via .lower().
    """
    while True:
        choice = get_non_empty_string("Are you sure? (yes/no): ")

        if choice.lower() == "yes":
            return True
        elif choice.lower() == "no":
            return False
        else:
            print("\nChoice needs to be either 'Yes' or 'No'")


def main():
    # Pre-populate the account list with test data so the program is
    # immediately usable without needing to create accounts manually
    test_account_1 = BankAccount(111, "Test 1", 100)
    test_account_2 = BankAccount(222, "Test 2", 200)
    test_account_3 = BankAccount(333, "Test 3", 300)
    accounts.append(test_account_1)
    accounts.append(test_account_2)
    accounts.append(test_account_3)
    user_menu()

# Only run the program when this file is executed directly,
# not when it is imported as a module
if __name__ == "__main__":
    main()