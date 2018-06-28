def find_gcd(N,Q):
    while(Q):
        N,Q = Q, N % Q
     
    return N
      L= [1,2,3,4,5]
n1 = L[0]
n2 = L[1]
gcd = find_gcd(n1, n2)
for i in range(2, len(L)):
    gcd_L = find_gcd(gcd, L[i])
    print(gcd_L)
R=[1,2,1,1,1]
a1=R[0]
a2=R[1]
gcd=find_gcd(a1,a2)
for i in range(2,len(R)):
gcd_R=find_gcd(gcd,R[i])
print(gcd_R)
