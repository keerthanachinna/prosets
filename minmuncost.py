def minmuncost(str1,str2,m,n):
if(m==0):
return n
if n==0
return m
if (str1[m-1]==str2[n-1]):
return minmuncost(str1,str2.,m-1,n-1)
return 1+min(minmuncost(str1+str2,m,n-1),minmuncost(str1,str2,m-1,n),minmuncost(str1,str2,m-1,n-1))
str1="BALL"
str2="BALLON"
print minmuncost(str1,str2,len(str1),len(str))
