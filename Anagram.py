# _01 Anagram Check

# Given two strings, check to see if they are anagrams. 
# An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."
# "clint eastwood" is an anagram of "old west action"

a = "god public relations"
b = "crap built on lies dog"
a = str(a).replace(' ','').lower()
b = str(b).replace(' ','').lower()
ascii_stra=[]
ascii_strb=[]
for char in a:
    ascii_stra.append(ord(char))
for char in b:
    ascii_strb.append(ord(char))

#print ascii_stra
#print ascii_strb

for i,key in enumerate(ascii_stra):
    for j,nextk in enumerate(ascii_stra):
        if(i==j):
            pass
        else:
            if ascii_stra[i]>ascii_stra[j]:
                temp=ascii_stra[i]
                ascii_stra[i]=ascii_stra[j]
                ascii_stra[j]=temp
#print ascii_stra
for i,key in enumerate(ascii_strb):
    for j,nextk in enumerate(ascii_strb):
        if(i==j):
            pass
        else:
            if ascii_strb[i]>ascii_strb[j]:
                temp=ascii_strb[i]
                ascii_strb[i]=ascii_strb[j]
                ascii_strb[j]=temp
#print ascii_strb
if(ascii_stra==ascii_strb):
    print "Anagram!"
else:
    print "Not an Anagram!"