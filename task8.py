q=int(input("Quantity: ")); mu=float(input("Material units/product: ")); mr=float(input("Material rate: ")); w=float(input("Wastage %: "))
lh=float(input("Labour hours: ")); lr=float(input("Labour rate: ")); machine=float(input("Machine cost: ")); price=float(input("Selling price/product: ")); target=float(input("Target margin %: "))
mat=q*mu*mr; cost=mat+mat*w/100+lh*lr+machine; rev=q*price; profit=rev-cost; margin=profit/rev*100 if rev else 0
print("Invalid input") if q<=0 or min(mu,mr,w,lh,lr,machine,price,target)<0 else print("Cost",cost,"Revenue",rev,"Profit",profit)