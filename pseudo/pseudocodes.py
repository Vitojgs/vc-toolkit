def pseudo_rgb_to_gray():
    return """
ALGORITMO: RGB para Tons de Cinzento

INÍCIO

Para cada pixel da imagem:

    Ler valor de R (Red)
    Ler valor de G (Green)
    Ler valor de B (Blue)

    Calcular:

        Gray = 0.299 × R
             + 0.587 × G
             + 0.114 × B

    Guardar o valor Gray
    na imagem de saída

Fim Para

Retornar imagem em tons de cinzento

FIM
"""


def pseudo_rgb_negative():
    return """
ALGORITMO: Negativo RGB

INÍCIO

Para cada pixel da imagem:

    Ler R
    Ler G
    Ler B

    Calcular:

        Novo_R = 255 - R
        Novo_G = 255 - G
        Novo_B = 255 - B

    Guardar os novos valores
    na imagem de saída

Fim Para

Retornar imagem negativa

FIM
"""

def pseudo_extract_rgb_channel():
    return """
ALGORITMO: Extração de Canal RGB

INÍCIO

Selecionar o canal desejado:
    Red, Green ou Blue

Para cada pixel da imagem:

    Ler o valor do canal selecionado

    Guardar esse valor
    na imagem de saída
    em tons de cinzento

Fim Para

Retornar imagem resultante

FIM
"""

def pseudo_rgb_to_hsv():
    return """
ALGORITMO: RGB para HSV

INÍCIO

Para cada pixel da imagem:

    Ler R, G, B

    Calcular:
        Max = maior valor entre R, G e B
        Min = menor valor entre R, G e B
        Delta = Max - Min

    Value = Max

    Se Max = 0:
        Saturation = 0
    Senão:
        Saturation = Delta / Max

    Calcular Hue
    conforme o maior canal:
        Red
        Green
        Blue

    Guardar H, S e V
    na imagem de saída

Fim Para

Retornar imagem HSV

FIM
"""


def pseudo_hsv_segmentation():
    return """
ALGORITMO: Segmentação HSV

INÍCIO

Receber:
    H mínimo e máximo
    S mínimo e máximo
    V mínimo e máximo

Para cada pixel da imagem HSV:

    Ler H, S e V

    Se:

        H dentro do intervalo
        E
        S dentro do intervalo
        E
        V dentro do intervalo

    Então:

        pixel = branco (255)

    Senão:

        pixel = preto (0)

Fim Para

Retornar máscara binária

FIM
"""


def pseudo_threshold_manual():
    return """
ALGORITMO: Threshold Manual

INÍCIO

Receber valor de threshold

Para cada pixel da imagem:

    Ler intensidade do pixel

    Se pixel >= threshold

        pixel = branco (255)

    Senão

        pixel = preto (0)

Fim Para

Retornar imagem binária

FIM
"""

def pseudo_threshold_global_mean():
    return """
ALGORITMO: Threshold por Média Global

INÍCIO

Somar todos os píxeis da imagem

Calcular:

    Threshold = Soma / Número total de píxeis

Para cada pixel da imagem:

    Se pixel >= Threshold

        pixel = branco (255)

    Senão

        pixel = preto (0)

Fim Para

Retornar:
    imagem binária
    valor do threshold

FIM
"""


def pseudo_dilation():
    return """
ALGORITMO: Dilatação

INÍCIO

Definir kernel (ex: 3x3)

Para cada pixel da imagem:

    Verificar todos os vizinhos
    dentro do kernel

    Se existir pelo menos
    um pixel branco (255)

        pixel de saída = branco

    Senão

        pixel de saída = preto

Fim Para

Retornar imagem dilatada

FIM
"""

def pseudo_erosion():
    return """
ALGORITMO: Erosão

INÍCIO

Definir kernel (ex: 3x3)

Para cada pixel da imagem:

    Verificar todos os vizinhos
    dentro do kernel

    Se TODOS os pixels forem brancos (255)

        pixel de saída = branco

    Senão

        pixel de saída = preto

Fim Para

Retornar imagem erodida

FIM
"""


def pseudo_opening():
    return """
ALGORITMO: Abertura (Opening)

INÍCIO

Aplicar Erosão

Aplicar Dilatação
sobre o resultado anterior

Retornar imagem final

FIM
"""


def pseudo_closing():
    return """
ALGORITMO: Fecho (Closing)

INÍCIO

Aplicar Dilatação

Aplicar Erosão
sobre o resultado anterior

Retornar imagem final

FIM
"""

def pseudo_mean_filter():
    return """
ALGORITMO: Filtro da Média

INÍCIO

Definir kernel (ex: 3x3)

Para cada pixel da imagem:

    Somar todos os pixels
    da vizinhança

    Calcular média:
        média = soma / número de pixels

    Substituir pixel central
    pela média

Fim Para

Retornar imagem filtrada

FIM
"""

