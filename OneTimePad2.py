

def xor_ciphers(c1, c2):
    # XOR the corresponding bytes of the ciphers
    xor_result = bytes([b1 ^ b2 for b1, b2 in zip(c1, c2)])

    return xor_result


def check_possible_numbers(xor_ciphers):
    my_list = []
    for x in range(len(xor_ciphers)):
        count = 0
        x_bytes = xor_ciphers[x]
        for i in range(9):
            for j in range(i, 9):
                if x_bytes == i ^ j:
                    count += 1
                    my_list.append({"digit": x + 1, "case": count, "value 1" : i, "value 2": j })
    return my_list


def bits_to_bytes(bits):
    # Ensure the length of bits is a multiple of 8 by adding leading zeros if needed
    while len(bits) % 8 != 0:
        bits = '0' + bits

    # Convert the binary string to an integer
    decimal_value = int(bits, 2)

    # Calculate the number of bytes required
    num_bytes = (len(bits) + 7) // 8

    # Convert the integer to bytes
    byte_representation = decimal_value.to_bytes(num_bytes, byteorder='big')

    return byte_representation

def combine_three_cipher(com1, com2):
    common_values = []
    for dictionary1 in com1:
        for dictionary2 in com2:
            if (dictionary1.get("digit") == dictionary2.get("digit")) and (dictionary1.get("value 1") == dictionary2.get("value 1") or dictionary1.get("value 1") == dictionary2.get("value 2")
                or dictionary1.get("value 2") == dictionary2.get("value 1") or dictionary1.get("value 2") == dictionary2.get("value 2")): 
                                                            

                    common_values.append({"digit": dictionary1.get("digit"), "value 1": dictionary1.get("value 1"), "value 2": dictionary2.get("value 1"), "value 3": dictionary1.get("value 2"), "value 4": dictionary2.get("value 2")})
        # Iterate over key-value pairs in the dictionary


    return common_values



def print_bytes(byte_sequence):
    for b in byte_sequence:
        binary_representation = format(b, '08b')
        print(binary_representation, end=" ")
    print("\n------------")


# Example usage
# key = 0100111000101010100100101101111001000001000001011001011000011010100011000001100100100011
# number3 = "5781"
# n3 = "00110101001101110011100000110001"
# cipher3 = "01111011000111011010101011101111"

number1 = "332"
number2 = "658"

n1 = "001100110011001100110010"
n2 = "001101100011010100111000"


cipher1 = "011111010001100110100000"
cipher2 = "011110000001111110101010"

c1 = bits_to_bytes(cipher1)
c2 = bits_to_bytes(cipher2)

print("Binary Representation Cipher 1: ")
print_bytes(c1)
print("Binary Representation Cipher 2: ")
print_bytes(c2)

xor_ciphers_1_2 = xor_ciphers(c1, c2)
print("Binary Representation xor Ciphers 1 and 2: ")
print_bytes(xor_ciphers_1_2)

list_of_dicts_1_2 = check_possible_numbers(xor_ciphers_1_2)

print("Combination of 1 and 2: ")
for dictionary in list_of_dicts_1_2:
    # Iterate over key-value pairs in the dictionary
    for key, value in dictionary.items():
        print(f"{key}: {value}")

    # Separate dictionaries with a line
    print("------")


print("\n")
