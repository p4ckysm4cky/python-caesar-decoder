decryptedText = []
def cipherInput():
    global plainText
    global key
    print("Welcome to the Caesar Cipher")
    plainText = input("Please enter the word you would like to decrypt\n:").lower()

    while True:
        key = input("Enter your key below\n:")
        if key.isnumeric() == True and int(key) <26 and int(key) >0:
            break
        else:
            print("---Please only enter numbers that are less than 26---")
    key = int(key)

def cipherOutput():
    for i in plainText:
        if ord(i) > 96 and ord(i) < 123:
            ordinal = ord(i) - key
            if ordinal < 97:
                ordinal = 123 - (97 - ordinal)
        else:
            ordinal = ord(i)
        
        letter = chr(ordinal)

        
        decryptedText.append(letter)

    print("Here is your decrypted message:\n---------------------------")    
    decryptNorm = ''.join(decryptedText)
    print(decryptNorm)


cipherInput()
cipherOutput()