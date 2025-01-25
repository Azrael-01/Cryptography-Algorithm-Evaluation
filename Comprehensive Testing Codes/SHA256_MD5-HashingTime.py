import hashlib
import time
import psutil
import os
import matplotlib.pyplot as plt
from Crypto.Random import get_random_bytes

# Function to test MD5 and SHA-256 performance including CPU and memory usage
def test_hash_algorithms(data):
    process = psutil.Process(os.getpid())  # Monitor current process

    # Initial CPU and memory usage
    initial_cpu = process.cpu_percent(interval=None)
    initial_memory = process.memory_info().rss

    # MD5 Hashing
    start_time = time.perf_counter()
    hashlib.md5(data).digest()
    md5_time = time.perf_counter() - start_time
    md5_cpu = process.cpu_percent(interval=None) - initial_cpu
    md5_memory = process.memory_info().rss - initial_memory

    # SHA-256 Hashing
    initial_cpu = process.cpu_percent(interval=None)
    initial_memory = process.memory_info().rss

    start_time = time.perf_counter()
    hashlib.sha256(data).digest()
    sha256_time = time.perf_counter() - start_time
    sha256_cpu = process.cpu_percent(interval=None) - initial_cpu
    sha256_memory = process.memory_info().rss - initial_memory

    return (md5_time, md5_cpu, md5_memory), (sha256_time, sha256_cpu, sha256_memory)

# Test data size (adjustable)
data_size = 4096  # 4 KB of random data
data = get_random_bytes(data_size)

# Run hash algorithm tests
(md5_time, md5_cpu, md5_memory), (sha256_time, sha256_cpu, sha256_memory) = test_hash_algorithms(data)

# Data for bar chart
algorithms = ['MD5', 'SHA-256']
times = [md5_time, sha256_time]
cpu_usages = [md5_cpu, sha256_cpu]
memory_usages = [md5_memory, sha256_memory]

# Plotting bar chart comparison for Hashing Time
plt.figure(figsize=(10, 8))

# Subplot 1: Hashing Time
plt.subplot(3, 1, 1)
plt.bar(algorithms, times, color=['blue', 'orange'])
plt.title(f'Hashing Time Comparison (Data Size: {data_size} bytes)')
plt.ylabel('Time (seconds)')
plt.grid(True, axis='y')

# Subplot 2: CPU Usage
plt.subplot(3, 1, 2)
plt.bar(algorithms, cpu_usages, color=['blue', 'orange'])
plt.title('CPU Usage Comparison')
plt.ylabel('CPU Usage (%)')
plt.grid(True, axis='y')

# Subplot 3: Memory Usage
plt.subplot(3, 1, 3)
plt.bar(algorithms, memory_usages, color=['blue', 'orange'])
plt.title('Memory Usage Comparison')
plt.ylabel('Memory Usage (Bytes)')
plt.grid(True, axis='y')

# Show the plot
plt.tight_layout()
plt.show()
