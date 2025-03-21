p=int(input("enter p value"))
r=int(input("enter r value"))
t=int(input("enter t value"))
A=p*(1+r/100)**t
CI=A-p
print(round(CI,2))
