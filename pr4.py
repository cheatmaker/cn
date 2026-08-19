def xor(a, b):
    return ''.join(['0' if a[i] == b[i] else '1' for i in range(1, len(b))])


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        return xor(divisor, tmp)
    else:
        return xor('0' * pick, tmp)


print("--- CRC Sender Side ---")

data = input("Enter the binary data to send (e.g., 100100): ")
divisor = input("Enter the Generator Polynomial/Divisor (e.g., 1101): ")

# Append zeros to the data
appended_data = data + '0' * (len(divisor) - 1)

# Calculate CRC remainder
crc_remainder = mod2div(appended_data, divisor)

# Form transmitted data
transmitted_data = data + crc_remainder

print(f"\nAppended Data:      {appended_data}")
print(f"CRC Remainder:      {crc_remainder}")
print(f"Transmitted Data:   {transmitted_data}")

print("\n--- CRC Receiver Side ---")

received_data = input(
    f"Enter received data (Press Enter to use '{transmitted_data}'): "
) or transmitted_data

receiver_remainder = mod2div(received_data, divisor)

print(f"\nReceiver Remainder: {receiver_remainder}")

if '1' in receiver_remainder:
    print("Status: ERROR DETECTED! The data was corrupted.")
else:
    print("Status: SUCCESS! No error detected in transmission.")
