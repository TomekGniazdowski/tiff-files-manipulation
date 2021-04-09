import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def fourier_transform(image_name):
    img = cv.imread(image_name)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_float32 = np.float32(img_gray)
    # transformacja fouriera
    dft = cv.dft(img_float32, flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    # 20log(A)
    magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1)
    # phase_spectrum = np.angle(dft_shift)
    return magnitude_spectrum #, phase_spectrum