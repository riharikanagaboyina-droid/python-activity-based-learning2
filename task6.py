dist=float(input("Distance km: ")); n=int(input("Passengers: ")); base=1.2*min(dist,100)+max(0,min(dist-100,400))+max(0,dist-500)*.8
for _ in range(n): 
 age=int(input("Age: ")); cls=input("Class Sleeper/Chair/AC: ").lower(); can=input("Cancelled y/n: ").lower(); f={"sleeper":1,"chair":1.4,"ac":2}.get(cls,0); fare=base*f*(.5 if age<12 else .7 if age>=60 else 1); pay=fare+40; print("Invalid class" if not f else ("Penalty/refund",round(fare*.25+40,2),round(pay-(fare*.25+40),2)) if can=="y" else ("Payable",round(pay,2)))
print("Fare calculation complete")