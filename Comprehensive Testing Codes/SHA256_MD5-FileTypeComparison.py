import hashlib
import time
import os
import matplotlib.pyplot as plt

# Function to read file content
def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# Function to test hashing time for MD5 and SHA256
def test_hash_algorithms(file_data):
    # MD5 Hashing
    start_time = time.perf_counter()
    hashlib.md5(file_data).digest()
    md5_time = time.perf_counter() - start_time

    # SHA-256 Hashing
    start_time = time.perf_counter()
    hashlib.sha256(file_data).digest()
    sha256_time = time.perf_counter() - start_time

    return md5_time, sha256_time

# File paths (replace these with the actual file paths if different)
file_paths = {
    'sample.txt': r'D:\SLIIT\3Y 1S\IE3082-Cryptography\Assignment\sample.txt',
    'data.csv': r'D:\SLIIT\3Y 1S\IE3082-Cryptography\Assignment\data.csv',
    'config.json': r'D:\SLIIT\3Y 1S\IE3082-Cryptography\Assignment\config.json',
    'info.xml': r'D:\SLIIT\3Y 1S\IE3082-Cryptography\Assignment\info.xml'
}

# Initialize lists to store results
file_types = []
md5_times = []
sha256_times = []

# Read and test each file
for file_type, file_path in file_paths.items():
    # Read file content
    file_data = read_file(file_path)

    # Test hashing time
    md5_time, sha256_time = test_hash_algorithms(file_data)

    # Store results
    file_types.append(file_type)
    md5_times.append(md5_time)
    sha256_times.append(sha256_time)

# Plotting results
plt.figure(figsize=(10, 6))

bar_width = 0.35
index = range(len(file_types))

# MD5 Bars
plt.bar(index, md5_times, bar_width, color='blue', label='MD5')

# SHA-256 Bars
plt.bar([i + bar_width for i in index], sha256_times, bar_width, color='orange', label='SHA-256')

# Labels and titles
plt.xlabel('File Types')
plt.ylabel('Time (seconds)')
plt.title('Hashing Time Comparison (MD5 vs SHA-256)')
plt.xticks([i + bar_width / 2 for i in index], file_types)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
