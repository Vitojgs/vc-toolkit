import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="VC Toolkit - IPCA", layout="wide")

st.title("🛠️ Visão por Computador - Toolkit de Funções")
st.write("Projeto desenvolvido para testar os algoritmos lecionados na disciplina.")

# 1. Upload da Imagem
uploaded_file = st.file_uploader("Faça upload da imagem (.ppm, .pgm, .jpg, .png)", type=["ppm", "pgm", "jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Ler a imagem com PIL e converter para array NumPy
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    # Garantir que temos a imagem original guardada (para processamentos em RGB)
    is_rgb = len(img_array.shape) == 3
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Imagem Original")
        st.image(image, use_column_width=True)
        st.write(f"Dimensões (Altura, Largura, Canais): {img_array.shape}")
        if is_rgb:
            st.write("Formato: RGB")
        else:
            st.write("Formato: Tons de Cinzento (Grayscale)")

    # 2. Seleção da Categoria e Função
    st.sidebar.header("Menu de Operações")
    categoria = st.sidebar.selectbox(
        "Selecione a Categoria:",
        ("1. Espaços de Cor", 
         "2. Segmentação e Binarização", 
         "3. Operadores Morfológicos", 
         "4. Filtros Espaciais (Passa-Baixo)",
         "5. Deteção de Contornos e Passa-Alto",
         "6. Histogramas",
         "7. Blobs e Etiquetagem")
    )
    
    with col2:
        st.header("Imagem Processada")
        
        # ---------------------------------------------------------
        # 1. ESPAÇOS DE COR
        # ---------------------------------------------------------
        if categoria == "1. Espaços de Cor":
            op_cor = st.sidebar.radio("Função:", ["Negativo", "Extrair Canal Vermelho", "RGB para Cinzento", "RGB para HSV e Máscara"])
            
            if op_cor == "Negativo":
                img_result = 255 - img_array
                st.image(img_result, use_column_width=True)
                
            elif op_cor == "Extrair Canal Vermelho":
                if is_rgb:
                    img_result = img_array.copy()
                    img_result[:, :, 1] = 0 # Zera Verde
                    img_result[:, :, 2] = 0 # Zera Azul
                    st.image(img_result, use_column_width=True)
                else:
                    st.warning("A imagem não é RGB.")
                    
            elif op_cor == "RGB para Cinzento":
                if is_rgb:
                    # Fórmula clássica: 0.299*R + 0.587*G + 0.114*B
                    img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                    st.image(img_gray, cmap="gray", use_column_width=True)
                else:
                    st.warning("A imagem já está em tons de cinzento.")
                    
            elif op_cor == "RGB para HSV e Máscara":
                if is_rgb:
                    img_hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
                    st.write("Ajuste os valores para segmentar uma cor:")
                    h_min = st.sidebar.slider("Hue Min", 0, 179, 0)
                    h_max = st.sidebar.slider("Hue Max", 0, 179, 179)
                    
                    lower_bound = np.array([h_min, 50, 50])
                    upper_bound = np.array([h_max, 255, 255])
                    mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
                    st.image(mask, cmap="gray", use_column_width=True, caption="Máscara de Segmentação HSV")
                else:
                    st.warning("Necessita de uma imagem RGB para converter para HSV.")

        # ---------------------------------------------------------
        # 2. SEGMENTAÇÃO E BINARIZAÇÃO
        # ---------------------------------------------------------
        elif categoria == "2. Segmentação e Binarização":
            op_bin = st.sidebar.radio("Função:", ["Threshold Manual", "Média Global"])
            
            # Converter para gray se for RGB
            img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if is_rgb else img_array.copy()
            
            if op_bin == "Threshold Manual":
                limiar = st.sidebar.slider("Valor do Threshold", 0, 255, 128)
                _, img_bin = cv2.threshold(img_gray, limiar, 255, cv2.THRESH_BINARY)
                st.image(img_bin, cmap="gray", use_column_width=True)
                
            elif op_bin == "Média Global":
                media = int(np.mean(img_gray))
                st.write(f"Média calculada da imagem: **{media}**")
                _, img_bin = cv2.threshold(img_gray, media, 255, cv2.THRESH_BINARY)
                st.image(img_bin, cmap="gray", use_column_width=True)

        # ---------------------------------------------------------
        # 3. OPERADORES MORFOLÓGICOS
        # ---------------------------------------------------------
        elif categoria == "3. Operadores Morfológicos":
            op_morf = st.sidebar.radio("Função:", ["Dilatação", "Erosão", "Abertura (Open)", "Fecho (Close)"])
            kernel_size = st.sidebar.slider("Tamanho do Kernel", 3, 15, 3, step=2)
            
            kernel = np.ones((kernel_size, kernel_size), np.uint8)
            img_work = img_array.copy()
            
            if op_morf == "Dilatação":
                img_result = cv2.dilate(img_work, kernel, iterations=1)
            elif op_morf == "Erosão":
                img_result = cv2.erode(img_work, kernel, iterations=1)
            elif op_morf == "Abertura (Open)": # Erosão seguida de Dilatação (Remove ruído fora)
                img_result = cv2.morphologyEx(img_work, cv2.MORPH_OPEN, kernel)
            elif op_morf == "Fecho (Close)":   # Dilatação seguida de Erosão (Fecha buracos dentro)
                img_result = cv2.morphologyEx(img_work, cv2.MORPH_CLOSE, kernel)
                
            st.image(img_result, use_column_width=True, caption=f"{op_morf} com Kernel {kernel_size}x{kernel_size}")

        # ---------------------------------------------------------
        # 4. FILTROS ESPACIAIS (PASSA-BAIXO)
        # ---------------------------------------------------------
        elif categoria == "4. Filtros Espaciais (Passa-Baixo)":
            op_filtro = st.sidebar.radio("Filtro:", ["Média", "Mediana (Remove Ruído Sal e Pimenta)", "Gaussiano"])
            k = st.sidebar.slider("Tamanho do Kernel", 3, 15, 5, step=2)
            
            if op_filtro == "Média":
                img_result = cv2.blur(img_array, (k, k))
            elif op_filtro == "Mediana (Remove Ruído Sal e Pimenta)":
                img_result = cv2.medianBlur(img_array, k)
            elif op_filtro == "Gaussiano":
                img_result = cv2.GaussianBlur(img_array, (k, k), 0)
                
            st.image(img_result, use_column_width=True)

        # ---------------------------------------------------------
        # 5. DETEÇÃO DE CONTORNOS (PASSA-ALTO)
        # ---------------------------------------------------------
        elif categoria == "5. Deteção de Contornos e Passa-Alto":
            op_edge = st.sidebar.radio("Operador:", ["Sobel", "Prewitt", "Laplaciano"])
            img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if is_rgb else img_array.copy()
            
            if op_edge == "Sobel":
                sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
                sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
                sobel_mag = np.sqrt(sobelx**2 + sobely**2)
                sobel_mag = np.uint8(255 * sobel_mag / np.max(sobel_mag))
                st.image(sobel_mag, cmap="gray", use_column_width=True)
                
            elif op_edge == "Prewitt":
                kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
                kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
                prewittx = cv2.filter2D(img_gray, -1, kernelx)
                prewitty = cv2.filter2D(img_gray, -1, kernely)
                prewitt_mag = cv2.addWeighted(prewittx, 0.5, prewitty, 0.5, 0)
                st.image(prewitt_mag, cmap="gray", use_column_width=True)
                
            elif op_edge == "Laplaciano":
                laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
                laplacian = np.uint8(np.absolute(laplacian))
                st.image(laplacian, cmap="gray", use_column_width=True)

        # ---------------------------------------------------------
        # 6. HISTOGRAMAS
        # ---------------------------------------------------------
        elif categoria == "6. Histogramas":
            op_hist = st.sidebar.radio("Função:", ["Visualizar Histograma", "Equalização de Histograma"])
            img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if is_rgb else img_array.copy()
            
            if op_hist == "Visualizar Histograma":
                st.write("Histograma de Tons de Cinzento:")
                fig, ax = plt.subplots()
                ax.hist(img_gray.ravel(), 256, [0, 256], color='black')
                ax.set_xlabel('Intensidade de Píxeis')
                ax.set_ylabel('Quantidade')
                st.pyplot(fig)
                st.image(img_gray, cmap="gray", use_column_width=True)
                
            elif op_hist == "Equalização de Histograma":
                img_eq = cv2.equalizeHist(img_gray)
                st.image(img_eq, cmap="gray", caption="Imagem Equalizada", use_column_width=True)
                
                st.write("Novo Histograma (Equalizado):")
                fig, ax = plt.subplots()
                ax.hist(img_eq.ravel(), 256, [0, 256], color='blue')
                st.pyplot(fig)

        # ---------------------------------------------------------
        # 7. BLOBS E ETIQUETAGEM
        # ---------------------------------------------------------
        elif categoria == "7. Blobs e Etiquetagem":
            st.write("Para encontrar Blobs (componentes conectados), primeiro binarizamos a imagem.")
            limiar = st.sidebar.slider("Threshold para Binarizar", 0, 255, 128)
            img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if is_rgb else img_array.copy()
            _, img_bin = cv2.threshold(img_gray, limiar, 255, cv2.THRESH_BINARY)
            
            # Etiquetagem (Blob Labelling)
            num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin, connectivity=8)
            
            # Criar uma imagem colorida para mostrar os blobs
            img_colorida = np.zeros((img_bin.shape[0], img_bin.shape[1], 3), dtype=np.uint8)
            
            # O blob 0 é sempre o fundo. Atribuímos cores aleatórias aos restantes.
            for i in range(1, num_labels):
                cor = np.random.randint(0, 255, size=3).tolist()
                img_colorida[labels == i] = cor
                
            st.image(img_colorida, use_column_width=True, caption=f"Foram detetados {num_labels - 1} Blobs.")
            st.write("*(Nota: Cada cor representa um blob/objeto distinto)*")
