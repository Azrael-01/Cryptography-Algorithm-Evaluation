import hashlib
import time
import matplotlib.pyplot as plt
from Crypto.Random import get_random_bytes

# Function to test MD5 and SHA-256 performance
def test_hash_algorithms(data):
    # MD5 Hashing
    start_time = time.perf_counter()
    md5_hash = hashlib.md5(data).digest()
    md5_time = time.perf_counter() - start_time

    # SHA-256 Hashing
    start_time = time.perf_counter()
    sha256_hash = hashlib.sha256(data).digest()
    sha256_time = time.perf_counter() - start_time

    return md5_time, sha256_time

# Test data sizes
data_sizes = [64, 512, 1024, 2048, 4096]  # In bytes

md5_times = []
sha256_times = []

# Iterate over different data sizes
for data_size in data_sizes:
    data = get_random_bytes(data_size)
    
    print(f"\nData Size: {data_size} bytes")
    
    # Run hash algorithm tests
    md5_time, sha256_time = test_hash_algorithms(data)
    md5_times.append(md5_time)
    sha256_times.append(sha256_time)

    print(f"MD5 Hashing Time: {md5_time:.10f}s")
    print(f"SHA-256 Hashing Time: {sha256_time:.10f}s")

# Plotting the results in a dual-graph format
fig, axs = plt.subplots(2, figsize=(12, 10))

# Top graph - MD5 Performance
axs[0].plot(data_sizes, md5_times, marker='o', label='MD5 Hash Time', color='blue')
axs[0].set_title('MD5 Hashing Performance for Different Data Sizes')
axs[0].set_xlabel('Data Size (bytes)')
axs[0].set_ylabel('Time (seconds)')
axs[0].grid(True)
axs[0].legend()

# Bottom graph - SHA-256 Performance
axs[1].plot(data_sizes, sha256_times, marker='o', label='SHA-256 Hash Time', color='orange')
axs[1].set_title('SHA-256 Hashing Performance for Different Data Sizes')
axs[1].set_xlabel('Data Size (bytes)')
axs[1].set_ylabel('Time (seconds)')
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()
