f = open('CSS\oneTimePadIN.txt','r') 
input = f.read().split('\n') 
input = [n.split() for n in input] 
clear_1 = ['c','d','9','0','v','u','b','y'] 
key_1 = [] 
i = 0 

while (i < len(input[0])/2): 
    key_1.append(int(input[0][i],16)^ord(clear_1[i]))
    i += 1 

while (i < len(input[1])): 
    key_1.append(int(input[1][i],16)^ord(clear_1[i-8])) 
    i += 1 
print(key_1) 
ans = [] 
for t in input: 
    help = '' 
    for n, j in enumerate(t): 
        help += (chr((int(j, 16)^key_1[n]))) 
    ans.append(help) 
key = '' 
for n in key_1: 
    key += chr(n) 
print(ans)
print(key)