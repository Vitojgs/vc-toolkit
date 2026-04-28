import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2


# Import das funções
from functions.color import (
    rgb_to_gray_manual,
    rgb_negative_manual,
    extract_rgb_channel_manual,
    rgb_to_hsv_manual,
    hsv_segmentation_manual
)

from functions.segmentation import (
    threshold_manual,
    threshold_global_mean
)

from functions.morphology import (
    dilation_manual,
    erosion_manual,
    opening_manual,
    closing_manual
)

from functions.filters import (
    mean_filter_manual,
    median_filter_manual,
    gaussian_filter_manual
)

from functions.edges import (
    sobel_manual,
    prewitt_manual,
    roberts_manual,
    laplacian_manual
)

from functions.histogram import (
    calculate_histogram_manual,
    histogram_equalization_manual
)

from functions.blobs import (
    blob_count_manual,
    blob_properties_manual,
    colorize_labels
)

from functions.fourier import (
    fft_spectrum_manual,
    low_pass_filter_fft,
    high_pass_filter_fft
)

from utils.helpers import (
    convert_numpy_to_downloadable_image
)

from utils.study_guide import (
    show_study_guide
)

from pseudo.pseudocodes import *


from utils.image_loader import (
    load_sample_images,
    load_selected_sample
)

# Configuração da página
st.set_page_config(
    page_title="VC Toolkit",
    layout="wide"
)

# Título principal
st.title("VC Toolkit - Visão por Computador")
st.write("Projeto académico para teste e estudo de algoritmos de Visão por Computador")

# -------------------------------------------------
# MENU LATERAL
# -------------------------------------------------

st.sidebar.title("Guia de Estudo")

guia_estudo = st.sidebar.selectbox(
    "Escolha um tema para revisão:",
    [
        "Nenhum",
        "Espaços de Cor",
        "Segmentação",
        "Morfologia",
        "Filtros",
        "Contornos",
        "Histogramas",
        "Blobs",
        "Fourier"
    ]
)

st.sidebar.title("Menu de Operações")

categoria = st.sidebar.selectbox(
    "Escolha a categoria:",
    [
        "Espaços de Cor",
        "Segmentação",
        "Morfologia",
        "Filtros",
        "Contornos",
        "Histogramas",
        "Blobs",
        "Fourier"
    ]
)

# Mostrar guia de estudo
if guia_estudo != "Nenhum":
    show_study_guide(guia_estudo)
    st.divider()
    
image = None
img_array = None
is_rgb = False
    
st.sidebar.title("Imagens de Exemplo")

sample_images = load_sample_images()

selected_sample = st.sidebar.selectbox(
    "Escolha uma imagem de exemplo:",
    ["Nenhuma"] + sample_images
)    

# -------------------------------------------------
# Upload da imagem
# -------------------------------------------------

if selected_sample != "Nenhuma":

    image, img_array, is_rgb = load_selected_sample(
        selected_sample
    )

