# 2.10 ATM PIN Simulator (With Balance Management)

VALID_PIN = "5678"
tries = 3
account_balance = 7500.0  # Setting a starting balance for the user
is_verified = False

# Part 1: PIN Verification Loop
while tries > 0:
    pin_input = input("Enter your 4-digit PIN: ")
    
    if pin_input == VALID_PIN:
        print("Login Successful!\n")
        is_verified = True
        break
    else:
        tries -= 1
        print(f"Wrong PIN. Attempts left: {tries}")

if tries == 0:
    print("ATM Card Blocked! Too many wrong attempts.")

# Part 2: ATM Transaction Menu (Runs only if PIN is correct)
while is_verified:
    print("----- ATM MENU -----")
    print("1. View Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Exit")
    
    option = input("Choose an option (1-4): ")
    
    if option == "1":
        print(f"Your current balance is: Rs. {account_balance}\n")
        
    elif option == "2":
        withdrawal = float(input("Enter withdrawal amount: "))
        
        if withdrawal > account_balance:
            print("Transaction Failed: Not enough balance!\n")
        elif withdrawal <= 0:
            print("Transaction Failed: Invalid amount!\n")
        else:
            account_balance -= withdrawal
            print(f"Rs. {withdrawal} withdrawn successfully.")
            print(f"Available Balance: Rs. {account_balance}\n")
            
    elif option == "3":
        deposit = float(input("Enter deposit amount: "))
        
        if deposit <= 0:
            print("Transaction Failed: Invalid amount!\n")
        else:
            account_balance += deposit
            print(f"Rs. {deposit} deposited successfully.")
            print(f"Updated Balance: Rs. {account_balance}\n")
            
    elif option == "4":
        print("Thank you for using the ATM. Have a nice day!")
        break  # Exits the ATM menu loop
        
    else:
        print("Invalid option! Please choose a valid option.\n")
