# CREATEING A CAESAR CIPHER

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Enter what you want to do Encode Or Decode the message?: ")


#**********************************Encryption***********************************************
def encrypt(text, shift):
    encrypted_message = ""
    for letter in text:
        for i, alpha in enumerate(alphabet):
            if alpha == letter:
                shift_position = i + shift
                shift_position %= len(alphabet)
                encrypted_message += alphabet[shift_position]

    print(f"Here is your encoded message: {encrypted_message}")

#### OR

# def encrypt(text, shift):
#     encrypted_message = ""
#     for letter in text:
#         shifted_position = alphabet.index(letter) + shift
#         shifted_position %= len(alphabet)
#         encrypted_message += alphabet[shifted_position]
        
#     print(f"Here is your encoded message: {encrypted_message}")


#encrypt(text, shift)

# **************************************Decryption***************************************
def decrypt(text, shift):
    decryted_message = ""
    for letter in text:
        for i, alpha in enumerate(alphabet):
            if alpha == letter:
                shift_position = i - shift
                shift_position %= len(alphabet)
                decryted_message += alphabet[shift_position]

    print(f"Here is your decripyted message: {decryted_message}")

#### OR

# def encrypt(text, shift):
#     decryted_message = ""
#     for letter in text:
#         shifted_position = alphabet.index(letter) + shift
#         shifted_position %= len(alphabet)
#         decryted_message += alphabet[shifted_position]
        
#     print(f"Here is your decryted message: {decryted_message}")


#decrypt(text, shift)

# *******************************Combined Encryption & Decryption***********************************

def ceasar_cipher(text, shift, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift *= -1
    for letter in text:
        for i, alpha in enumerate(alphabet):
            if alpha == letter:
                shift_position = i + shift
                shift_position %= len(alphabet)
                output_text += alphabet[shift_position]

    print(f"Here is your {encode_or_decode}d message: {output_text}")


ceasar_cipher(text, shift, direction)