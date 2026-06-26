#making am atm
print("welcome to the ATM")

print("enter_1_to_check_balance")
print("enter_2_to_withdrawl_money")
print("enter_3_to_deposit_money")
print("enter_4_to_exit")

choice=int(input("enter your choice"))
balance=5000
if choice==1:
    print("current_balance:",balance)
elif choice==2:
    y=int(input("enter amount to withdraw"))
    if y>balance:
          print("insufficient balance")
    else:
          print("amount withdraw;",y)
          print("new balance=",balance-y)
                     
elif choice==3:
    z=int(input("enter the amount to be deposit"))
    print("new balance=",z+balance)
   
else:
    print("you have been exit")
