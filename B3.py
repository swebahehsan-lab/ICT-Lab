readings=[3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2]
count=0
high=readings[0]
low=readings[0]
total=0
count1= 0
avg=0

for x in range(len(readings)):
    count1+=1
    
    total+=readings[x]
    if readings[x]>3.2:
        count+=1
    if readings[x]>high:
        high=readings[x]
    if readings[x]<low:
        low=readings[x]

avg=total/count1

print(" highest value is ",high)
print("lowest value is ",low)
print("total is ",total)
print("count is",count)
print("Average is ",avg)
