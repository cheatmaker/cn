def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1'
                   for i in range(1, len(b)))

def mod2div(data, key):
    tmp = data[:len(key)]
    for i in range(len(key), len(data) + 1):
        tmp = xor(key if tmp[0] == '1' else '0' * len(key), tmp)
        if i < len(data):
            tmp += data[i]
    return tmp

data = input("Enter data: ")
key = input("Enter generator: ")

crc = mod2div(data + '0' * (len(key) - 1), key)
sent = data + crc
print("Transmitted Data:", sent)

received = input("Enter received data: ") or sent
remainder = mod2div(received, key)
print("Remainder:", remainder)
print("Error Detected" if '1' in remainder else "No Error Detected")
