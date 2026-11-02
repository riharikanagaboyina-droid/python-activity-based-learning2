p=[("Basic",199,2,200,28,20,.5),("Smart",299,5,500,56,15,.4),("Max",399,10,1000,84,10,.3)]
d=float(input("Data GB: ")); c=int(input("Call minutes: ")); days=int(input("Validity days: ")); budget=float(input("Budget: "))
costs=[(price+max(0,d-dl)*dr+max(0,c-cl)*cr,name,v) for name,price,dl,cl,v,dr,cr in p]; [print(x[1],round(x[0],2)) for x in costs]
ok=[x for x in costs if x[2]>=days and x[0]<=budget]; print("Best:",min(ok) if ok else "NO SUITABLE PLAN")