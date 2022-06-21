'''
     A simple script to generate a plaintext from ciphertext
'''

def ciphertoplain(ciphertext):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintexts = []

    for i in range(1, 27):
        plaintext = ''
        for cipherletter in ciphertext:
            if cipherletter != ' ':
                plaintext += alphabets[(alphabets.index(cipherletter) - i) % 26]
            else:
                plaintext += ' '
        plaintexts.append(plaintext)
    
    return plaintexts


if __name__ == '__main__':
    ciphertext = 'BGZRD ANZS OQNFQZL ZOOQNUD'
    ans = ciphertoplain(ciphertext)
    for a in ans:
        print(a)
