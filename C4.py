def loaded_divider(vs, r1, r2, rl):
    rtotal=(r2*rl)/(r2+rl)
    vs * (rtotal / (r1 + rtotal))
    return(vs*(r1/(r1+r2)),vs*(rtotal/(r1+rtotal)))
