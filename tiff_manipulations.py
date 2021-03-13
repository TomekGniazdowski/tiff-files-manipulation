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
    photometric_value = -1
    rel_unit = -1
    xres = -1
    header = int('0x0010', 16)
    hexrange = len(data_hex_list) - 12
    # lil endian
    if byte_order == 0:
        while header < hexrange:
            if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x0100:
                width = image_width(data_hex_list, byte_order, header)
            if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x0101:
                length = image_length(data_hex_list, byte_order, header)
            if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x0106:
                photometric_value = photometric(data_hex_list, byte_order, header)
            if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x0128:
                rel_unit = resolution_unit(data_hex_list, byte_order, header)
        #    if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x011A:
        #        xres = xresolution(data_hex_list, byte_order, header)
            header += 12
        print("Width is:", width)
        print("Length is:", length)
        print("Photometric Interpretation is:", photometric_value)
        print("Resolution unit is:", rel_unit)
        print("XResolution is:", xres)
    # biggie endian
    elif byte_order == 1:
        while header < hexrange:
            if int(data_hex_list[header] + data_hex_list[header+1], 16) == 0x0100:
                width = image_width(data_hex_list, byte_order, header)
            if int(data_hex_list[header] + data_hex_list[header+1], 16) == 0x0101:
                length = image_length(data_hex_list, byte_order, header)
            if int(data_hex_list[header] + data_hex_list[header+1], 16) == 0x0106:
                photometric_value = photometric(data_hex_list, byte_order, header)
            if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x0128:
                rel_unit = resolution_unit(data_hex_list, byte_order, header)
         #   if int(data_hex_list[header + 1] + data_hex_list[header], 16) == 0x011A:
         #       xres = xresolution(data_hex_list, byte_order, header)
            header += 12
        print("Width is:", width)
        print("Length is:", length)
        print("Photometric Interpretation is:", photometric_value)
        print("Resolution unit is:", rel_unit)
        print("XResolution is:", xres)

def check_type(data_hex_list, byte_order, header):

    if byte_order == 0:
        type_of_var = int(data_hex_list[header + 3] + data_hex_list[header+2] , 16)
    elif byte_order == 1:
        type_of_var = int(data_hex_list[header+2] + data_hex_list[header + 3], 16)
    else:
        type_of_var = -1

    return type_of_var


def proper_type_place(data_hex_list, byte_order, header):
    chunk_type = check_type(data_hex_list, byte_order, header)
    if byte_order == 0:
        if chunk_type == 0x0001 or chunk_type == 0x0002:
            return int(data_hex_list[header + 8], 16)
        if chunk_type == 0x0003:
            return int(data_hex_list[header+9] + data_hex_list[header+8], 16)
        if chunk_type == 0x0004:
            return int(data_hex_list[header + 11] + data_hex_list[header+10] + data_hex_list[header+9] + data_hex_list[header+8], 16)
      #  if chunk_type == 0x0005:
      #      header_copy = int(data_hex_list[header + 11] + data_hex_list[header+10], 16)
      #      return (int(data_hex_list[header_copy + 5] + data_hex_list[header_copy+4] + data_hex_list[header_copy+3] + data_hex_list[header+2], 16),int(data_hex_list[header_copy + 9] + data_hex_list[header_copy+8] + data_hex_list[header_copy+7] + data_hex_list[header+6], 16))
        else:
            return -1

    elif byte_order == 1:
        if chunk_type == 0x0001 or chunk_type == 0x0002:
            return int(data_hex_list[header + 8], 16)
        if chunk_type == 0x0003:
            return int(data_hex_list[header+8] + data_hex_list[header+9], 16)
        if chunk_type == 0x0004:
            return int(data_hex_list[header + 8] + data_hex_list[header+9] + data_hex_list[header+10] + data_hex_list[header+11], 16)
      #  if chunk_type == 0x0005:
      #      header_copy = int(data_hex_list[header+10] + data_hex_list[header+11], 16)
      #      return (int(data_hex_list[header_copy + 2] + data_hex_list[header_copy+3] + data_hex_list[header_copy+4] + data_hex_list[header+5], 16),int(data_hex_list[header_copy + 6] + data_hex_list[header_copy+7] + data_hex_list[header_copy+8] + data_hex_list[header+9], 16))
        else:
            return -1
    else:
        return -1


def image_width(data_hex_list, byte_order, header):
    # width
    return proper_type_place(data_hex_list, byte_order, header)


def image_length(data_hex_list, byte_order, header):
    # length
    return proper_type_place(data_hex_list, byte_order, header)


def photometric(data_hex_list, byte_order, header):

    return proper_type_place(data_hex_list, byte_order, header)


def resolution_unit(data_hex_list, byte_order, header):

    return proper_type_place(data_hex_list, byte_order, header)


def xresolution(data_hex_list, byte_order, header):

    return proper_type_place(data_hex_list, byte_order, header)
