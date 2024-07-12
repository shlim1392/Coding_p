def xor_decrypt(T):
    known_str = "CHICKENS"
    key = ord(T[0]) ^ ord(known_str[0])
    
    decrypted_message = ''.join(chr(ord(char) ^ key) for char in T)
    
    return decrypted_message

T = input()

print(xor_decrypt(T))
