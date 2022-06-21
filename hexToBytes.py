'''
    hex to bytes 
'''

def hexToBytes(hexStr):
    '''
        hex to bytes
    '''
    return bytes.fromhex(hexStr)

def bytesToHex(byteStr):
    '''
        bytes to hex
    '''
    return byteStr.hex()

if __name__ == '__main__':
    hexStr = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
    print(hexToBytes(hexStr))