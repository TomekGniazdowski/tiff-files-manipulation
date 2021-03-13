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


def allloop(data_hex_list, byte_order):

    width = -1
    length = -1
    header = int('0x0010', 16)
    hexrange = len(data_hex_list) - 20
    # lil endian
    if byte_order == 0:
        while(header < hexrange):
            if(int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x0100):
                width = image_width(data_hex_list, byte_order, header)
            if(int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x0101):
                length = image_length(data_hex_list, byte_order, header)
            header+=12
        print("Width is:", width)
        print("Length is:", length)

    elif byte_order == 1:
        while (header < hexrange):
            if (int(data_hex_list[header] + data_hex_list[header+1], 16) == 0x0100):
                width = image_width(data_hex_list, byte_order, header)
            if (int(data_hex_list[header] + data_hex_list[header+1], 16) == 0x0101):
                length = image_length(data_hex_list, byte_order, header)
            header += 12
        print("Width is:", width)
        print("Length is:", length)

def image_width(data_hex_list, byte_order, header):
    # width

    if byte_order == 0:
        return int(data_hex_list[header + 11] + data_hex_list[header+10] + data_hex_list[header+9] + data_hex_list[header+8], 16)

    elif byte_order == 1:
        return int(data_hex_list[header+8] + data_hex_list[header + 9] + data_hex_list[header + 10] +data_hex_list[header + 11], 16)
    else:
        return -1

def image_length(data_hex_list, byte_order, header):
    #length

    if byte_order == 0:
        return int(data_hex_list[header + 11] + data_hex_list[header+10] + data_hex_list[header+9] + data_hex_list[header+8], 16)

    elif byte_order == 1:
        return int(data_hex_list[header+8] + data_hex_list[header + 9] + data_hex_list[header + 10] +data_hex_list[header + 11], 16)

    else:
        return -1


