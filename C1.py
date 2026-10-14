def ohms_current(v,r):
    return v/r

def power_dissipated(v, r):
    i= ohms_current(v,r)
    return (i**2)*r

