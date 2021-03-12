def read_return_hex(file_name):
    # open file, read data as bytes
    file = open(file_name, "rb")
    data = file.read()
    file.close()
    data_hex = data.hex()
    return data_hex


def str_to_hexlist(s):
    data_hex_list = []
    for i in range(len(s)):
        if i % 2 == 0 and i != 0:
            data_hex_list.append(s[i - 2:i])
    return data_hex_list


def return_byte_order(data_hex_list):
    header = int('0x0000', 16)
    # little-endian
    if int(data_hex_list[header] + data_hex_list[header + 1], 16) == 0x4949:
        return 0
    # big-endian
    elif int(data_hex_list[header] + data_hex_list[header + 1], 16) == 0x4d4d:
        return 1
    # error
    else:
        return -1


# 0 - litte, 1 - big (endian)
def is_file_tiff(data_hex_list, byte_order):
    header = int('0x0002', 16)
    if byte_order == 0:
        if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x002A:
            return True
        else:
            return False

    if byte_order == 1:
        if int(data_hex_list[header] + data_hex_list[header + 1], 16) == 0x002A:
            return True
        else:
            return False


# ****************************na razie zle
def image_dim(data_hex_list, byte_order):
    # width
    header_width = 0x0022
    if byte_order == 0:
        width = int(data_hex_list[header_width + 1] + data_hex_list[header_width], 16)

    elif byte_order == 1:
        width = int(data_hex_list[header_width] + data_hex_list[header_width + 1], 16)

    else:
        width = -1

    # length
    header_length = 0x002E
    if byte_order == 0:
        length = int(data_hex_list[header_length + 1] + data_hex_list[header_length], 16)

    elif byte_order == 1:
        length = int(data_hex_list[header_length] + data_hex_list[header_length + 1], 16)

    else:
        length = -1

    return (width, length)



