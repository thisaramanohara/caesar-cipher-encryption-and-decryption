#Author : Thisara Manohara

key = 3

def createAlphabet():
    alphabet = {}
    for i in range(26):
        alphabet[chr(i+97)] = i
    return alphabet

alphabet = createAlphabet()

def encryptedText(plainText):
    encryptedMsg = ""
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())
    for i in range(len(plainText)):
        if(plainText[i]==' '):
            encryptedMsg += ' '
            continue
        letterId = ord(plainText[i])-97
        letterId = (letterId + key) % 26
        position = val_list.index(letterId)
        encryptedMsg += key_list[position]
    return encryptedMsg

plainText = input("Enter the plain text : ")
print("Encrypted Text : " + encryptedText(plainText))


