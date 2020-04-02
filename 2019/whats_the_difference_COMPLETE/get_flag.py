#!/usr/bin/python3
# taken from: https://github.com/AMACB/picoCTF-2019-writeups/tree/master/problems/whats-the-difference
c=open("whats_the_difference/cattos.jpg","rb").read()
k=open("whats_the_difference/kitters.jpg","rb").read()
diff=[(k[i], c[i]) for i in range(len(k)) if k[i] != c[i]]
flag=''.join(chr(c[i]) for i in range(len(k)) if k[i] != c[i])
print(flag)