def pseudo_median_filter():
    return """
ALGORITMO: Filtro da Mediana

INÍCIO

Definir kernel (ex: 3x3)

Para cada pixel da imagem:

    Recolher todos os pixels
    da vizinhança

    Ordenar os valores

    Escolher o valor central
    (mediana)

    Substituir pixel central
    pela mediana

Fim Para

Retornar imagem filtrada

FIM
"""


def pseudo_gaussian_filter():
    return """
ALGORITMO: Filtro Gaussiano

INÍCIO

Definir kernel gaussiano:

1 2 1
2 4 2
1 2 1

Para cada pixel da imagem:

    Multiplicar cada vizinho
    pelo respetivo peso

    Somar todos os valores

    Dividir pela soma dos pesos

    Substituir pixel central

Fim Para

Retornar imagem filtrada

FIM
"""

def pseudo_sobel():
    return """
ALGORITMO: Operador de Sobel

INÍCIO

Definir kernel horizontal (Gx)

Definir kernel vertical (Gy)

Para cada pixel da imagem:

    Aplicar convolução com Gx

    Aplicar convolução com Gy

    Calcular magnitude:

        Magnitude =
        sqrt(Gx² + Gy²)

    Guardar resultado

Fim Para

Retornar imagem de contornos

FIM
"""

def pseudo_prewitt():
    return """
ALGORITMO: Operador de Prewitt

INÍCIO

Definir kernel horizontal (Gx)

Definir kernel vertical (Gy)

Para cada pixel da imagem:

    Aplicar convolução com Gx

    Aplicar convolução com Gy

    Calcular magnitude:

        Magnitude =
        sqrt(Gx² + Gy²)

    Guardar resultado

Fim Para

Retornar imagem de contornos

FIM
"""


def pseudo_roberts():
    return """
ALGORITMO: Operador de Roberts

INÍCIO

Para cada pixel da imagem:

    Calcular gradiente diagonal:

        Gx = pixel atual
             - pixel diagonal

        Gy = pixel inferior
             - pixel lateral

    Calcular magnitude:

        Magnitude =
        sqrt(Gx² + Gy²)

    Guardar resultado

Fim Para

Retornar imagem de contornos

FIM
"""


def pseudo_laplacian():
    return """
ALGORITMO: Operador Laplaciano

INÍCIO

Definir kernel Laplaciano

Para cada pixel da imagem:

    Aplicar convolução
    com o kernel

    Calcular valor absoluto

    Guardar resultado

Fim Para

Retornar imagem de contornos

FIM
"""


def pseudo_histogram():
    return """
ALGORITMO: Histograma Gray

INÍCIO

Criar vetor de 256 posições
inicializado com zero

Para cada pixel da imagem:

    Ler intensidade do pixel

    Incrementar posição correspondente
    no vetor do histograma

Fim Para

Retornar histograma

FIM
"""


def pseudo_histogram_equalization():
    return """
ALGORITMO: Equalização de Histograma

INÍCIO

Calcular histograma

Calcular CDF
(função de distribuição acumulada)

Normalizar CDF

Criar tabela de conversão

Para cada pixel da imagem:

    Substituir intensidade
    pelo novo valor equalizado

Fim Para

Retornar imagem equalizada

FIM
"""


def pseudo_blob_labelling():
    return """
ALGORITMO: Blob Labelling

INÍCIO

Inicializar contador de labels = 0

Para cada pixel da imagem:

    Se pixel for branco
    e ainda não estiver etiquetado:

        incrementar label

        aplicar Flood Fill
        para marcar toda a região

Fim Para

Retornar:
    imagem etiquetada
    número total de blobs

FIM
"""



def pseudo_blob_properties():
    return """
ALGORITMO: Área e Centro de Massa

INÍCIO

Para cada blob etiquetado:

    Inicializar área = 0

    Somar coordenadas X e Y

    Para cada pixel:

        Se pixel pertence ao blob:

            área += 1

            soma_x += x
            soma_y += y

    Calcular:

        centro_x = soma_x / área
        centro_y = soma_y / área

Guardar resultados

Fim Para

Retornar propriedades

FIM
"""


def pseudo_fft():
    return """
ALGORITMO: FFT e Espectro

INÍCIO

Aplicar FFT 2D
na imagem

Centrar frequências baixas
no centro do espectro

Calcular magnitude:

    magnitude =
    log(|FFT|)

Normalizar valores

Retornar espectro

FIM
"""

def pseudo_low_pass_fft():
    return """
ALGORITMO: Filtro Passa-Baixo FFT

INÍCIO

Aplicar FFT

Centrar frequências

Criar máscara circular

Manter apenas
baixas frequências

Aplicar máscara

Aplicar FFT inversa

Normalizar imagem

Retornar imagem filtrada

FIM
"""


def pseudo_high_pass_fft():
    return """
ALGORITMO: Filtro Passa-Alto FFT

INÍCIO

Aplicar FFT

Centrar frequências

Criar máscara circular

Remover baixas frequências
(centro)

Manter altas frequências

Aplicar FFT inversa

Normalizar imagem

Retornar imagem filtrada

FIM
"""


