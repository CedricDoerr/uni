
f = open('/Users/cedricdorr/Documents/Programmieren/Test/input.txt','r')
input = f.read().split('\n')
input = [n.split() for n in input]

clear_1 = [99, 100, 57, 48, 118, 117, 98, 121]
key_1 = []
i = 0

while (i < len(input[0])/2):
    if(clear_1[i] > int(input[0][i], 16)):
        key_1.append(127 - clear_1[i] + int(input[0][i], 16))
    else:
        key_1.append(int(input[0][i], 16) - clear_1[i])
    i += 1
while (i < len(input[1])):
    if(clear_1[i-8] > int(input[1][i], 16)):
        key_1.append(127 - clear_1[i-8] + int(input[1][i], 16))
    else:
        key_1.append(int(input[1][i], 16) - clear_1[i-8])
    i += 1

print(key_1)

ans = []

for t in input:
    help = ''
    for n, j in enumerate(t):
        if(int(j, 16) - key_1[n] < 0): 
            help += (chr(int(j, 16) - key_1[n] + 127 ))
        else:
            help += (chr(int(j, 16) - key_1[n]))
    ans.append(help)
key = ''
for n in key_1:
    key += chr(n)
print(ans)
print(key)