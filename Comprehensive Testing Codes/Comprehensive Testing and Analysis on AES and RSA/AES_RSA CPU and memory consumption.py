import psutil
import time
import matplotlib.pyplot as plt
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


def pad_data(data, block_size):
    padding_len = block_size - len(data) % block_size
    return data + bytes([padding_len] * padding_len)


def unpad_data(data):
    padding_len = data[-1]
    return data[:-padding_len]


def test_aes_resource_usage(data, aes_key):
    process = psutil.Process()

   
    start_cpu = process.cpu_percent(interval=None)
    start_memory = process.memory_info().rss  

    cipher = AES.new(aes_key, AES.MODE_ECB)
    padded_data = pad_data(data, AES.block_size)

    # AES encryption
    start_time = time.perf_counter()
    encrypted_data = cipher.encrypt(padded_data)
    encryption_time = time.perf_counter() - start_time

    # AES decryption
    start_time = time.perf_counter()
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_data = unpad_data(decrypted_data)
    decryption_time = time.perf_counter() - start_time

    # Get CPU and memory usage after encryption
    end_cpu = process.cpu_percent(interval=None)
    end_memory = process.memory_info().rss

    cpu_usage = end_cpu - start_cpu
    memory_usage = (end_memory - start_memory) / (1024 * 1024)  

    return encryption_time, decryption_time, cpu_usage, memory_usage


def test_rsa_resource_usage(data, rsa_key):
    process = psutil.Process()

    
    start_cpu = process.cpu_percent(interval=None)
    start_memory = process.memory_info().rss

    cipher_rsa = PKCS1_OAEP.new(rsa_key.publickey())

    # RSA encryption
    start_time = time.perf_counter()
    encrypted_data = cipher_rsa.encrypt(data)
    encryption_time = time.perf_counter() - start_time

    # RSA decryption
    cipher_rsa_dec = PKCS1_OAEP.new(rsa_key)
    start_time = time.perf_counter()
    decrypted_data = cipher_rsa_dec.decrypt(encrypted_data)
    decryption_time = time.perf_counter() - start_time

  
    end_cpu = process.cpu_percent(interval=None)
    end_memory = process.memory_info().rss

    cpu_usage = end_cpu - start_cpu
    memory_usage = (end_memory - start_memory) / (1024 * 1024) 

    return encryption_time, decryption_time, cpu_usage, memory_usage


aes_key = get_random_bytes(16)  
rsa_key = RSA.generate(2048)  # 


aes_results = []
rsa_results = []


print("Testing AES Resource Usage:")
aes_results.append(test_aes_resource_usage(data, aes_key))

print("\nTesting RSA Resource Usage:")
rsa_results.append(test_rsa_resource_usage(data, rsa_key))


aes_times, aes_decrypt_times, aes_cpu, aes_memory = zip(*aes_results)
rsa_times, rsa_decrypt_times, rsa_cpu, rsa_memory = zip(*rsa_results)


fig, axs = plt.subplots(4, 1, figsize=(10, 15))


axs[0].bar(["AES", "RSA"], [aes_times[0], rsa_times[0]], color=['blue', 'orange'])
axs[0].set_title("Encryption Time Comparison")
axs[0].set_ylabel("Time (seconds)")


axs[1].bar(["AES", "RSA"], [aes_decrypt_times[0], rsa_decrypt_times[0]], color=['blue', 'orange'])
axs[1].set_title("Decryption Time Comparison")
axs[1].set_ylabel("Time (seconds)")


axs[2].bar(["AES", "RSA"], [aes_cpu[0], rsa_cpu[0]], color=['blue', 'orange'])
axs[2].set_title("CPU Usage Comparison")
axs[2].set_ylabel("CPU Usage (%)")


axs[3].bar(["AES", "RSA"], [aes_memory[0], rsa_memory[0]], color=['blue', 'orange'])
axs[3].set_title("Memory Usage Comparison")
axs[3].set_ylabel("Memory Usage (MB)")


plt.tight_layout()
plt.show()
