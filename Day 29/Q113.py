#calculator
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit")
    
    x=int(input("enter your choice"))
    
    if x==1:
        A=float(input("enter your first number"))
        B=float(input("enter your second number"))
        
        sum_num=A+B
        print("the answer is=",sum_num)
        
    elif x==2:
        A=float(input("enter your first number"))
        B=float(input("enter your second number"))
        
        diff_num=A-B
        print("the answer is=",diff_num)
        
    elif x==3:
        A=float(input("enter your first number"))
        B=float(input("enter your second number"))
        
        multi_num=A*B
        print("the answer is=",multi_num) 
        
    elif x==4:
        A=float(input("enter your first number"))
        B=float(input("enter your second number"))
        if B==0:
            print("invalid response")
        
        div_num=A/B
        print("the answer is=",div_num)
        
    elif x==5:
        print("you have been exit") 
        break;
