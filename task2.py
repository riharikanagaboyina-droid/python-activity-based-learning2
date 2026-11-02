n=int(input("Months: ")); bills=[]
for i in range(n):
 u=float(input("Units: ")); e=2*min(u,100)+3*min(max(u-100,0),100)+5*max(u-200,0); b=e+75+e*.05-(50 if u<=100 else 0); bills.append(b); print("Bill",i+1,round(b,2))
 if len(bills)>1 and bills[-2]>0 and (b-bills[-2])/bills[-2]>.30: print("UNUSUAL INCREASE")