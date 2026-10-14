num=int(input("How many resistors? "))
equ=0
for x in range(1,num+1):
    r=int(input("Enter R"+str(x)+": "))
    equ+=r

print("Total Resistance",equ)
