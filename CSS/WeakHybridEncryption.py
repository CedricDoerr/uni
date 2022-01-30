import base64
from crypto import Random
from crypto.Cipher import AES

f = open('CSS\data.bin','r')
input = f.read().split('|')
input[1] = base64.b64decode(input[1]).hex()
pq = [982457503, 982457513]
d = 294661167473102753
e = 672977
n = 965222755025570039

ans = []
ansHex=[]
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def encryptRSA(cipher):
    i=0
    keys = []
    while (i < 4):
        keys.append('0'+ hex(int(cipher[16*i:16*(i+1)], 16) ^ d % n)[2:])
        print(int(cipher[16*i:16*(i+1)], 16) ^ d % n)
        i += 1
    return keys
keys = encryptRSA(input[0])
print(keys)
print(input[1], len(input[1])/16)
""" for i in kAES:
    ans.append(i^d%n)

for i in ans:
    ansHex.append(hex(i))
print(ans,ansHex) """

for key in keys:
    cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC)
    print(cipher.decrypt(bytes.fromhex(input[1])).hex())


