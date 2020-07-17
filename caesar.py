def encripted(string,shift):

    cipher = ''

    for char in string:
        if char == "":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char)+shift - 65) % 26+65)
        elif char.isnumeric():
            cipher = cipher + char

        elif char.islower():
            cipher = cipher + chr((ord(char)+shift - 97) % 26+97)

    return cipher

def decryption(string , shift):

    decipher = ""
    for char in string:
        if char.isnumeric():
            decipher = decipher + char
        if char.isupper():
            decipher = decipher + chr((ord(char) - shift - 65) % 26+65)
        if char.islower():
            decipher = decipher  + chr((ord(char)-shift - 97) % 26+97)

    return decipher




print("what you want to do?")
print("1.Encryption")
print("2.Decryption")
inputvalue = int(input("Enter Number "))
if inputvalue == 1:
        text = input("enter text ")
        s = int(input("enter the shift key "))
        print("the original string is : ", text)
        print("encripted text is : ", encripted(text, s))
else:
      text = input("enter encripted text ")
      s = int(input("enter shift key "))
      print("the encriptrd string is : ", text)
      print("Decripted or orginal text is : ",decryption(text,s))



