import numpy as np


def flood_fill(img, labels, y, x, label):
    """
    Flood fill manual para etiquetagem.
    """

    altura, largura = img.shape

    stack = [(y, x)]

    while stack:
        cy, cx = stack.pop()

        if cy < 0 or cy >= altura:
            continue

        if cx < 0 or cx >= largura:
            continue

        if img[cy, cx] == 0:
            continue

        if labels[cy, cx] != 0:
            continue

        labels[cy, cx] = label

        # 4-connectivity
        stack.append((cy - 1, cx))
        stack.append((cy + 1, cx))
        stack.append((cy, cx - 1))
        stack.append((cy, cx + 1))


def blob_count_manual(img_binary):
    """
    Etiquetagem manual de blobs.

    Parâmetros:
        img_binary -> imagem binária

    Retorna:
        labels -> imagem etiquetada
        total_labels -> número de blobs
    """

    altura, largura = img_binary.shape

    labels = np.zeros((altura, largura), dtype=np.int32)

    current_label = 0

    for y in range(altura):
        for x in range(largura):

            if img_binary[y, x] == 255 and labels[y, x] == 0:
                current_label += 1

                flood_fill(
                    img_binary,
                    labels,
                    y,
                    x,
                    current_label
                )

    return labels, current_label


def blob_properties_manual(labels, total_labels):
    """
    Calcula área e centro de massa
    de cada blob.

    Parâmetros:
        labels -> imagem etiquetada
        total_labels -> número de blobs

    Retorna:
        lista com:
        [
            {
                "label": 1,
                "area": ...,
                "centroid": (x, y)
            }
        ]
    """

    propriedades = []

    for label in range(1, total_labels + 1):

        area = 0
        soma_x = 0
        soma_y = 0

        altura, largura = labels.shape

        for y in range(altura):
            for x in range(largura):

                if labels[y, x] == label:
                    area += 1
                    soma_x += x
                    soma_y += y

        if area > 0:
            centroid_x = int(soma_x / area)
            centroid_y = int(soma_y / area)

            propriedades.append({
                "label": label,
                "area": area,
                "centroid": (centroid_x, centroid_y)
            })

    return propriedades


def colorize_labels(labels):
    """
    Converte a imagem de etiquetas numa imagem colorida.
    
    Cada blob tem uma cor diferente usando uma paleta vibrante.
    O fundo (label=0) aparece em branco.

    Parâmetros:
        labels -> imagem etiquetada (inteiros)

    Retorna:
        imagem RGB colorida com cores vibrantes
    """

    altura, largura = labels.shape

    # Inicializa com branco (fundo)
    img_colored = np.ones(
        (altura, largura, 3),
        dtype=np.uint8
    ) * 255

    total_labels = np.max(labels)

    # Paleta de cores MUITO vibrantes (RGB)
    cores_paleta = [
        (255, 0, 0),       # Vermelho puro
        (0, 255, 0),       # Verde puro
        (0, 0, 255),       # Azul puro
        (255, 255, 0),     # Amarelo puro
        (255, 0, 255),     # Magenta puro
        (0, 255, 255),     # Ciano puro
        (255, 128, 0),     # Laranja
        (128, 0, 255),     # Roxo escuro
        (255, 0, 128),     # Rosa quente
        (0, 255, 128),     # Verde-ciano
        (128, 255, 0),     # Lima brilhante
        (0, 128, 255),     # Azul-claro
        (255, 192, 0),     # Ouro
        (128, 0, 128),     # Roxo escuro
        (0, 128, 128),     # Azul-escuro
        (255, 64, 64),     # Vermelho-coral
        (64, 255, 64),     # Verde-brilhante
        (64, 64, 255),     # Azul-brilhante
    ]

    for label in range(1, total_labels + 1):
        # Seleciona cor da paleta (com repetição se necessário)
        cor_idx = (label - 1) % len(cores_paleta)
        cor = cores_paleta[cor_idx]

        mask = labels == label
        img_colored[mask] = cor

    return img_colored




