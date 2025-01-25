import hashlib
import time

# Function to hash data using MD5
def md5_hash(data):
    md5_signature = hashlib.md5(data.encode()).hexdigest()
    return md5_signature

# Function to hash user input using MD5
def hash_user_data_md5():
    # Ask for user input
    data = input("Enter the data you want to hash using MD5: ")

    # Hash the data and measure the performance
    start_time = time.time()
    hash_result = md5_hash(data)
    end_time = time.time()

    # Output the MD5 hash and time taken
    print(f"\nMD5 Hash: {hash_result}")
    print(f"Time taken to hash: {end_time - start_time:.10f} seconds\n")

# Main execution
if __name__ == "__main__":
    hash_user_data_md5()
