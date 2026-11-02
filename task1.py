n=int(input("Applicants: ")); a=[]
for i in range(n):
 name=input("Name: "); m=[float(input("Subject mark: ")) for _ in range(3)]; att=float(input("Attendance: ")); inc=float(input("Income: ")); avg=sum(m)/3; ok=avg>=80 and min(m)>=60 and att>=75 and inc<=300000; a.append((avg,att,-inc,-i,name)) if ok else print(name,"NOT ELIGIBLE")
a.sort(reverse=True); [print(i+1,x[4],round(x[0],2),"AWARDED" if i<2 else "") for i,x in enumerate(a)]