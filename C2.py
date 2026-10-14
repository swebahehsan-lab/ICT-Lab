def parallel_resistance(resistors):

    total=0 
    for x in range(0,len(resistors)):
        total=total+1/resistors[x]
    total=1/total
    return total
    
