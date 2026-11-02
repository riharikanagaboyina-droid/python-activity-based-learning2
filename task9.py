budget=float(input("Budget: ")); n=int(input("Expenses: ")); expenses=[]
for _ in range(n):
 cat=input("Category: "); cur=input("Currency: "); amount=float(input("Amount: ")); rate=float(input("Home currency per unit: ")); cost=amount*rate*1.02; expenses.append((cat,cost)) if amount>=0 and rate>0 else print("Invalid amount/rate")
total=sum(x[1] for x in expenses); cats=[(cat,sum(x[1] for x in expenses if x[0]==cat)) for cat,cost in expenses]; print("Total=",total)