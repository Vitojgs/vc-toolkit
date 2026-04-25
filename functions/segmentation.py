import numpy as np


def threshold_manual(img_gray, threshold):
    """
    Binarização manual por threshold.

    Se pixel >= threshold:
        pixel = 255

    Senão:
        pixel = 0

    Parâmetros:
        img_gray -> imagem em tons de cinzento
        threshold -> valor do limiar

    Retorna:
        imagem binária
    """

    altura, largura = img_gray.shape

    img_binary = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):

            pixel = img_gray[y, x]

            if pixel >= threshold:
                img_binary[y, x] = 255
            else:
                img_binary[y, x] = 0

    return img_binary


def threshold_global_mean(img_gray):
    """
    Binarização automática usando
    threshold pela média global.

    T = média de todos os píxeis

    Parâmetros:
        img_gray -> imagem grayscale

    Retorna:
        imagem binária
        valor do threshold calculado
    """

    altura, largura = img_gray.shape

    soma = 0

    # Calcular soma manualmente
    for y in range(altura):
        for x in range(largura):
            soma += img_gray[y, x]

    total_pixels = altura * largura

    threshold = int(soma / total_pixels)

    # Aplicar threshold
    img_binary = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):

            if img_gray[y, x] >= threshold:
                img_binary[y, x] = 255
            else:
                img_binary[y, x] = 0

    return img_binary, threshold


