import numpy as np


def fft_spectrum_manual(img_gray):
    """
    Calcula o espectro de frequência
    usando FFT.

    Parâmetros:
        img_gray -> imagem grayscale

    Retorna:
        magnitude_spectrum
    """

    # FFT 2D
    f = np.fft.fft2(img_gray)

    # Centrar frequências baixas
    fshift = np.fft.fftshift(f)

    # Magnitude
    magnitude_spectrum = 20 * np.log(
        np.abs(fshift) + 1
    )

    # Normalização para visualização
    magnitude_spectrum = (
        magnitude_spectrum /
        np.max(magnitude_spectrum)
    ) * 255

    magnitude_spectrum = magnitude_spectrum.astype(
        np.uint8
    )

    return magnitude_spectrum


def low_pass_filter_fft(img_gray, radius=30):
    """
    Filtro passa-baixo no domínio
    da frequência.

    Parâmetros:
        img_gray -> imagem grayscale
        radius -> raio do filtro circular

    Retorna:
        imagem filtrada
    """

    rows, cols = img_gray.shape
    crow, ccol = rows // 2, cols // 2

    # FFT
    f = np.fft.fft2(img_gray)
    fshift = np.fft.fftshift(f)

    # Máscara circular
    mask = np.zeros((rows, cols), np.uint8)

    for y in range(rows):
        for x in range(cols):

            distance = np.sqrt(
                (y - crow) ** 2 +
                (x - ccol) ** 2
            )

            if distance <= radius:
                mask[y, x] = 1

    # Aplicar filtro
    fshift_filtered = fshift * mask

    # Transformada inversa
    f_ishift = np.fft.ifftshift(
        fshift_filtered
    )

    img_back = np.fft.ifft2(
        f_ishift
    )

    img_back = np.abs(
        img_back
    )

    # Normalização
    img_back = (
        img_back /
        np.max(img_back)
    ) * 255

    img_back = img_back.astype(
        np.uint8
    )

    return img_back


def high_pass_filter_fft(img_gray, radius=30):
    """
    Filtro passa-alto no domínio
    da frequência.

    Parâmetros:
        img_gray -> imagem grayscale
        radius -> raio da região removida

    Retorna:
        imagem filtrada
    """

    rows, cols = img_gray.shape
    crow, ccol = rows // 2, cols // 2

    # FFT
    f = np.fft.fft2(img_gray)
    fshift = np.fft.fftshift(f)

    # Máscara inicial = tudo 1
    mask = np.ones((rows, cols), np.uint8)

    for y in range(rows):
        for x in range(cols):

            distance = np.sqrt(
                (y - crow) ** 2 +
                (x - ccol) ** 2
            )

            if distance <= radius:
                mask[y, x] = 0

    # Aplicar filtro
    fshift_filtered = fshift * mask

    # FFT inversa
    f_ishift = np.fft.ifftshift(
        fshift_filtered
    )

    img_back = np.fft.ifft2(
        f_ishift
    )

    img_back = np.abs(
        img_back
    )

    # Normalização
    img_back = (
        img_back /
        np.max(img_back)
    ) * 255

    img_back = img_back.astype(
        np.uint8
    )

    return img_back




