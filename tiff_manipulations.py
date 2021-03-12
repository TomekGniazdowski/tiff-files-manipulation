def read_return_hex(file_name):
    # open file, read data as bytes
    file = open(file_name, "rb")
    data = file.read()
    file.close()
    data_hex = data.hex()
    return data_hex


def return_byte_order(data_hex):
    # little-endian
    if data_hex[:4] == '4949':
        return 'II'
    # big-endian
    elif data_hex[:4] == '4D4D':
        return 'MM'
    # error
    else:
        return -1
