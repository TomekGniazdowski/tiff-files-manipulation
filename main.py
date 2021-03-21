import tiff_manipulations as tf
import cv2 as cv
import matplotlib.pyplot as plt
image = 'kilka_pikseli.tif'

tiff_file = tf.Tiff_manipulations(image)
tiff_file.read_data()
tiff_file.list_data()
print(tiff_file.check_required_fields())

img = plt.imread(image)
plt.imshow(img)
plt.show()