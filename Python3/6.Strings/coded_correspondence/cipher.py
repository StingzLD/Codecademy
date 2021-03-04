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

# Decode message by brute forcing the offset value
brute_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(len(alphabet)):
    print("Offset of " + str(i) + ":\n" + decoder(brute_message, i) + "\n")

# Decode message using the Vigenere Cipher with the keyword of friends
vigenere_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

def vigenere_decoder(message, keyword):
    decoded_message = ""
    keyword_index = 0
    keyword_letter = ""
    for char in message:
        if alphabet.find(char) == -1:
            decoded_message += char
        else:
            keyword_letter = keyword[keyword_index]
            #print(keyword_index, keyword_letter)
            new_char = alphabet[(alphabet.find(char) - alphabet.find(keyword_letter)) % len(alphabet)]
            decoded_message += new_char
            #print(decoded_message)
            keyword_index = (keyword_index + 1) % len(keyword)
    return decoded_message

print(vigenere_decoder(vigenere_message, keyword))

# Encode and decode a message using the Vigenere Cipher
vigenere_message_to_code = "let's make sure that we can code and decode properly, shall we?"
keyword = "shibby"

def vigenere_coder(message, keyword):
    coded_message = ""
    keyword_index = 0
    keyword_letter = ""
    for char in message:
        if alphabet.find(char) == -1:
            coded_message += char
        else:
            keyword_letter = keyword[keyword_index]
            #print(keyword_index, keyword_letter)
            new_char = alphabet[(alphabet.find(char) + alphabet.find(keyword_letter)) % len(alphabet)]
            coded_message += new_char
            #print(coded_message)
            keyword_index = (keyword_index + 1) % len(keyword)
    return coded_message

print(vigenere_coder(vigenere_message_to_code, keyword))
print(vigenere_decoder(vigenere_coder(vigenere_message_to_code, keyword), keyword))
