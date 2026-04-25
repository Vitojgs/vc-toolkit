import numpy as np


def dilation_manual(img_binary, kernel_size=3):
    """
    Dilatação manual de imagem binária.

    A dilatação expande os objetos brancos.

    Parâmetros:
        img_binary -> imagem binária
        kernel_size -> tamanho do kernel (ímpar)

    Retorna:
        imagem dilatada
    """

    altura, largura = img_binary.shape

    output = np.zeros((altura, largura), dtype=np.uint8)

    offset = kernel_size // 2

    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):

            found_white = False

            for ky in range(-offset, offset + 1):
                for kx in range(-offset, offset + 1):

                    if img_binary[y + ky, x + kx] == 255:
                        found_white = True

            if found_white:
                output[y, x] = 255
            else:
                output[y, x] = 0

    return output

def erosion_manual(img_binary, kernel_size=3):
    """
    Erosão manual de imagem binária.

    A erosão reduz os objetos brancos.

    Parâmetros:
        img_binary -> imagem binária
        kernel_size -> tamanho do kernel (ímpar)

    Retorna:
        imagem erodida
    """

    altura, largura = img_binary.shape

    output = np.zeros((altura, largura), dtype=np.uint8)

    offset = kernel_size // 2

    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):

            all_white = True

            for ky in range(-offset, offset + 1):
                for kx in range(-offset, offset + 1):

                    if img_binary[y + ky, x + kx] == 0:
                        all_white = False

            if all_white:
                output[y, x] = 255
            else:
                output[y, x] = 0

    return output


def opening_manual(img_binary, kernel_size=3):
    """
    Abertura morfológica.

    Opening = Erosão + Dilatação

    Primeiro reduz ruídos pequenos
    e depois recompõe o objeto principal.

    Parâmetros:
        img_binary -> imagem binária
        kernel_size -> tamanho do kernel

    Retorna:
        imagem processada
    """

    img_eroded = erosion_manual(
        img_binary,
        kernel_size
    )

    img_opened = dilation_manual(
        img_eroded,
        kernel_size
    )

    return img_opened


def closing_manual(img_binary, kernel_size=3):
    """
    Fecho morfológico.

    Closing = Dilatação + Erosão

    Primeiro expande e depois reduz,
    preenchendo pequenas falhas internas.

    Parâmetros:
        img_binary -> imagem binária
        kernel_size -> tamanho do kernel

    Retorna:
        imagem processada
    """

    img_dilated = dilation_manual(
        img_binary,
        kernel_size
    )

    img_closed = erosion_manual(
        img_dilated,
        kernel_size
    )

    return img_closed