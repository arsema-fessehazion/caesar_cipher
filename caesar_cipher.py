# Encryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encrypting the code
def encrypt(text,shift):
    list_text = list(text)
    encoded_word = ""
    for letter in list_text:
        new_letter_position = alphabet.index(letter) + shift
        new_letter = alphabet[new_letter_position]
        encoded_word += new_letter
    print(f"Your encoded word is {encoded_word}!")

#decrypting the code
def decode(text,shift):
    list_text = list(text)
    decoded_word = ""
    for letter in list_text:
        new_letter_position = alphabet.index(letter) - shift
        new_letter = alphabet[new_letter_position]
        decoded_word += new_letter
    print(f"Your decoded word is {decoded_word}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text,shift)
else:
    decode(text,shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1','2','3','4','5','6','7','8','9']
space = [' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#combining the encrypting and decrypting functions
def caesar(direction,text,shift):
    list_text = list(text)
    caesar_word = ""
    for letter in list_text:
        if direction == "encode":
            new_letter_position = alphabet.index(letter) + shift
        else:
            new_letter_position = alphabet.index(letter) - shift
        new_letter = alphabet[new_letter_position]
        caesar_word += new_letter
    print(f"Your word is {caesar_word}")

caesar(direction,text,shift)
