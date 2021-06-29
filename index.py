import Cryptomath
import os
import random
import sys
import rabinMiller


def main():
    makeKeyFiles('RSA_demo', 1024)


def generateKey(keySize):
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    print('Generating p prime...')
    # p = RabinMiller.generateLargePrime(keySize)
    p = rabinMiller.generateLargePrime(keySize)
    print('Generating q prime...')
    # q = RabinMiller.generateLargePrime(keySize)
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if Cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e.
    print('Calculating d that is mod inverse of e...')
    d = Cryptomath.findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return publicKey, privateKey


def makeKeyFiles(name, keySize):
    # Crea dos archivos 'x_pubkey.txt' y 'x_privkey.txt'
    # (donde x es el valor en el nombre) con los enteros n, eyd, e escritos en ellos,
    # delimitado por una coma.
    # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' 
    # (where x is the value in name) with the the n,e and d,e integers written in them,
    # delimited by a comma.
    if os.path.exists('%s_pubkey.txt' % name) or os.path.exists('%s_privkey.txt' % name):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete '
                 'these files and re-run this program.' % (name, name))
    publicKey, privateKey = generateKey(keySize)
    print()
    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % name)

    fo = open('%s_pubkey.txt' % name, 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()
    print()
    print('The private key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % name)

    fo = open('%s_privkey.txt' % name, 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()
    # Si se ejecuta makeRsaKeys.py (en lugar de importarse como un módulo) llame
    # la función main ().
    # If makeRsaKeys.py is run (instead of imported as a module) call
    # the main() function.


if __name__ == '__main__':
    main()
