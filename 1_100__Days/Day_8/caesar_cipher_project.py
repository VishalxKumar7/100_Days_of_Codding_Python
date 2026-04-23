# CREATEING A CAESAR CIPHER
from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Enter what you want to do Encode Or Decode the message?: ")


def ceasar_cipher(text, shift, encoder_or_decoder):
    output_text = ""
    if encoder_or_decoder == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        
    print(f"Here is your {encoder_or_decoder}d message: {output_text}")


ceasar_cipher(text, shift, direction)