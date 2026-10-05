cp = float(input("Enter Cost Price : "))
sp = float(input("Enter Selling  Price : "))
if sp > cp :
    profit = sp - cp
    print("Profit = " , profit )
elif sp < cp :
    loss = cp - sp
    print("Loss = " , loss )

else :
    print(" No Profit ..... No Loss ") 
