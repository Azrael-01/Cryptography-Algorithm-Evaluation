import rsa
import time

# Generating RSA public and private keys (2048 bits)
(public_key, private_key) = rsa.newkeys(2048)


message = b'This is a sample message for RSA encryption.'


start_time = time.perf_counter()
encrypted_message = rsa.encrypt(message, public_key)
encryption_time = time.perf_counter() - start_time


start_time = time.perf_counter()
decrypted_message = rsa.decrypt(encrypted_message, private_key)
decryption_time = time.perf_counter() - start_time


print(f"Encrypted (RSA): {encrypted_message[:50]}...")  
print(f"Decrypted (RSA): {decrypted_message.decode('utf-8')}")
print(f"RSA Encryption Time: {encryption_time:.8f} seconds")
print(f"RSA Decryption Time: {decryption_time:.8f} seconds")
