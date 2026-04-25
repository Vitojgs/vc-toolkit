import numpy as np


def mean_filter_manual(img, kernel_size=3):
    """
    Filtro da média (passa-baixo).

    Cada pixel é substituído pela média
    dos vizinhos dentro do kernel.

    Parâmetros:
        img -> imagem (gray ou RGB)
        kernel_size -> tamanho do kernel (ímpar)

    Retorna:
        imagem filtrada
    """

    altura, largura = img.shape[:2]

    # Verifica se é RGB
    is_rgb = len(img.shape) == 3

    if is_rgb:
        output = np.zeros((altura, largura, 3), dtype=np.uint8)
    else:
        output = np.zeros((altura, largura), dtype=np.uint8)

    offset = kernel_size // 2

    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):

            if is_rgb:
                soma = [0, 0, 0]
            else:
                soma = 0

            count = 0

            for ky in range(-offset, offset + 1):
                for kx in range(-offset, offset + 1):

                    if is_rgb:
                        for c in range(3):
                            soma[c] += img[y + ky, x + kx, c]
                    else:
                        soma += img[y + ky, x + kx]

                    count += 1

            if is_rgb:
                for c in range(3):
                    output[y, x, c] = int(soma[c] / count)
            else:
                output[y, x] = int(soma / count)

    return output


def median_filter_manual(img, kernel_size=3):
    """
    Filtro da mediana.

    Cada pixel é substituído pela mediana
    dos pixels vizinhos.

    Excelente para remover
    ruído sal e pimenta.

    Parâmetros:
        img -> imagem gray ou RGB
        kernel_size -> tamanho do kernel

    Retorna:
        imagem filtrada
    """

    altura, largura = img.shape[:2]

    is_rgb = len(img.shape) == 3

    if is_rgb:
        output = np.zeros((altura, largura, 3), dtype=np.uint8)
    else:
        output = np.zeros((altura, largura), dtype=np.uint8)

    offset = kernel_size // 2

    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):

            if is_rgb:

                for c in range(3):
                    vizinhos = []

                    for ky in range(-offset, offset + 1):
                        for kx in range(-offset, offset + 1):
                            valor = img[y + ky, x + kx, c]
                            vizinhos.append(valor)

                    vizinhos.sort()
                    mediana = vizinhos[len(vizinhos) // 2]

                    output[y, x, c] = mediana

            else:
                vizinhos = []

                for ky in range(-offset, offset + 1):
                    for kx in range(-offset, offset + 1):
                        valor = img[y + ky, x + kx]
                        vizinhos.append(valor)

                vizinhos.sort()
                mediana = vizinhos[len(vizinhos) // 2]

                output[y, x] = mediana

    return output


def gaussian_filter_manual(img):
    """
    Filtro Gaussiano manual
    usando kernel clássico 3x3:

    1 2 1
    2 4 2
    1 2 1

    Soma = 16

    Parâmetros:
        img -> imagem gray ou RGB

    Retorna:
        imagem filtrada
    """

    kernel = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]

    divisor = 16

    altura, largura = img.shape[:2]
    is_rgb = len(img.shape) == 3

    if is_rgb:
        output = np.zeros((altura, largura, 3), dtype=np.uint8)
    else:
        output = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):

            if is_rgb:

                for c in range(3):
                    soma = 0

                    for ky in range(-1, 2):
                        for kx in range(-1, 2):
                            pixel = img[y + ky, x + kx, c]
                            peso = kernel[ky + 1][kx + 1]
                            soma += pixel * peso

                    output[y, x, c] = int(soma / divisor)

            else:
                soma = 0

                for ky in range(-1, 2):
                    for kx in range(-1, 2):
                        pixel = img[y + ky, x + kx]
                        peso = kernel[ky + 1][kx + 1]
                        soma += pixel * peso

                output[y, x] = int(soma / divisor)

    return output