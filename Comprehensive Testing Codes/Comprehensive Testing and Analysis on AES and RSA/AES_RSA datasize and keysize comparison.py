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


def test_aes_key_sizes(data_sizes):
    key_sizes = [128, 192, 256]  
    aes_results = {"key_sizes": [], "data_sizes": [], "encryption_times": [], "decryption_times": []}

    for key_size in key_sizes:
        for data_size in data_sizes:
            aes_key = get_random_bytes(key_size // 8)
            cipher = AES.new(aes_key, AES.MODE_ECB)
            data = get_random_bytes(data_size)
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

            
            aes_results["key_sizes"].append(key_size)
            aes_results["data_sizes"].append(data_size)
            aes_results["encryption_times"].append(encryption_time)
            aes_results["decryption_times"].append(decryption_time)

    return aes_results


def test_rsa_key_sizes(data_sizes):
    key_sizes = [1024, 2048, 4096]  
    rsa_results = {"key_sizes": [], "data_sizes": [], "encryption_times": [], "decryption_times": []}

    for key_size in key_sizes:
        key = RSA.generate(key_size)
        public_key = key.publickey()

        cipher_rsa_enc = PKCS1_OAEP.new(public_key)
        cipher_rsa_dec = PKCS1_OAEP.new(key)

        for data_size in data_sizes:
            data = get_random_bytes(min(data_size, key_size // 8 - 42))  # RSA can only encrypt small amounts of data

            # RSA encryption
            start_time = time.perf_counter()
            encrypted_data = cipher_rsa_enc.encrypt(data)
            encryption_time = time.perf_counter() - start_time

            # RSA decryption
            start_time = time.perf_counter()
            decrypted_data = cipher_rsa_dec.decrypt(encrypted_data)
            decryption_time = time.perf_counter() - start_time

            rsa_results["key_sizes"].append(key_size)
            rsa_results["data_sizes"].append(data_size)
            rsa_results["encryption_times"].append(encryption_time)
            rsa_results["decryption_times"].append(decryption_time)

    return rsa_results


def plot_results(aes_results, rsa_results):
    
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 1, 1)
    for data_size in set(aes_results["data_sizes"]):
        data_indices = [i for i, size in enumerate(aes_results["data_sizes"]) if size == data_size]
        plt.plot([aes_results["key_sizes"][i] for i in data_indices],
                 [aes_results["encryption_times"][i] for i in data_indices],
                 label=f'AES Encryption Time - Data Size {data_size} bytes', marker='o')
        plt.plot([aes_results["key_sizes"][i] for i in data_indices],
                 [aes_results["decryption_times"][i] for i in data_indices],
                 label=f'AES Decryption Time - Data Size {data_size} bytes', marker='o')
    
    plt.title('AES Performance')
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid()

    
    plt.subplot(2, 1, 2)
    for data_size in set(rsa_results["data_sizes"]):
        data_indices = [i for i, size in enumerate(rsa_results["data_sizes"]) if size == data_size]
        plt.plot([rsa_results["key_sizes"][i] for i in data_indices],
                 [rsa_results["encryption_times"][i] for i in data_indices],
                 label=f'RSA Encryption Time - Data Size {data_size} bytes', marker='o')
        plt.plot([rsa_results["key_sizes"][i] for i in data_indices],
                 [rsa_results["decryption_times"][i] for i in data_indices],
                 label=f'RSA Decryption Time - Data Size {data_size} bytes', marker='o')
    
    plt.title('RSA Performance')
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid()

  
    plt.tight_layout()
    plt.show()


data_sizes = [64, 512, 2048]  


print("Running AES and RSA performance tests with different data sizes...")
aes_results = test_aes_key_sizes(data_sizes)
rsa_results = test_rsa_key_sizes(data_sizes)


plot_results(aes_results, rsa_results)
