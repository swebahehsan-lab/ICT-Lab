volts = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

cstart = volts[0]
cend = volts[0]
z = 1
dec = 1

for x in range(len(volts) - 1):
  
  if volts[x + 1] < volts[x]:
    if z == 1:
      cstart = volts[x]  
    z += 1
    cend = volts[x + 1]  
  else:
    z = 1
  if z > dec:
    dec = z
    max_start = cstart
    max_end = cend

print(
    f"Longest continuous drop: {dec} minutes Started at: {max_start} V Ended"
    f" at: {max_end} V"
)
