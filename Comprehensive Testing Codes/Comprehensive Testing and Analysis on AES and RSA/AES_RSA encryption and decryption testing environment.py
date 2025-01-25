import time
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def pad_data(data, block_size):
    padding_len = block_size - len(data) % block_size
    return data + bytes([padding_len] * padding_len)


def unpad_data(data):
    padding_len = data[-1]
    return data[:-padding_len]


def test_aes_performance(key_size, data):
    aes_key = get_random_bytes(key_size // 8)
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

    return encryption_time, decryption_time


def test_rsa_performance(key_size, data):
    key = RSA.generate(key_size)
    public_key = key.publickey()

    cipher_rsa_enc = PKCS1_OAEP.new(public_key)
    cipher_rsa_dec = PKCS1_OAEP.new(key)

    # RSA encryption
    start_time = time.perf_counter()
    encrypted_data = cipher_rsa_enc.encrypt(data)
    encryption_time = time.perf_counter() - start_time

    # RSA decryption
    start_time = time.perf_counter()
    decrypted_data = cipher_rsa_dec.decrypt(encrypted_data)
    decryption_time = time.perf_counter() - start_time

    return encryption_time, decryption_time


def update_data_size_label():
    input_text = text_entry.get().encode('utf-8')
    data_size = len(input_text)  
    data_size_label.config(text=f"Input Data Size: {data_size} bytes")


def perform_test():
   
    input_text = text_entry.get().encode('utf-8')
    aes_key_size = int(aes_key_var.get())
    rsa_key_size = int(rsa_key_var.get())

    if not input_text:
        messagebox.showerror("Input Error", "Please enter some text to encrypt.")
        return

    
    aes_enc_time, aes_dec_time = test_aes_performance(aes_key_size, input_text)

    
    rsa_enc_time, rsa_dec_time = test_rsa_performance(rsa_key_size, input_text)

  
    algorithms = ['AES Encryption', 'AES Decryption', 'RSA Encryption', 'RSA Decryption']
    times = [aes_enc_time, aes_dec_time, rsa_enc_time, rsa_dec_time]

  
    plt.style.use('ggplot')  
    plt.figure(figsize=(10, 6))
    
   
    bars = plt.bar(algorithms, times, color=['#4caf50', '#ff9800', '#f44336', '#2196f3'])

    for bar, time_val in zip(bars, times):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0001, f'{time_val:.10f}s', 
                 ha='center', va='bottom', fontsize=10, color='black')

   
    plt.title(f'Performance Comparison of AES-{aes_key_size} and RSA-{rsa_key_size}\n'
              f'Text: "{text_entry.get()}"', fontsize=14)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.xlabel('Operation', fontsize=12)

   
    plt.tight_layout()
    plt.show()


root = tk.Tk()
root.title("Encryption Performance Tester")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.geometry(f'{screen_width}x{screen_height}')
root.configure(bg="#e6e6fa")  


title_label = tk.Label(root, text="Encryption Performance Tester", font=("Helvetica", 24, "bold"), bg="#e6e6fa", fg="#4b0082")
title_label.pack(pady=20)


tk.Label(root, text="Enter Text to Encrypt:", font=("Helvetica", 16), bg="#e6e6fa", fg="#4b0082").pack(pady=10)
text_entry = tk.Entry(root, width=70, font=("Helvetica", 14))  
text_entry.pack(pady=5)


data_size_label = tk.Label(root, text="Input Data Size: 0 bytes", font=("Helvetica", 14), bg="#e6e6fa", fg="#4b0082")
data_size_label.pack(pady=10)


text_entry.bind("<KeyRelease>", lambda event: update_data_size_label())


tk.Label(root, text="Select AES Key Size (128, 192, or 256 bits):", font=("Helvetica", 16), bg="#e6e6fa", fg="#4b0082").pack(pady=10)
aes_key_var = tk.StringVar(value="128")
aes_128_rb = tk.Radiobutton(root, text="128 bits", variable=aes_key_var, value="128", font=("Helvetica", 14), bg="#e6e6fa", fg="#4b0082", indicatoron=True)
aes_192_rb = tk.Radiobutton(root, text="192 bits", variable=aes_key_var, value="192", font=("Helvetica", 14), bg="#e6e6fa", fg="#4b0082", indicatoron=True)
aes_256_rb = tk.Radiobutton(root, text="256 bits", variable=aes_key_var, value="256", font=("Helvetica", 14), bg="#e6e6fa", fg="#4b0082", indicatoron=True)

aes_128_rb.pack()
aes_192_rb.pack()
aes_256_rb.pack()


tk.Label(root, text="Select RSA Key Size (1024, 2048, or 4096 bits):", font=("Helvetica", 16), bg="#e6e6fa", fg="#4b0082").pack(pady=10)
rsa_key_var = tk.StringVar(value="1024")
rsa_1024_rb = tk.Radiobutton(root, text="1024 bits", variable=rsa_key_var, value="1024", font=("Helvetica", 14), bg="#e6e6fa", fg="#4b0082", indicatoron=True)
rsa_2048_rb = tk.Radiobutton(root, text="2048 bits", variable=rsa_key_var, value="2048", font=("Helvetica", 14), bg="#e6e6fa", fg="#4b0082", indicatoron=True)
rsa_4096_rb = tk.Radiobutton(root, text="4096 bits", variable=rsa_key_var, value="4096", font=("Helvetica", 14), bg="#e6e6fa", fg="#4b0082", indicatoron=True)

rsa_1024_rb.pack()
rsa_2048_rb.pack()
rsa_4096_rb.pack()


start_button = tk.Button(root, text="Start Test", command=perform_test, font=("Helvetica", 16, "bold"), bg="#4caf50", fg="white", width=15)
start_button.pack(pady=30)

root.mainloop()
