def add_binary_strings(s1, s2):
    # Convert binary strings to integers
    num1 = int(s1, 2)
    num2 = int(s2, 2)
    
    # Add the integers
    total = num1 + num2
    
    # Convert the sum back to a binary string and remove the '0b' prefix
    result = bin(total)[2:]
    
    # Remove leading zeros
    result = result.lstrip('0')
    
    # If the result is an empty string, it means the result is 0
    if not result:
        result = '0'
    
    return result

# Example usage
s1 = "00101"
s2 = "00011"
print(add_binary_strings(s1, s2))  # Output: "1000"