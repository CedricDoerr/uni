p = 473383
q = 835391
n = p*q
phi = (p-1)*(q-1)
e = 65537
d = 0

def euklid(a_0,b_0):
    i = 0
    a,b,q_ek,r = [],[],[],[]
    a.append(a_0)
    b.append(b_0)
    while(b[i]>0):
        q_ek.append(a[i]//b[i])
        r.append(a[i]%b[i])
        a.append(b[i])
        b.append(r[i])
        i += 1
    return a,b,q_ek,r

print(euklid(240120,65537))
print("P = "+str(p)+" Q = "+str(q)+" N = "+str(n)+" Phi = "+str(phi)+" E = "+str(e)+" D = "+str(d))