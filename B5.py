
count1=0
count5=0
countr=0
resistor=1

while resistor!=0:

    resistor=int(input("Enter resistance"))
    if resistor>=99.0 and resistor<=101.0:
        count1+=1
    elif resistor>=95.0 and resistor<=105.0:
        count5+=1
    elif resistor<95.0 or resistor>105.0:
        countr+=1

print(count1)
print(count5)
print(countr)
