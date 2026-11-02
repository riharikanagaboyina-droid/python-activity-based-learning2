name=input("Employee: "); b=float(input("Basic: ")); a=float(input("Allowance: ")); h=float(input("Overtime hours: ")); i=float(input("Incentive: "))
g=b*1.2+a+h*200+i; d=0 if g<=15000 else (g-15000)*.05 if g<=30000 else 750+(g-30000)*.1
print("Invalid input") if min(b,a,h,i)<0 else print(name,"Gross",g,"Deduction",d,"NET",g-d)
print("Salary statement complete")