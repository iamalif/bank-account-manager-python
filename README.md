# bank-account-manager-python

A Python command-line application to manage bank accounts, 
built using Object-Oriented Programming (OOP) principles.

## About
This program simulates a basic banking system where users can create 
accounts, deposit and withdraw money, check balances, and list all 
accounts via a console menu. Includes overdraft prevention and 
withdrawal confirmation. Built as a personal OOP practice project.

## Features
- BankAccount class with private attributes (account number, owner name, balance)
- Getter and setter methods for all attributes
- Create a new bank account with duplicate account number prevention
- Deposit money to an account
- Withdraw money with overdraft prevention and confirmation prompt
- Check balance for a specific account
- List all existing accounts
- Pre-loaded test accounts for quick testing
- Input validation throughout

## How to Run
```bash
python bank_account.py
```

## Built With
- Python 3
- OOP — classes, private attributes, getter/setter methods
- Input validation functions for clean, reusable code

## Test Accounts
Three test accounts are pre-loaded on launch for quick testing:
| Account Number | Owner | Balance |
|---------------|-------|---------|
| 111 | Test 1 | 100 |
| 222 | Test 2 | 200 |
| 333 | Test 3 | 300 |
