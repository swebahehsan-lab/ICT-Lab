A=int(input("Enter A: "))

if A!=0 or A!=1:
    while A!=0 and A!=1:
        A=int(input("Enter A again: "))

B=int(input("Enter B: "))
if B!=0 or B!=1:
    while B!=0 and B!=1:
        B=int(input("Enter B again: "))


if A==1 and B==1:
    andd=1
    orr=1
    xor=0
elif A==0 and B==0:
    andd=0
    orr=0
    xor=0
elif A==1 and B==0:
    andd=0
    orr=1
    xor=1
elif A==0 and B==1:
    andd=0
    orr=1
    xor= 1

print("AND= ",andd)
print("OR= ",orr)
print("XOR= ",xor)