else:
    uploaded_file = st.file_uploader(
        "Faça upload da imagem",
        type=["ppm", "pgm", "pbm", "jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        is_rgb = len(img_array.shape) == 3

# -----------------------------
# Só continua se existir imagem
# -----------------------------

if img_array is not None:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Imagem Original")

        st.image(
            image,
            use_container_width=True
        )

        st.write(f"Dimensões: {img_array.shape}")

        if is_rgb:
            st.write("Formato: RGB")
        else:
            st.write("Formato: Tons de Cinzento")
            
            
    # Informações básicas da imagem
    st.write(f"**Dimensões:** {img_array.shape}")
    if is_rgb:
        st.write("**Formato:** RGB")
    else:
        st.write("**Formato:** Tons de Cinzento")

# =====================================================
# 1. ESPAÇOS DE COR
    # =====================================================
    if categoria == "Espaços de Cor":
        
        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "RGB para Gray",
                "Negativo RGB",
                "Extrair Canal RGB",
                "RGB para HSV",
                "Segmentação HSV"
            ]
        )

        # ---------------------------------
        # RGB para Gray
        # ---------------------------------
        if operacao == "RGB para Gray":

            if is_rgb:

                img_manual = rgb_to_gray_manual(
                    img_array
                )

                comparar_opencv = st.checkbox(
                    "Comparar com OpenCV?"
                )

                if comparar_opencv:

                    img_opencv = cv2.cvtColor(
                        img_array,
                        cv2.COLOR_RGB2GRAY
                    )

                    difference = cv2.absdiff(
                        img_manual,
                        img_opencv
                    )

                    st.write("### Comparação Manual vs OpenCV")

                    col_a, col_b, col_c = st.columns(3)

                    with col_a:
                        st.image(
                            img_manual,
                            use_container_width=True,
                            caption="Implementação Manual"
                        )

                    with col_b:
                        st.image(
                            img_opencv,
                            use_container_width=True,
                            caption="OpenCV"
                        )

                    with col_c:
                        st.image(
                            difference,
                            use_container_width=True,
                            caption="Diferença"
                        )

                else:

                    st.write("### Resultado")

                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Conversão Manual RGB para Gray"
                    )

                    image_bytes = convert_numpy_to_downloadable_image(
                        img_manual
                    )

                    st.download_button(
                        label="Download da Imagem Processada",
                        data=image_bytes,
                        file_name="rgb_to_gray.png",
                        mime="image/png"
                    )

                    st.write("### Explicação Teórica")

                    st.write("""
    A conversão de RGB para tons de cinzento não deve ser feita por média simples.

    É utilizada uma média ponderada porque o olho humano percebe
    mais intensamente a componente verde, seguida da vermelha
    e por fim a azul.

    Fórmula utilizada:

    Gray = 0.299 × R + 0.587 × G + 0.114 × B
                """)

                    st.write("### Pseudocódigo")

                    st.code(
                        pseudo_rgb_to_gray(),
                        language="text"
                    )

            else:
                st.warning("A imagem já está em tons de cinzento.")

        # ---------------------------------
        # Negativo RGB
        # ---------------------------------
        elif operacao == "Negativo RGB":

            if is_rgb:

                img_result = rgb_negative_manual(img_array)

                st.write("### Imagem Original")
                st.image(image, use_container_width=True)

                st.write("### Resultado")
                st.image(
                    img_result,
                    use_container_width=True,
                    caption="Negativo Manual RGB"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_result
                )

                st.download_button(
                    label="Download da Imagem Processada",
                    data=image_bytes,
                    file_name="rgb_negative.png",
                    mime="image/png"
                )

                st.write("### Explicação Teórica")

                st.write("""
    O negativo de uma imagem é calculado invertendo os valores
    de intensidade de cada canal RGB.

    Cada valor é transformado segundo:

    Novo Valor = 255 - Valor Atual

    Isto produz a cor oposta no espaço RGB.
    Por exemplo:

    Preto → Branco  
    Vermelho → Ciano  
    Azul → Amarelo
                """)

                st.write("### Pseudocódigo")

                st.code(
                    pseudo_rgb_negative(),
                    language="text"
                )

            else:
                st.warning("Esta operação necessita de uma imagem RGB.")


    # ---------------------------------
    # Extrair Canal RGB
    # ---------------------------------
        elif operacao == "Extrair Canal RGB":

            if is_rgb:

                canal = st.sidebar.selectbox(
                    "Escolha o canal:",
                    [
                        "Vermelho",
                        "Verde",
                        "Azul"
                    ]
                )

                if canal == "Vermelho":
                    channel_index = 0

                elif canal == "Verde":
                    channel_index = 1

                else:
                    channel_index = 2

                img_result = extract_rgb_channel_manual(
                    img_array,
                    channel_index
                )

                st.write("### Imagem Original")
                st.image(image, use_container_width=True)

                st.write("### Resultado")
                st.image(
                    img_result,
                    use_container_width=True,
                    caption=f"Canal Extraído: {canal}"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_result
                )

                st.download_button(
                    label="Download da Imagem Processada",
                    data=image_bytes,
                    file_name=f"canal_{canal.lower()}.png",
                    mime="image/png"
                )

                st.write("### Explicação Teórica")

                st.write("""
    Uma imagem RGB é composta por três canais:

    R → Red (Vermelho)  
    G → Green (Verde)  
    B → Blue (Azul)

    Cada canal representa a intensidade dessa cor.

    Ao extrair apenas um canal, obtemos uma imagem em tons
    de cinzento onde cada pixel representa apenas a intensidade
    da componente selecionada.
                """)

                st.write("### Pseudocódigo")

                st.code(
                    pseudo_extract_rgb_channel(),
                    language="text"
                )

            else:
                st.warning("Esta operação necessita de uma imagem RGB.")


    # ---------------------------------
    # RGB para HSV
    # ---------------------------------
        elif operacao == "RGB para HSV":

            if is_rgb:

                img_hsv = rgb_to_hsv_manual(img_array)

                h_channel = img_hsv[:, :, 0]
                s_channel = img_hsv[:, :, 1]
                v_channel = img_hsv[:, :, 2]

                st.write("### Imagem Original")
                st.image(image, use_container_width=True)

                st.write("### Resultado")
                col_h, col_s, col_v = st.columns(3)

                with col_h:
                    st.image(
                        h_channel,
                        use_container_width=True,
                        caption="Canal H (Hue)"
                    )

                with col_s:
                    st.image(
                        s_channel,
                        use_container_width=True,
                        caption="Canal S (Saturation)"
                    )

                with col_v:
                    st.image(
                        v_channel,
                        use_container_width=True,
                        caption="Canal V (Value)"
                    )

                st.write("### Explicação Teórica")

                st.write("""
    O espaço de cor HSV separa a informação de cor da informação
     de intensidade luminosa.

    H → Hue (Matiz / Cor)

    S → Saturation (Saturação)

    V → Value (Brilho / Intensidade)

    Ao contrário do RGB, o HSV facilita bastante a segmentação
     de objetos por cor, sendo muito utilizado em Visão por Computador.
                """)

                st.write("### Pseudocódigo")

                st.code(
                    pseudo_rgb_to_hsv(),
                    language="text"
                )

            else:
                st.warning("Esta operação necessita de uma imagem RGB.")


    # ---------------------------------
    # Segmentação HSV
    # ---------------------------------
        elif operacao == "Segmentação HSV":

            if is_rgb:

                st.sidebar.write("### Ajuste dos Intervalos HSV")

                h_min = st.sidebar.slider("H mínimo", 0, 179, 0)
                h_max = st.sidebar.slider("H máximo", 0, 179, 179)

                s_min = st.sidebar.slider("S mínimo", 0, 255, 50)
                s_max = st.sidebar.slider("S máximo", 0, 255, 255)

                v_min = st.sidebar.slider("V mínimo", 0, 255, 50)
                v_max = st.sidebar.slider("V máximo", 0, 255, 255)

                img_hsv = rgb_to_hsv_manual(img_array)

                img_result = hsv_segmentation_manual(
                    img_hsv,
                    h_min, h_max,
                    s_min, s_max,
                    v_min, v_max
                )

                st.write("### Imagem Original")
                st.image(image, use_container_width=True)

                st.write("### Resultado")
                st.image(
                    img_result,
                    use_container_width=True,
                    caption="Máscara Binária da Segmentação HSV"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_result
                )

                st.download_button(
                    label="Download da Imagem Processada",
                    data=image_bytes,
                    file_name="hsv_segmentation.png",
                    mime="image/png"
                )

                st.write("### Explicação Teórica")

                st.write("""
            A segmentação HSV permite isolar objetos com base na sua cor.

            Em vez de trabalhar diretamente em RGB, convertemos a imagem
            para HSV, onde a cor (Hue) fica separada da intensidade luminosa.

            Definindo intervalos mínimos e máximos para:

            H → Matiz  
            S → Saturação  
            V → Valor

            podemos criar uma máscara binária para segmentar objetos.
                    """)

                st.write("### Pseudocódigo")

                st.code(
                    pseudo_hsv_segmentation(),
                    language="text"
                )


    # =====================================================
    # 2. SEGMENTAÇÃO
    # =====================================================
    elif categoria == "Segmentação":

        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "Threshold Manual",
                "Threshold por Média Global"
            ]
        )

        # ---------------------------------
        # Threshold Manual
        # ---------------------------------
        if operacao == "Threshold Manual":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            threshold_value = st.sidebar.slider(
                "Valor do Threshold",
                0,
                255,
                128
            )

            img_manual = threshold_manual(
                img_gray,
                threshold_value
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                _, img_opencv = cv2.threshold(
                    img_gray,
                    threshold_value,
                    255,
                    cv2.THRESH_BINARY
                )

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption="Imagem Binária"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="threshold_manual.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    A binarização por threshold (limiarização) permite separar
    objetos do fundo com base na intensidade luminosa.

    Cada pixel é comparado com um valor limite chamado threshold.

    Se:

    pixel >= threshold

    então o pixel torna-se branco (255)

    caso contrário:

    o pixel torna-se preto (0)

    O resultado é uma imagem binária.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_threshold_manual(),
                language="text"
            )


        # ---------------------------------
        # Threshold por Média Global
        # ---------------------------------
        elif operacao == "Threshold por Média Global":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            img_result, threshold_value = threshold_global_mean(
                img_gray
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Threshold Calculado")
            st.success(f"Threshold automático calculado: {threshold_value}")

            st.write("### Resultado")
            st.image(
                img_result,
                use_container_width=True,
                caption="Imagem Binária por Média Global"
            )

            image_bytes = convert_numpy_to_downloadable_image(
                img_result
            )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="threshold_global_mean.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    Neste método, o threshold não é definido manualmente.

    O valor do limiar é calculado automaticamente através
    da média de intensidade de todos os píxeis da imagem.

    Fórmula:

    Threshold = soma de todos os píxeis / total de píxeis

    Depois disso, a imagem é binarizada normalmente.

    Este método é conhecido como threshold global.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_threshold_global_mean(),
                language="text"
            )           


    # =====================================================
    # 3. MORFOLOGIA
    # =====================================================
    elif categoria == "Morfologia":

        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "Dilatação",
                "Erosão",
                "Abertura",
                "Fecho"
            ]
        )

        # ---------------------------------
        # Dilatação
        # ---------------------------------
        if operacao == "Dilatação":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            # Primeiro binarizamos
            threshold_value = st.sidebar.slider(
                "Threshold para binarização",
                0,
                255,
                128
            )

            img_binary = threshold_manual(
                img_gray,
                threshold_value
            )

            # Kernel
            kernel_size = st.sidebar.slider(
                "Tamanho do Kernel",
                3,
                11,
                3,
                step=2
            )

            img_manual = dilation_manual(
                img_binary,
                kernel_size
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                # Criar kernel para OpenCV
                kernel = cv2.getStructuringElement(
                    cv2.MORPH_ELLIPSE,
                    (kernel_size, kernel_size)
                )

                img_opencv = cv2.dilate(
                    img_binary,
                    kernel,
                    iterations=1
                )

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption=f"Dilatação com Kernel {kernel_size}x{kernel_size}"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="dilation.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    A dilatação é uma operação morfológica que expande
    os objetos brancos de uma imagem binária.

    É utilizada para:

    - aumentar objetos
    - preencher pequenas falhas
    - unir regiões próximas
    - reforçar blobs

    A dilatação verifica a vizinhança de cada pixel
    através de um kernel.
    Se existir pelo menos um pixel branco nessa região,
    o pixel central torna-se branco.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_dilation(),
                language="text"
            )    

        # ---------------------------------
        # Erosão
        # ---------------------------------
        elif operacao == "Erosão":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            # Primeiro binarizamos
            threshold_value = st.sidebar.slider(
                "Threshold para binarização",
                0,
                255,
                128
            )

            img_binary = threshold_manual(
                img_gray,
                threshold_value
            )

            # Kernel
            kernel_size = st.sidebar.slider(
                "Tamanho do Kernel",
                3,
                11,
                3,
                step=2
            )

            img_manual = erosion_manual(
                img_binary,
                kernel_size
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                # Criar kernel para OpenCV
                kernel = cv2.getStructuringElement(
                    cv2.MORPH_ELLIPSE,
                    (kernel_size, kernel_size)
                )

                img_opencv = cv2.erode(
                    img_binary,
                    kernel,
                    iterations=1
                )

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption=f"Erosão com Kernel {kernel_size}x{kernel_size}"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="erosion.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    A erosão é uma operação morfológica que reduz
    os objetos brancos de uma imagem binária.

    É utilizada para:

    - remover pequenos ruídos
    - separar objetos ligados
    - reduzir blobs
    - limpar pequenas regiões

    A erosão verifica a vizinhança de cada pixel
    através de um kernel.

    Se TODOS os pixels da vizinhança forem brancos,
    o pixel central permanece branco.

    Caso contrário, torna-se preto.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_erosion(),
                language="text"
            )

        # ---------------------------------
        # Abertura
        # ---------------------------------
        elif operacao == "Abertura":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            # Binarização inicial
            threshold_value = st.sidebar.slider(
                "Threshold para binarização",
                0,
                255,
                128
            )

            img_binary = threshold_manual(
                img_gray,
                threshold_value
            )

            # Kernel
            kernel_size = st.sidebar.slider(
                "Tamanho do Kernel",
                3,
                11,
                3,
                step=2
            )

            img_manual = opening_manual(
                img_binary,
                kernel_size
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                # Criar kernel para OpenCV
                kernel = cv2.getStructuringElement(
                    cv2.MORPH_ELLIPSE,
                    (kernel_size, kernel_size)
                )

                img_opencv = cv2.morphologyEx(
                    img_binary,
                    cv2.MORPH_OPEN,
                    kernel,
                    iterations=1
                )

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption=f"Abertura com Kernel {kernel_size}x{kernel_size}"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="opening.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    A abertura (Opening) é uma operação morfológica composta por:

    Erosão + Dilatação

    nesta ordem.

    É utilizada para:

    - remover pequenos ruídos brancos
    - eliminar pequenas regiões isoladas
    - limpar objetos
    - preservar melhor a forma principal

    Primeiro a erosão remove pequenas regiões,
    depois a dilatação recompõe o objeto principal.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_opening(),
                language="text"
            )

        # ---------------------------------
        # Fecho
        # ---------------------------------
        elif operacao == "Fecho":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            # Binarização inicial
            threshold_value = st.sidebar.slider(
                "Threshold para binarização",
                0,
                255,
                128
            )

            img_binary = threshold_manual(
                img_gray,
                threshold_value
            )

            # Kernel
            kernel_size = st.sidebar.slider(
                "Tamanho do Kernel",
                3,
                11,
                3,
                step=2
            )

            img_manual = closing_manual(
                img_binary,
                kernel_size
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                # Criar kernel para OpenCV
                kernel = cv2.getStructuringElement(
                    cv2.MORPH_ELLIPSE,
                    (kernel_size, kernel_size)
                )

                img_opencv = cv2.morphologyEx(
                    img_binary,
                    cv2.MORPH_CLOSE,
                    kernel,
                    iterations=1
                )

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption=f"Fecho com Kernel {kernel_size}x{kernel_size}"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="closing.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O fecho (Closing) é uma operação morfológica composta por:

    Dilatação + Erosão

    nesta ordem.

    É utilizada para:

    - fechar pequenos buracos internos
    - preencher falhas dentro dos objetos
    - unir pequenas interrupções
    - suavizar contornos internos

    Primeiro a dilatação expande o objeto,
    depois a erosão ajusta novamente a sua forma.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_closing(),
                language="text"
            )        
    # =====================================================
    # 4. FILTROS ESPACIAIS
    # =====================================================
    elif categoria == "Filtros":

        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "Filtro da Média",
                "Filtro da Mediana",
                "Filtro Gaussiano"
            ]
        )


        # ---------------------------------
        # Filtro da Média
        # ---------------------------------
        if operacao == "Filtro da Média":

            kernel_size = st.sidebar.slider(
                "Tamanho do Kernel",
                3,
                11,
                3,
                step=2
            )

            img_result = mean_filter_manual(
                img_array,
                kernel_size
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Resultado")
            st.image(
                img_result,
                use_container_width=True,
                caption=f"Filtro da Média ({kernel_size}x{kernel_size})"
            )

            image_bytes = convert_numpy_to_downloadable_image(
                img_result
            )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="mean_filter.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O filtro da média é um filtro passa-baixo utilizado
    para suavizar imagens.

    Cada pixel é substituído pela média dos pixels vizinhos
    dentro de um kernel.

    É utilizado para:

    - reduzir ruído
    - suavizar contornos
    - remover detalhes pequenos
    - desfocar a imagem

    Quanto maior o kernel,
    maior será o efeito de suavização.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_mean_filter(),
                language="text"
            )

        # ---------------------------------
        # Filtro da Mediana
        # ---------------------------------
        elif operacao == "Filtro da Mediana":

            kernel_size = st.sidebar.slider(
                "Tamanho do Kernel",
                3,
                11,
                3,
                step=2
            )

            img_result = median_filter_manual(
                img_array,
                kernel_size
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Resultado")
            st.image(
                img_result,
                use_container_width=True,
                caption=f"Filtro da Mediana ({kernel_size}x{kernel_size})"
            )

            image_bytes = convert_numpy_to_downloadable_image(
                img_result
            )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="median_filter.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O filtro da mediana é um filtro passa-baixo
    muito eficaz para remover ruído sal e pimenta.

    Ao contrário do filtro da média:

    - preserva melhor os contornos
    - remove melhor ruído impulsivo
    - evita desfocagem excessiva

    Cada pixel é substituído pela mediana
    dos pixels vizinhos dentro do kernel.

    A mediana corresponde ao valor central
    após ordenar os pixels da vizinhança.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_median_filter(),
                language="text"
            )


        # ---------------------------------
        # Filtro Gaussiano
        # ---------------------------------
        elif operacao == "Filtro Gaussiano":

            img_manual = gaussian_filter_manual(
                img_array
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                img_opencv = cv2.GaussianBlur(
                    img_array,
                    (3, 3),
                    0
                )

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption="Filtro Gaussiano (Kernel 3x3)"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="gaussian_filter.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O filtro Gaussiano é um filtro passa-baixo
    utilizado para suavização de imagens.

    Ao contrário do filtro da média,
    ele atribui maior peso aos pixels centrais
    e menor peso aos pixels mais afastados.

    Isso produz:

    - suavização mais natural
    - menos distorção
    - melhor preservação estrutural

    É muito utilizado antes de:

    - deteção de contornos
    - segmentação
    - processamento avançado
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_gaussian_filter(),
                language="text"
            )    

    # =====================================================
    # 5. CONTORNOS
    # =====================================================
    elif categoria == "Contornos":

        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "Sobel",
                "Prewitt",
                "Roberts",
                "Laplaciano"
            ]
        )

        # ---------------------------------
        # Sobel
        # ---------------------------------
        if operacao == "Sobel":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            img_manual = sobel_manual(
                img_gray
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                # Cálculo de Sobel com OpenCV
                sobelx = cv2.Sobel(img_gray, cv2.CV_32F, 1, 0, ksize=3)
                sobely = cv2.Sobel(img_gray, cv2.CV_32F, 0, 1, ksize=3)
                
                # Calcular magnitude
                img_opencv = np.sqrt(sobelx**2 + sobely**2)
                img_opencv = np.clip(img_opencv, 0, 255).astype(np.uint8)

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption="Deteção de Contornos - Sobel"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="sobel.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O operador de Sobel é utilizado para deteção
    de contornos e variações bruscas de intensidade.

    Ele calcula:

    - gradiente horizontal (Gx)
    - gradiente vertical (Gy)

    e depois combina ambos para obter
    a magnitude do gradiente.

    Fórmula:

    Magnitude = sqrt(Gx² + Gy²)

    Quanto maior a magnitude,
    mais forte é o contorno detectado.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_sobel(),
                language="text"
            )


        # ---------------------------------
        # Prewitt
        # ---------------------------------
        elif operacao == "Prewitt":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            img_manual = prewitt_manual(
                img_gray
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                # Cálculo de Prewitt com OpenCV (usando filtro customizado)
                kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
                kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
                
                prewittx = cv2.filter2D(img_gray.astype(np.float32), -1, kernelx)
                prewitty = cv2.filter2D(img_gray.astype(np.float32), -1, kernely)
                
                img_opencv = np.sqrt(prewittx**2 + prewitty**2)
                img_opencv = np.clip(img_opencv, 0, 255).astype(np.uint8)

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption="Deteção de Contornos - Prewitt"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="prewitt.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O operador de Prewitt é utilizado para deteção
    de contornos através do cálculo de gradientes.

    Tal como o Sobel, calcula:

    - gradiente horizontal (Gx)
    - gradiente vertical (Gy)

    e depois combina ambos.

    A principal diferença é que Prewitt utiliza
    kernels mais simples e uniformes.

    Fórmula:

    Magnitude = sqrt(Gx² + Gy²)

    É muito utilizado para comparação académica
    com o operador de Sobel.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_prewitt(),
                language="text"
            )


        # ---------------------------------
        # Roberts
        # ---------------------------------
        elif operacao == "Roberts":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            img_manual = roberts_manual(
                img_gray
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                # Cálculo de Roberts com OpenCV (usando kernels Roberts)
                kernelx = np.array([[1, 0], [0, -1]], dtype=np.float32)
                kernely = np.array([[0, 1], [-1, 0]], dtype=np.float32)
                
                robertsx = cv2.filter2D(img_gray.astype(np.float32), -1, kernelx)
                robertsy = cv2.filter2D(img_gray.astype(np.float32), -1, kernely)
                
                img_opencv = np.sqrt(robertsx**2 + robertsy**2)
                img_opencv = np.clip(img_opencv, 0, 255).astype(np.uint8)

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption="Deteção de Contornos - Roberts"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="roberts.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O operador de Roberts é um dos métodos mais antigos
    de deteção de contornos.

    Ao contrário de Sobel e Prewitt,
    utiliza um kernel 2x2 e calcula
    gradientes diagonais.

    Isso permite:

    - deteção rápida
    - menor complexidade
    - boa sensibilidade a contornos diagonais

    Fórmula:

    Magnitude = sqrt(Gx² + Gy²)

    É muito utilizado para comparação académica
    com outros operadores de edge detection.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_roberts(),
                language="text"
            )    


        # ---------------------------------
        # Laplaciano
        # ---------------------------------
        elif operacao == "Laplaciano":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            img_manual = laplacian_manual(
                img_gray
            )

            comparar_opencv = st.checkbox(
                "Comparar com OpenCV?"
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            if comparar_opencv:

                img_opencv = cv2.Laplacian(
                    img_gray,
                    cv2.CV_32F
                )

                img_opencv = np.clip(
                    np.abs(img_opencv),
                    0,
                    255
                ).astype(np.uint8)

                difference = cv2.absdiff(
                    img_manual,
                    img_opencv
                )

                st.write("### Comparação Manual vs OpenCV")

                col_a, col_b, col_c = st.columns(3)

                with col_a:
                    st.image(
                        img_manual,
                        use_container_width=True,
                        caption="Implementação Manual"
                    )

                with col_b:
                    st.image(
                        img_opencv,
                        use_container_width=True,
                        caption="OpenCV"
                    )

                with col_c:
                    st.image(
                        difference,
                        use_container_width=True,
                        caption="Diferença (Preto = Idêntico)"
                    )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            else:

                st.write("### Resultado")
                st.image(
                    img_manual,
                    use_container_width=True,
                    caption="Deteção de Contornos - Laplaciano"
                )

                image_bytes = convert_numpy_to_downloadable_image(
                    img_manual
                )

            st.download_button(
                label="Download da Imagem Processada",
                data=image_bytes,
                file_name="laplacian.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    O operador Laplaciano é utilizado para deteção
    de contornos através da segunda derivada espacial.

    Ao contrário de:

    - Sobel
    - Prewitt
    - Roberts

    que utilizam primeira derivada (gradiente),

    o Laplaciano utiliza segunda derivada.

    Isso permite:

    - deteção mais sensível
    - realce de mudanças bruscas
    - forte destaque de contornos

    É muito utilizado em comparação académica
    com operadores baseados em gradiente.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_laplacian(),
                language="text"
            )    


    # =====================================================
    # 6. HISTOGRAMAS
    # =====================================================
    elif categoria == "Histogramas":

        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "Histograma Gray"
            ]
        )

        # ---------------------------------
        # Histograma Gray
        # ---------------------------------
        if operacao == "Histograma Gray":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            histogram = calculate_histogram_manual(
                img_gray
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Resultado")

            st.image(
                img_gray,
                use_container_width=True,
                caption="Imagem em Tons de Cinzento"
            )

            st.write("### Gráfico do Histograma")

            fig, ax = plt.subplots()

            ax.bar(
                range(256),
                histogram
            )

            ax.set_xlabel("Intensidade")
            ax.set_ylabel("Quantidade de Pixels")
            ax.set_title("Histograma Gray")

            st.pyplot(fig)

            st.write("### Explicação Teórica")

            st.write("""
    O histograma representa a distribuição
    das intensidades dos pixels de uma imagem.

    No caso grayscale:

    - 0 → preto
    - 255 → branco

    O histograma permite analisar:

    - contraste
    - brilho
    - distribuição tonal
    - qualidade para segmentação

    É uma ferramenta fundamental
    em Visão por Computador.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_histogram(),
                language="text"
            )


        # ---------------------------------
        # Equalização de Histograma
        # ---------------------------------
        elif operacao == "Equalização de Histograma":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            img_result = histogram_equalization_manual(
                img_gray
            )

            hist_original = calculate_histogram_manual(
                img_gray
            )

            hist_equalized = calculate_histogram_manual(
                img_result
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Resultado")

            col_a, col_b = st.columns(2)

            with col_a:
                st.image(
                    img_gray,
                    use_container_width=True,
                    caption="Imagem Original"
                )

            with col_b:
                st.image(
                    img_result,
                    use_container_width=True,
                    caption="Imagem Equalizada"
                )

            image_bytes = convert_numpy_to_downloadable_image(
               img_result
            )

            st.download_button(
                label="Download da Imagem Equalizada",
                data=image_bytes,
                file_name="histograma_equalizado.png",
                mime="image/png"
            )

            st.write("### Comparação dos Histogramas")

            fig1, ax1 = plt.subplots()

            ax1.bar(
                range(256),
                hist_original
            )

            ax1.set_title("Histograma Original")
            ax1.set_xlabel("Intensidade")
            ax1.set_ylabel("Pixels")

            st.pyplot(fig1)

            fig2, ax2 = plt.subplots()

            ax2.bar(
                range(256),
                hist_equalized
            )

            ax2.set_title("Histograma Equalizado")
            ax2.set_xlabel("Intensidade")
            ax2.set_ylabel("Pixels")

            st.pyplot(fig2)

            st.write("### Explicação Teórica")

            st.write("""
    A equalização de histograma melhora o contraste
    da imagem redistribuindo as intensidades dos pixels.

    É especialmente útil quando a imagem apresenta:

    - pouco contraste
    - tons muito concentrados
    - regiões escuras ou claras excessivas

    A técnica utiliza:

    - histograma
    - CDF (distribuição acumulada)
    - normalização

    para criar uma nova distribuição tonal.
        """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_histogram_equalization(),
                language="text"
            )        



    # =====================================================
    # 7. BLOBS
    # =====================================================
    elif categoria == "Blobs":

        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "Blob Labelling",
                "Área e Centro de Massa"
            ]
        )

        # ---------------------------------
        # Blob Labelling
        # ---------------------------------
        if operacao == "Blob Labelling":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            # Threshold inicial
            threshold_value = st.sidebar.slider(
                "Threshold para binarização",
                0,
                255,
                128
            )

            img_binary = threshold_manual(
                img_gray,
                threshold_value
            )

            labels, total_blobs = blob_count_manual(
                img_binary
            )

            # Normalizar labels para visualização
            if total_blobs > 0:
                img_labels = (
                    labels.astype(np.float32) / total_blobs
                ) * 255
                img_labels = img_labels.astype(np.uint8)
            else:
                img_labels = labels.astype(np.uint8)

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Número de Blobs Detectados")

            st.success(f"Total de blobs encontrados: {total_blobs}")

            st.write("### Resultado")

            col_a, col_b = st.columns(2)

            with col_a:
                st.image(
                    img_binary,
                    use_container_width=True,
                    caption="Imagem Binária"
                )

            with col_b:
                st.image(
                    img_labels,
                    use_container_width=True,
                    caption="Imagem Etiquetada"
                )

            st.write("### Explicação Teórica")

            st.write("""
    Blob Labelling (Connected Components)
    permite identificar objetos separados
    numa imagem binária.

    Cada região branca conectada recebe
    uma etiqueta (label) diferente.

    Isto permite:

    - contar objetos
    - separar regiões
    - calcular área
    - calcular perímetro
    - calcular centro de massa

    É uma das técnicas mais importantes
    de segmentação.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_blob_labelling(),
                language="text"
            )

        # ---------------------------------
        # Área e Centro de Massa
        # ---------------------------------
        elif operacao == "Área e Centro de Massa":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            # Threshold inicial
            threshold_value = st.sidebar.slider(
                "Threshold para binarização",
                0,
                255,
                128
            )

            img_binary = threshold_manual(
                img_gray,
                threshold_value
            )

            labels, total_blobs = blob_count_manual(
                img_binary
            )

            propriedades = blob_properties_manual(
                labels,
                total_blobs
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Resultado")

            col_bin, col_labeled = st.columns(2)

            with col_bin:
                st.image(
                    img_binary,
                    use_container_width=True,
                    caption="Imagem Binária"
                )

            with col_labeled:
                img_labeled_colored = colorize_labels(labels)
                st.image(
                    img_labeled_colored,
                    use_container_width=True,
                    caption="Imagem Etiquetada (Colorida)"
                )

            st.write("### Propriedades dos Blobs")

            if len(propriedades) > 0:

                st.success(f"✓ Total de blobs encontrados: {len(propriedades)}")

                # Criar tabela com as propriedades
                blob_data = []
                for blob in propriedades:
                    blob_data.append({
                        "Blob ID": blob['label'],
                        "Área (pixels)": blob['area'],
                        "Centro X": blob['centroid'][0],
                        "Centro Y": blob['centroid'][1]
                    })

                st.table(blob_data)

                # Mostrar detalhes de cada blob
                st.write("**Detalhes de cada Blob:**")
                
                for i, blob in enumerate(propriedades, 1):
                    with st.expander(f"🔍 Blob {blob['label']} - Área: {blob['area']} pixels"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.metric("Área", f"{blob['area']} pixels")
                        
                        with col2:
                            st.metric("Centro de Massa", f"({blob['centroid'][0]}, {blob['centroid'][1]})")

            else:
                st.warning("Nenhum blob encontrado. Tente ajustar o threshold para detectar objetos.")

            st.write("### Explicação Teórica")

            st.write("""
    Depois da etiquetagem dos blobs,
    podemos calcular propriedades importantes
    de cada objeto.

    As principais são:

    Área:
    número total de pixels do blob

    Centro de Massa:
    posição média do objeto na imagem

    Estas métricas são muito utilizadas em:

    - inspeção visual
    - reconhecimento de objetos
    - controlo de qualidade
    - visão industrial
        """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_blob_properties(),
                language="text"
            )


    # =====================================================
    # 8. FOURIER
    # =====================================================
    elif categoria == "Fourier":

        operacao = st.sidebar.radio(
            "Escolha a função:",
            [
                "FFT e Espectro"
            ]
        )

        # ---------------------------------
        # FFT e Espectro
        # ---------------------------------
        if operacao == "FFT e Espectro":

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            img_result = fft_spectrum_manual(
                img_gray
            )

            st.write("### Imagem Original")
            st.image(image, use_container_width=True)

            st.write("### Resultado")

            col_a, col_b = st.columns(2)

            with col_a:
                st.image(
                    img_gray,
                    use_container_width=True,
                    caption="Imagem em Tons de Cinzento"
                )

            with col_b:
                st.image(
                    img_result,
                    use_container_width=True,
                    caption="Espectro de Frequências (FFT)"
                )
            image_bytes = convert_numpy_to_downloadable_image(
                img_result
            )

            st.download_button(
                label="Download do Espectro FFT",
                data=image_bytes,
                file_name="fft_spectrum.png",
                mime="image/png"
            )

            st.write("### Explicação Teórica")

            st.write("""
    A Transformada de Fourier permite analisar
    a imagem no domínio da frequência.

    Em vez de observar pixels diretamente,
    analisamos:

    - frequências baixas
    - frequências altas

    Baixas frequências representam:

    - áreas suaves
    - regiões homogéneas

    Altas frequências representam:

    - contornos
    - ruído
    - detalhes finos

    O espectro de magnitude mostra
    essa distribuição de frequências.
            """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_fft(),
                language="text"
            )

        # ---------------------------------
        # Filtro Passa-Baixo FFT
        # ---------------------------------
        elif operacao == "Filtro Passa-Baixo FFT":

            st.write("### Explicação Teórica")

            st.write("""
    O filtro passa-baixo no domínio da frequência
    mantém apenas as baixas frequências da imagem.

    Isso significa:

    - suavização
    - redução de ruído
    - remoção de detalhes finos
    - diminuição de contornos

    O processo funciona assim:

    1. Aplicar FFT

    2. Criar máscara circular

    3. Manter apenas o centro
    (baixas frequências)

    4. Aplicar FFT inversa

    O resultado é semelhante
    a um filtro espacial de suavização.
        """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_low_pass_fft(),
                language="text"
            )

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            radius = st.sidebar.slider(
                "Raio do Filtro",
                5,
                100,
                30
            )

            img_result = low_pass_filter_fft(
                img_gray,
                radius
            )

            st.write("### Resultado")

            col_a, col_b = st.columns(2)

            with col_a:
                st.image(
                    img_gray,
                    use_container_width=True,
                    caption="Imagem Original"
                )

            with col_b:
                st.image(
                    img_result,
                    use_container_width=True,
                    caption=f"Filtro Passa-Baixo FFT (Raio = {radius})"
                )

            image_bytes = convert_numpy_to_downloadable_image(
               img_result
            )

            st.download_button(
                label="Download do Filtro Passa-Baixo",
                data=image_bytes,
                file_name="low_pass_fft.png",
                mime="image/png"
            )

        # ---------------------------------
        # Filtro Passa-Alto FFT
        # ---------------------------------
        elif operacao == "Filtro Passa-Alto FFT":

            st.write("### Explicação Teórica")

            st.write("""
    O filtro passa-alto no domínio da frequência
    remove as baixas frequências da imagem
    e mantém apenas as altas frequências.

    Isso permite:

    - realçar contornos
    - destacar detalhes finos
    - reforçar estruturas pequenas
    - evidenciar variações bruscas

    O processo funciona assim:

    1. Aplicar FFT

    2. Criar máscara circular

    3. Remover o centro
    (baixas frequências)

    4. Aplicar FFT inversa

    O resultado é semelhante a uma deteção
    de contornos no domínio da frequência.
        """)

            st.write("### Pseudocódigo")

            st.code(
                pseudo_high_pass_fft(),
                language="text"
            )

            # Converter para grayscale se necessário
            if is_rgb:
                img_gray = rgb_to_gray_manual(img_array)
            else:
                img_gray = img_array.copy()

            radius = st.sidebar.slider(
                "Raio da Região Removida",
                5,
                100,
                30
            )

            img_result = high_pass_filter_fft(
                img_gray,
                radius
            )

            st.write("### Resultado")

            col_a, col_b = st.columns(2)

            with col_a:
                st.image(
                    img_gray,
                    use_container_width=True,
                    caption="Imagem Original"
                )

            with col_b:
                st.image(
                    img_result,
                    use_container_width=True,
                    caption=f"Filtro Passa-Alto FFT (Raio = {radius})"
                )
            image_bytes = convert_numpy_to_downloadable_image(
               img_result
            )

            st.download_button(
                label="Download do Filtro Passa-Alto",
                data=image_bytes,
                file_name="high_pass_fft.png",
                mime="image/png"
            )    

