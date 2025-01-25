from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

# Generating random AES key and IV (16 bytes for AES-128)
key = get_random_bytes(16)
iv = get_random_bytes(16)

# AES in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

message = b'This is a sample message for AES encryption.'


start_time = time.perf_counter()
ciphertext = cipher.encrypt(pad(message, AES.block_size))
encryption_time = time.perf_counter() - start_time


cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
start_time = time.perf_counter()
decrypted_message = unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
decryption_time = time.perf_counter() - start_time


print(f"Encrypted (AES): {ciphertext[:50]}...")  
print(f"Decrypted (AES): {decrypted_message.decode('utf-8')}")
print(f"AES Encryption Time: {encryption_time:.8f} seconds")
print(f"AES Decryption Time: {decryption_time:.8f} seconds")
