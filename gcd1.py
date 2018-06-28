def find_gcd(N, Q):
	
	while(Q):
		N, Q = Q, N % Q
	
	return N
		
# Driver Code	 
l = [5, 1, 1]

n1 = l[0]
n2 = l[1]
gcd = find_gcd(n1, n2)

for i in range(2, len(l)):
	gcd = find_gcd(gcd, l[i])
	
print(gcd)
le = [1,2,3]

a1 = le[0]
a2 = le[1]
gcd=find_gcd(a1, a2)

for i in range(2,len(le)):
    gcd = find_gcd(gcd, le[i])
    print(gcd)
