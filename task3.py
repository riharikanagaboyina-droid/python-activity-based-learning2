name=input("Patient: "); c=float(input("Consultation: ")); d=float(input("Diagnostics: ")); t=float(input("Treatment: "))
g=c+d+t; disc=g*.10 if g>=5000 else 0; bill=g-disc; p=float(input("Payment: "))
if min(c,d,t,p)<0 or p>bill: print("Invalid charges/payment")
else: print(name,"Gross",g,"Concession",disc,"Bill",bill,"Balance",bill-p,"Status",("PAID" if p==bill else "PARTIALLY PAID"))