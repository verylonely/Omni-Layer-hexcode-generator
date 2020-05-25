import binascii
print("Just generate hex code for Simple Send in Omni Layer")
omni = binascii.hexlify(b'omni').decode()
simple_send = '00000000'
token_id = hex(int(input('Token ID: ')))[2:]

amount = input("Amount: ")

amount = float(amount) * 100000000

amount = hex(int(amount))[2:]

def get_len(data):
    ctr = 0
    for i in data:
        ctr += 1
    return ctr

def get_nulls(min, data):
    nulls_len = min - get_len(str(data))
    nulls = ''
    for i in range(nulls_len):
        nulls += '0'
    return nulls

hex_data = omni + simple_send + get_nulls(8, token_id) + token_id + get_nulls(16, amount) + amount

if get_len(hex_data) != 40:
    print('ERROR: incorrect value')
else:

    print('Hex code:', hex_data)

