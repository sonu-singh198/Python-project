import time

print("please insert your card")
time.sleep(5)
password = 1234
balance = 5000

pin = int(input("Enter your pin: "))

if pin == password:
    while True:
        print("""
          1 == balance
          2 == withdraw balance
          3 == deposit balance
          4 == exit
          """)

        try:
            option = int(input("please enter your choice: "))
        except ValueError:
            print("please enter a valid option")

        if option == 1:
            print(f"your current balance is {balance}")
        if option == 2:
            withdraw_amount = int(input("please enter withdraw amount: "))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {balance}")
        if option == 3:
            deposit_amount = int(input("please enter deposit amount: "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance}")
        if option == 4:
            break
else:
    print("wrong pin please try again")

