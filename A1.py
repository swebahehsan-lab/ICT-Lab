volt=int(input("Please enter the voltage"))
resistance=int(input("Please enter the ressitance"))

print("The current is",volt/resistance)
if (volt/resistance)>2:
    print("Fuse will blow")
else:
    
 print("Circuit is safe")
