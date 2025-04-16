import hashlib

hashmd=input("Enter message:")
star=hashmd.encode()

star1=hashlib.md5(star)
star2=hashlib.sha1(star)

print("MD5:", star1.hexdigest())
print("SHA1:", star2.hexdigest())