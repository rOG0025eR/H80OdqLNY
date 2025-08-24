# 代码生成时间: 2025-08-24 22:22:36
import hashlib
import sys

class HashCalculator:
    """A simple hash calculator tool that takes input from the user
    and calculates various hash values.
    """

    def __init__(self):
# 改进用户体验
        pass

    def calculate_hash(self, input_string, hash_type='sha256'):
        """Calculates the hash of the given input string using the specified hash type.
# 扩展功能模块

        Args:
            input_string (str): The input string to calculate the hash for.
            hash_type (str): The type of hash to calculate (e.g., 'sha256', 'md5', 'sha1').
# FIXME: 处理边界情况

        Returns:
            str: The calculated hash value.
# 改进用户体验

        Raises:
            ValueError: If the hash type is not supported.
        """
        supported_hashes = {'sha256': hashlib.sha256, 'md5': hashlib.md5, 'sha1': hashlib.sha1}

        if hash_type not in supported_hashes:
            raise ValueError(f"Unsupported hash type: {hash_type}
# 增强安全性
Supported types: {[*supported_hashes.keys()]}
")

        # Create a new hash object using the specified type
        hash_obj = supported_hashes[hash_type]()

        # Update the hash object with the input string encoded to bytes
        hash_obj.update(input_string.encode('utf-8'))

        # Return the hexadecimal representation of the hash digest
        return hash_obj.hexdigest()

    def main(self):
# 增强安全性
        """The main method that takes input from the user and
        calculates the hash using the specified hash type.
        """
        try:
            # Prompt the user for input
            input_string = input("What would you like to hash? ")

            # Prompt the user for the hash type (default to 'sha256')
            hash_type = input("Enter hash type (default 'sha256'): ") or 'sha256'
# FIXME: 处理边界情况

            # Calculate the hash and print the result
# 改进用户体验
            hash_value = self.calculate_hash(input_string, hash_type)
            print(f"Hash ({hash_type}): {hash_value}
")

        except ValueError as ve:
            print(f"Error: {ve}
")

if __name__ == '__main__':
    # Create an instance of the HashCalculator and run the main method
    hash_calculator = HashCalculator()
    hash_calculator.main()