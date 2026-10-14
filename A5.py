r1=int(input("Enter R1: "))
r2=int(input("Enter R2: "))
r3=int(input("Enter R3: "))

if r1>r2 and r1>r3:
    print("Largest: ",r1,"Ohm")
elif r2>r1 and r2>r3:
    print("Largest: ",r2,"Ohm")
elif r3>r1 and r3>r2:
    print("Largest: ",r3,"Ohm")

if r1<r2 and r1<r3:
    print("Smallest: ",r1,"Ohm")
elif r2<r1 and r2<r3:
    print("Smallest: ",r2,"Ohm")
elif r3<r1 and r3<r2:
    print("Smallest: ",r3,"Ohm")
