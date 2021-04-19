import numpy as np
import cv2 as cv

def fourier_transform(image_name):
    # odczyt obrazu
    img = cv.imread(image_name)
    # do skali szrosci
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_float32 = np.float32(img_gray)
    # transformacja fouriera
    dft = cv.dft(img_float32, flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    dft_real = dft_shift[:, :, 0]
    dft_imag = 1j * dft_shift[:, :, 1]
    dft_abs = np.abs(dft_real + dft_imag) + 1
    # 20log(A)
    dft_bounded = 20 * np.log(dft_abs)
    # faza
    dft_phase = np.angle((1j * dft_shift[:, :, 1]) / dft_shift[:, :, 0], deg=True)
    return dft_bounded, dft_phase