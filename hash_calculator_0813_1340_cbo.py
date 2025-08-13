# 代码生成时间: 2025-08-13 13:40:10
# hash_calculator.py
# A simple hash calculator tool using Python and hashlib library.

import hashlib
import sys

def calculate_hash(data, algorithm='sha256'):
    """
    Calculate the hash for the provided data using the specified algorithm.
    
    Args:
        data (str): The data to be hashed.
        algorithm (str): The hash algorithm to use. Defaults to 'sha256'.
    
    Returns:
        str: The hexadecimal representation of the hash.
# 添加错误处理
    
    Raises:
        ValueError: If the algorithm is not supported.
    """
    try:
        hash_object = getattr(hashlib, algorithm)(data.encode())
        return hash_object.hexdigest()
# FIXME: 处理边界情况
    except AttributeError:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

def main():
    """
    The main function that processes command line arguments and calculates the hash.
    """
    if len(sys.argv) < 3:
        print("Usage: python hash_calculator.py <algorithm> <data>")
        sys.exit(1)
    
    algorithm, *data_parts = sys.argv[1:]
    data = ' '.join(data_parts)
    try:
        hash_result = calculate_hash(data, algorithm)
        print(f"Hash ({algorithm}): {hash_result}")
    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()