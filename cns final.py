'''1st program'''
def encryptDecrypt(inpString):
    xorKey='H'
    length=len(inpString)
    for i in range(length):
        inpString=(inpString[:i]+chr(ord(inpString[i])^ord(xorKey))+inpString[i+1:]);
        print(inpString[i],end=' ')
    return inpString
if __name__=='__main__':
    sampleString="Hello World"
    print("encrypted String:", end='')
    sampleString=encryptDecrypt(sampleString)
    print("\n")
    print("decrypted String:",end='')
    encryptDecrypt(sampleString)

''' 2nd program'''
def encrypt(text,s):
    result=''
    for i in range(len(text)):
        char=text[i]
        if (char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result
text=input("enter the plain text to convert to ceaser cipher text:")
s=5
print("Text:"+text)
print("shift:"+str(s))
print("Cipher:"+encrypt(text,s))
def decrypt(text,x):
    result=''
    for i in range(len(text)):
        char=text[i]
        if (char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result
text=input("enter the ceaser cipher to convert the plain text:")
s=26-5
print("Text:"+text)
print("shift:"+str(s))
print("Cipher:"+decrypt(text,s))

'''3rd Program'''
def hill_cipher(msg, key):
    key_m = [[ord(key[i*3+j]) % 65 for j in range(3)] for i in range(3)]  
    msg_v = [ord(c) % 65 for c in msg]
    cipher = [
        chr(sum(key_m[i][j]*msg_v[j] for j in range(3)) % 26 + 65)
        for i in range(3)
    ]   
    return ''.join(cipher)
msg = input("Enter 3-letter message: ").upper()
key = input("Enter 9-letter key: ").upper()
print("Ciphertext:", hill_cipher(msg, key))

'''4th program '''
import os

def generate_key(length):
    return os.urandom(length)

def vernam_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Key must be same length as plaintext")
    
    return bytes([p ^ k for p, k in zip(plaintext.encode(), key)])

def vernam_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Key must be same length as ciphertext")
    
    return ''.join([chr(c ^ k) for c, k in zip(ciphertext, key)])

def main():
    plaintext = "Hello Vernam Cipher"
    
    key = generate_key(len(plaintext))
    print("Key:", key.hex())
    
    ciphertext = vernam_encrypt(plaintext, key)
    print("Cipher:", ciphertext.hex())
    
    decrypted = vernam_decrypt(ciphertext, key)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
    

'''5th program'''
import string
letters = string.ascii_letters
key = 4
text = input("Enter text: ")
cipher = ''.join(
    letters[(letters.index(c)+key) % len(letters)] if c in letters else c
    for c in text
)

plain = ''.join(
    letters[(letters.index(c)-key) % len(letters)] if c in letters else c
    for c in cipher
)
print("Cipher Text:", cipher)
print("Recovered Text:", plain)

'''6th program'''
from Crypto.Cipher import DES
key=b'secret_k'
msg=b'Hello123'
cipher=DES.new(key,DES.MODE_ECB)
ct=cipher.encrypt(msg)
pt=cipher.decrypt(ct)
print("Cipher text:",ct)
print("decrypted:",pt)

'''7th program'''
import hashlib
msg = "Hello"
sha256 = hashlib.sha256(msg.encode()).hexdigest()
sha1 = hashlib.sha1(msg.encode()).hexdigest()
print("SHA-256:", sha256)
print("SHA-1:", sha1)

'''9th porgram'''
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
message = b"Hello"
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)
try:
    public_key.verify(
        signature,
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Valid Signature")
except:
    print("Invalid Signature")
















