import base64
from Crypto import Random
from Crypto.Cipher import AES

f = open('CSS\data.bin','r')
input = f.read().split('|')
input[1] = base64.b64decode(input[1]).hex()
pq = [982457503, 982457513]
d = 294661167473102753
e = 672977
n = 965222755025570039

""" kAES = [721786126185516225,3239110541552888201,5224165158219227231110,102491508211381099]
keys = ['0e12946d1f41c36028e57925092da628','11b37cddc5305307c2757ac7be9b38fcca','e12946d1f41c36028e57925092da62811b37cddc5305307c2757ac7be9b38fcca'] """

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


