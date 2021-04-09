import tiff_manipulations as tf
import fourier as fr
import cv2 as cv
import matplotlib.pyplot as plt
image = 'nasa.tif'

tiff_file = tf.Tiff_manipulations(image)
tiff_file.read_data()
tiff_file.list_data()
print(tiff_file.check_required_fields())

modul_widma = fr.fourier_transform(image)
ax1 = plt.subplot(1,1,1)
ax1.imshow(modul_widma, cmap='gray')

plt.show()
img = plt.imread(image)
plt.imshow(img)
plt.show()

print("\n\n Usuwamy metadane: \n\n")
tiff_file.read_data(mod=1)
tiff_file.list_data()
