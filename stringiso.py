MAX_CHARS = 256
 def aIsomorphic(str1, str2):
    m = len(str1)
    n = len(str2)
 if m != n:
        return False
 marked = [False] * MAX_CHARS
map=[-1]*MAX_CHARS
for i in xrange(n):
if map[ord(str1[i])]==-1:
   if marked[ord(str2[i])]==True:
                return Fals
                marked[ord(str2[i])]=True
  map[ord(str1[i])]=str2[i]
 elif map[ord(str1[i])]!=str2[i]:
            return False
            return True
 print aIsomorphic("aab","xxy")


