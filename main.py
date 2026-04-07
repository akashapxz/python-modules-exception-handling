import file_utils
import math_operations

# File handling
print("Reading file:")
result = file_utils.read_file("sample.txt")
print(result)

# Math operations
print("\nDivision:")
print(math_operations.divide(10, 2))
print(math_operations.divide(10, 0))   # exception

print("\nSquare Root:")
print(math_operations.square_root(16))
print(math_operations.square_root(-4))  # exception