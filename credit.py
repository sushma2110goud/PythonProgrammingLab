def credit(balance,transactions,amount):
  balance+=amount
  transactions.append(amount)
  print(amount,"credited successfully")
  return balance,transactions 
def debit(balance,transactions,amount):
    if amount>balance:
        print("insuficient balance!")
    else:
        balance-=amount
        transactions.append(-amount)
        print(amount,"debited succesfully")
    return balance,transactions
    
def show_balance(balance):
    print("current balance: rs{balance}")
    
def last_5_transactions(transaction):
    print("last 5 transactions:")
    for transaction in transactions[-5:]:
      balance = 0
transactions=[]
print("bank applications")
print("1.credit")
print("2.debit")
print("3.show balance")
print("4.last 5 transactions")
print("5.exit")

choice = input("enter your choice:")

if choice=="1":
    amount=int(input("enter amount to credit:"))

def credit(balance,transactions,amount):
    if amount>balance:
        print("insufficient amount")
    else:
        balance=amount
        transactions.append(amount)
        print(amount,"debited successfully")
        return balance,transactions,amount
def show_balance(balance):
    print("current balance: rs{balance}")
    
    
