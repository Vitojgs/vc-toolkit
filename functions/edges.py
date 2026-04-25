import numpy as np


def sobel_manual(img_gray):
    """
    Operador de Sobel manual.

    Calcula gradientes horizontal e vertical
    e depois a magnitude do gradiente.

    Parâmetros:
        img_gray -> imagem em tons de cinzento

    Retorna:
        imagem de contornos
    """

    kernel_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    kernel_y = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]

    altura, largura = img_gray.shape

    output = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):

            gx = 0
            gy = 0

            for ky in range(-1, 2):
                for kx in range(-1, 2):

                    pixel = int(img_gray[y + ky, x + kx])

                    gx += pixel * kernel_x[ky + 1][kx + 1]
                    gy += pixel * kernel_y[ky + 1][kx + 1]

            magnitude = int(np.sqrt(gx**2 + gy**2))

            if magnitude > 255:
                magnitude = 255

            output[y, x] = magnitude

    return output

def prewitt_manual(img_gray):
    """
    Operador de Prewitt manual.

    Calcula gradientes horizontal e vertical
    e depois a magnitude.

    Parâmetros:
        img_gray -> imagem grayscale

    Retorna:
        imagem de contornos
    """

    kernel_x = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ]

    kernel_y = [
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ]

    altura, largura = img_gray.shape

    output = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):

            gx = 0
            gy = 0

            for ky in range(-1, 2):
                for kx in range(-1, 2):

                    pixel = int(img_gray[y + ky, x + kx])

                    gx += pixel * kernel_x[ky + 1][kx + 1]
                    gy += pixel * kernel_y[ky + 1][kx + 1]

            magnitude = int(np.sqrt(gx**2 + gy**2))

            if magnitude > 255:
                magnitude = 255

            output[y, x] = magnitude

    return output


def roberts_manual(img_gray):
    """
    Operador de Roberts manual.

    Usa gradientes diagonais
    com kernel 2x2.

    Parâmetros:
        img_gray -> imagem grayscale

    Retorna:
        imagem de contornos
    """

    altura, largura = img_gray.shape

    output = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(altura - 1):
        for x in range(largura - 1):

            gx = int(img_gray[y, x]) - int(img_gray[y + 1, x + 1])
            gy = int(img_gray[y + 1, x]) - int(img_gray[y, x + 1])

            magnitude = int(np.sqrt(gx**2 + gy**2))

            if magnitude > 255:
                magnitude = 255

            output[y, x] = magnitude

    return output


def laplacian_manual(img_gray):
    """
    Operador Laplaciano manual.

    Usa segunda derivada espacial
    para deteção de contornos.

    Kernel clássico:

        0  -1   0
       -1   4  -1
        0  -1   0

    Parâmetros:
        img_gray -> imagem grayscale

    Retorna:
        imagem de contornos
    """

    kernel = [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ]

    altura, largura = img_gray.shape

    output = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):

            soma = 0

            for ky in range(-1, 2):
                for kx in range(-1, 2):

                    pixel = int(img_gray[y + ky, x + kx])
                    peso = kernel[ky + 1][kx + 1]

                    soma += pixel * peso

            soma = abs(soma)

            if soma > 255:
                soma = 255

            output[y, x] = soma

    return output