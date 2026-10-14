volts = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]


z=0
dec[]=0
for x in range(0,len(voltages)):
    

    if volts[x]<volt[x+1]:
        if inc!=0:
            
        inc=0
        dec[z]+=1
        


    elif volts[x]>volt[x+1]:
        z+=1
        
