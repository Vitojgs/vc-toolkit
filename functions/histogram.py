import numpy as np


def calculate_histogram_manual(img_gray):
    """
    Calcula manualmente o histograma
    de uma imagem grayscale.

    Retorna:
        vetor com 256 posições
        (0 a 255)
    """

    histogram = np.zeros(256, dtype=int)

    altura, largura = img_gray.shape

    for y in range(altura):
        for x in range(largura):

            pixel = img_gray[y, x]

            histogram[pixel] += 1

    return histogram


def histogram_equalization_manual(img_gray):
    """
    Equalização manual de histograma.

    Melhora o contraste da imagem
    redistribuindo as intensidades.

    Parâmetros:
        img_gray -> imagem grayscale

    Retorna:
        imagem equalizada
    """

    histogram = calculate_histogram_manual(img_gray)

    total_pixels = img_gray.shape[0] * img_gray.shape[1]

    # Função de distribuição acumulada (CDF)
    cdf = np.zeros(256, dtype=int)
    cdf[0] = histogram[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]

    # Normalização
    cdf_min = 0

    for value in cdf:
        if value != 0:
            cdf_min = value
            break

    lookup_table = np.zeros(256, dtype=np.uint8)

    for i in range(256):
        lookup_table[i] = int(
            ((cdf[i] - cdf_min) /
            (total_pixels - cdf_min)) * 255
        )

    # Aplicar nova intensidade
    altura, largura = img_gray.shape
    output = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):
            pixel = img_gray[y, x]
            output[y, x] = lookup_table[pixel]

    return output