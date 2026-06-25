# The obfuscated decimal ASCII sequence
ascii_string = "104,116,116,112,115,58,47,47,114,101,97,108,108,121,115,101,99,117,114,101,117,112,100,97,116,101,46,116,114,121,104,97,116,109,101,46,99,111,109,47,117,112,100,97,116,101,46,101,120,101"

# Split the string by commas and convert each piece to an integer
decimal_values = [int(x) for x in ascii_string.split(",")]

# Convert each integer back to its ASCII character character and join them together
decoded_text = "".join(chr(num) for num in decimal_values)

# Print the decoded output
print(f"Decoded String: {decoded_text}")