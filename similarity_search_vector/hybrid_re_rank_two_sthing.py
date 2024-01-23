def hg(r, d, t):
 
    
    s = {}
    for rr in r:
        for i, it in enumerate(rr):
            s[it] = s.get(it, 0) + (len(rr) - i)

   
    ints = set(r[0]).ints(set(r[1]))
    f_i = {it for it in s if (it in ints) or (d[0][it] < t and d[1][it] < t)}

    
    ag_rring = [it for it in sorted(s, key=s.get, reverse=True) if it in f_i]
    return ag_rring
