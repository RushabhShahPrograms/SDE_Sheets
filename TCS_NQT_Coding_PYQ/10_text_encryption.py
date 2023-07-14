'''
Problem Statement

The Caesar cipher is a type of substitution cipher in which each alphabet in the plaintext or messages is shifted by a number of places down the alphabet.
For example,with a shift of 1, P would be replaced by Q, Q would become R, and so on.
To pass an encrypted message from one person to another, it is first necessary that both parties have the ‘Key’ for the cipher, so that the sender may encrypt and the receiver may decrypt it.
Key is the number of OFFSET to shift the cipher alphabet. Key can have basic shifts from 1 to 25 positions as there are 26 total alphabets.
As we are designing custom Caesar Cipher, in addition to alphabets, we are considering numeric digits from 0 to 9. Digits can also be shifted by key places.
For Example, if a given plain text contains any digit with values 5 and keyy =2, then 5 will be replaced by 7, “-”(minus sign) will remain as it is. Key value less than 0 should result into “INVALID INPUT”

Example 1:
Enter your PlainText: All the best
Enter the Key: 1

The encrypted Text is: Bmm uif Cftu

Write a function CustomCaesarCipher(int key, String message) which will accept plaintext and key as input parameters and returns its cipher text as output.
'''

def ceaser(text,key):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
      # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)
        elif(char.isdigit()):
            result += str(int(char) + key)
        elif(char == '-'):
            result += '-'
        elif (char.isspace()):
            result += " "
    return result
#check the above function
text = input("Enter your plain text:")
key = int(input("Enter the key:"))
print(ceaser(text,key))