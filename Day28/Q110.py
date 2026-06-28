accounts=[]

print("welcome to bank")

while True:
    print("1. Create Account")
    print("2. Search Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5.exit")
    
    x=int(input("enter your choice"))
    if x==1:
        Account_Number=int(input("enter your account number"))
        Accoun_Holder_Name=input("enter your name")
        Balance=int(input("enter your balance"))
        
        account={
            "account no.":Account_Number,
            "name":Accoun_Holder_Name,
            "balance":Balance
        }
        
        accounts.append(account)
        print("account added succesfully")
        
    elif x==2:
        
        y=int(input("enter your account number"))
        for account in accounts:
         if account["account no."]==y:
            print("account no.",account["account no."])
            print("name",account["name"])
            print("balance",account["balance"])
            
            break;
        if account["account no."]!=y:
            print("no account found")
            
    elif x==3:
        z=int(input("enter your account number to deposit money"))
        for account in accounts:
            if account["account no."]==z:
                u=int(input("enter the balance to deposit"))
                Balance=Balance+u
                print("amount has been deposited")
                print("new balance is",Balance)
                
    elif x==4:
        v=int(input("enter the account no  to  withdraw money "))
        for account in accounts:
            if account["account no."]==v:
                w=int(input("enter the amount to withdraw"))
                Balance=Balance-w
                print("money has been withdrawn")
                print("updated balance",Balance)
                
    elif x==5:
         print("exit")
         break;  
             
