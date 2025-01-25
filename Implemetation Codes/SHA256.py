import hashlib
import time

# Function to hash data using SHA-256
def sha256_hash(data):
    sha256_signature = hashlib.sha256(data.encode()).hexdigest()
    return sha256_signature

# Function to hash user input using SHA-256
def hash_user_data_sha256():
    # Ask for user input
    data = input("Enter the data you want to hash using SHA-256: ")

    # Hash the data and measure the performance
    start_time = time.time()
    hash_result = sha256_hash(data)
    end_time = time.time()

    # Output the SHA-256 hash and time taken
    print(f"\nSHA-256 Hash: {hash_result}")
    print(f"Time taken to hash: {end_time - start_time:.10f} seconds\n")

# Main execution
if __name__ == "__main__":
    hash_user_data_sha256()
