import tiff_manipulations as tf

data = tf.read_return_hex('nasa.tif')
hex_data_list = tf.str_to_hexlist(data)

#print(hex_data_list)

# 0 - little, 1 - big
byte_order = tf.return_byte_order(hex_data_list)
print('Byte order:', byte_order)

# najpierw trzeba sprawdzic czy small czy big, a potem dalej
# check if 0x0002 value is 42
is_file_tiff = tf.is_file_tiff(hex_data_list, byte_order)
print('Is file a tiff:', is_file_tiff)


# image dimensions
dim = tf.image_dim(hex_data_list, byte_order)
print('Image dimensions:', dim)