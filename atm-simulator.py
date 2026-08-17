balance = 5000
pin = "1234"

entered_pin = input("Enter your PIN:")

if entered_pin == pin:
    while True:
        print("\n === ATM simulator ===")
        print("1.' check Balance', \n2. 'Deposit',\n3.'withdraw',\n 4. 'Exit'")
        
        choice= input("Enter choice:")
        
        if choice=="1":
           print("Your balance is: rs",balance) 
           
        elif choice =="2":
            amount=float(input("Enter deposit number:"))
            balance+= amount
            print("Amount deposited successfully!")
            print("New balance: rs",balance)
        elif choice =="3":
            amount= float(input("Enter withdrawal amount:"))
            
            if amount <= balance:
                balance-= amount
                print("please collect your cash.")
                print("Remaining balance : rs",balance)
                
            else:
                print("Insufficient balance!")
                
        elif choice =="4":
            print("Thank you for using the ATM!")
            break
        
        else:
            print("Invalid choice!")
            
else:
    print("Incorrect PIN!")
            
            
            