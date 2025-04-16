import math

p=int(input("Enter the prime num:"))
q=int(input("Enter the primitive root:"))


a=int(input("Enter the private key of a:"))
b=int(input("Enter the private key of b:"))


if a>p and b>p:
    print("enter the valid private keys")


    
    

x=pow(q,a,p)  #public key of a
y=pow(q,b,p)  #public key of b

print("Public key of a:",x)
print("Public key of b:",y)


ka=pow(y,a,p)  #secret key of a
kb=pow(x,b,p)  #secret key of b

print("Secret key of a:",ka)
print("Secret key of b:",kb)

#The secret key must be always same

if ka==kb:
    print("****************Key exchange successfull************************")

    
    
