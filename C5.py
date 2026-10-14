def star_to_delta(ra, rb, rc):
    r_num = (ra * rb) + (rb * rc) + (rc * ra)
    R_ab=r_num/rc
    R_bc=r_num/ra
    R_ca=r_num/rb
    return (round(R_ab, 2), round(R_bc, 2), round(R_ca, 2))
