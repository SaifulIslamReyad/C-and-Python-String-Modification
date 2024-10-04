# we can do the same thing as L[i]='z' can do 
# L="abcccba"
# L[2]='k'
# L=L.replace(L[2],"k",1)
# print(L) #output: abkccb
L = "abcccba"
L = L[:2] + 'x' + L[3:]
print(L)  # Output: abxccba
