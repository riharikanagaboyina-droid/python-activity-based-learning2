items=[]; n=int(input("Products: "))
for _ in range(n): name=input("Name: "); cat=input("Category grocery/clothing/electronics: ").lower(); p=float(input("Price: ")); q=int(input("Quantity: ")); r={"grocery":.05,"clothing":.12,"electronics":.18}.get(cat,-1); items.append((name,p*q,r)) if p>=0 and q>=0 and r>=0 else print("Invalid item")
sub=sum(x[1] for x in items); disc=min(sub*.1,1000) if sub>=5000 else 0; tax=sum(x[1]*(sub-disc)/sub*x[2] for x in items) if sub else 0
print("Subtotal",sub,"Discount",disc,"Tax",round(tax,2),"TOTAL",round(sub-disc+tax,2))