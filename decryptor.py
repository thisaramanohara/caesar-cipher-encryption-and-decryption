#Author : Thisara Manohara

key = 3

def createAlphabet():
    alphabet = {}
    for i in range(26):
        alphabet[chr(i+97)] = i
    return alphabet

alphabet = createAlphabet()


def decryptedText(cipherText):
    decryptedMsg = ""
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())
    for i in range(len(cipherText)):
        if(cipherText[i]==' '):
            decryptedMsg += ' '
            continue
        letterId = ord(cipherText[i])-97
        letterId = (letterId - key) % 26
        position = val_list.index(letterId)
        decryptedMsg += key_list[position]
    return decryptedMsg

cipherText = input("Enter the cipher text : ")
print("Decrypted Text : " + decryptedText(cipherText))
