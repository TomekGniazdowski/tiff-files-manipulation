import tiff_manipulations as tf
import fourier as fr
import matplotlib.pyplot as plt
image = 'PIA24380.tif'

tiff_file = tf.Tiff_manipulations(image)
tiff_file.read_data()
tiff_file.list_data()
print(tiff_file.check_required_fields())


modul_widma, faza = fr.fourier_transform(image)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.imshow(modul_widma, cmap='gray')
ax2.imshow(faza, cmap='gray')
plt.show()


img = plt.imread(image)
plt.imshow(img)
plt.show()

print("\n\n*** Usuwamy metadane: ***\n\n")
tiff_file.read_data(mod=1)
tiff_file.list_data()

print("\n\n*** Po usunieciu: ***\n\n")
tiff_file.read_data()
tiff_file.list_data()
