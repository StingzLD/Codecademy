# Decode a Caeser Cipher message that has an offset of 10
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alphabet = "abcdefghijklmnopqrstuvwxyz"
offset = 10

def decoder(message, offset):
    decoded_message = ""
    for char in message:
        if alphabet.find(char) == -1:
            decoded_message += char
        else:
            new_char = alphabet[(alphabet.find(char) + offset) % len(alphabet)]
            decoded_message += new_char
    return decoded_message

print(decoder(message, offset))

# Encode a message using the Caeser Cipher with an offset of 10
message = "i wonder what julius caesar would think about ciphers if he was alive today. do you think he would would pushed us to even better ciphers than we have now?"
alphabet = "abcdefghijklmnopqrstuvwxyz"
offset = 10

def coder(message, offset):
    coded_message = ""
    for char in message:
        if alphabet.find(char) == -1:
            coded_message += char
        else:
            new_char = alphabet[(alphabet.find(char) - offset) % len(alphabet)]
            coded_message += new_char
    return coded_message

print(coder(message, offset))

# Decode first message to figure out how to decode the second message
first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
offset = 10
print(decoder(first_message, offset))

# Decode second message using the clue from the deciphered first message
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
offset = 14
print(decoder(second_message, offset))

