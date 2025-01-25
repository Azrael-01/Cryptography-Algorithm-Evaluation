import os
import time
import matplotlib.pyplot as plt
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES Encryption Function
def aes_encrypt(file_path, aes_key):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    cipher_aes = AES.new(aes_key, AES.MODE_ECB)
    padded_data = pad(file_data, AES.block_size)

    start_time = time.perf_counter()
    encrypted_data = cipher_aes.encrypt(padded_data)
    encryption_time = time.perf_counter() - start_time

    return encrypted_data, encryption_time

# AES Decryption Function
def aes_decrypt(encrypted_data, aes_key):
    cipher_aes = AES.new(aes_key, AES.MODE_ECB)

    start_time = time.perf_counter()
    decrypted_data = unpad(cipher_aes.decrypt(encrypted_data), AES.block_size)
    decryption_time = time.perf_counter() - start_time

    return decrypted_data, decryption_time

# RSA Encryption Function (Encrypts AES Key)
def rsa_encrypt_aes_key(aes_key, rsa_public_key):
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
    
    start_time = time.perf_counter()
    encrypted_key = cipher_rsa.encrypt(aes_key)
    encryption_time = time.perf_counter() - start_time

    return encrypted_key, encryption_time

# RSA Decryption Function (Decrypts AES Key)
def rsa_decrypt_aes_key(encrypted_key, rsa_private_key):
    cipher_rsa = PKCS1_OAEP.new(rsa_private_key)
    
    start_time = time.perf_counter()
    decrypted_key = cipher_rsa.decrypt(encrypted_key)
    decryption_time = time.perf_counter() - start_time

    return decrypted_key, decryption_time


rsa_key = RSA.generate(2048)
public_key = rsa_key.publickey()


aes_key = get_random_bytes(16)


test_files = ['sample.txt', 'data.csv', 'config.json', 'info.xml']


file_names = []
aes_encrypt_times = []
aes_decrypt_times = []
rsa_encrypt_times = []
rsa_decrypt_times = []


for file in test_files:
    if os.path.exists(file):
        print(f"\nProcessing file: {file}")
        file_names.append(file)
        
        
        encrypted_data_aes, aes_enc_time = aes_encrypt(file, aes_key)
        _, aes_dec_time = aes_decrypt(encrypted_data_aes, aes_key)
        
        
        encrypted_aes_key, rsa_enc_time = rsa_encrypt_aes_key(aes_key, public_key)
        _, rsa_dec_time = rsa_decrypt_aes_key(encrypted_aes_key, rsa_key)
        
        
        aes_encrypt_times.append(aes_enc_time)
        aes_decrypt_times.append(aes_dec_time)
        rsa_encrypt_times.append(rsa_enc_time)
        rsa_decrypt_times.append(rsa_dec_time)

        print(f"AES Encryption Time: {aes_enc_time:.10f}s, AES Decryption Time: {aes_dec_time:.10f}s")
        print(f"RSA Encryption Time: {rsa_enc_time:.10f}s, RSA Decryption Time: {rsa_dec_time:.10f}s")
    else:
        print(f"File {file} does not exist.")

plt.figure(figsize=(10, 6))
width = 0.2  


x = range(len(file_names))

plt.bar([p - width for p in x], aes_encrypt_times, width=width, label='AES Encryption', color='blue')
plt.bar(x, aes_decrypt_times, width=width, label='AES Decryption', color='cyan')
plt.bar([p + width for p in x], rsa_encrypt_times, width=width, label='RSA Encrypt AES Key', color='green')
plt.bar([p + 2*width for p in x], rsa_decrypt_times, width=width, label='RSA Decrypt AES Key', color='orange')


plt.yscale('log')


plt.xlabel('File Types')
plt.ylabel('Time (seconds) [Log Scale]')
plt.title('Encryption and Decryption Times (AES and RSA)')
plt.xticks(x, file_names)
plt.legend()
plt.tight_layout()
plt.show()
