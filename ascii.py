'''
    script for converting between ascii numbers and alphabets
'''

def asciiToAlphabet(ascii):
    return chr(ascii)

def alphabetToAscii(alphabet):
    return ord(alphabet)

if __name__ == '__main__':
    asciis = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    ans = ''
    for i in asciis:
        ans += asciiToAlphabet(i)

    print(ans)