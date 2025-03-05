import math

def generate_keys(p, q):
    n = p * q
    etf = (p - 1) * (q - 1)

    e = 3
    while math.gcd(e, etf) != 1:
        e += 2

    for d in range(2, etf):
        if (d * e) % etf == 1:
            return e, d, n  

    

def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

if __name__ == "__main__":
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))

    if not (all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1)) and
            all(q % i != 0 for i in range(2, int(math.sqrt(q)) + 1))):
        print("Both numbers must be prime")
        exit()

    keys = generate_keys(p, q)
    
    

    e, d, n = keys  
    message = int(input("Enter the message m: "))

    print(f"Public key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")

    ciphertext = encrypt(message, e, n)
    print(f"Encrypted message: {ciphertext}")

    decrypted_message = decrypt(ciphertext, d, n)
    print(f"Decrypted message: {decrypted_message}")
