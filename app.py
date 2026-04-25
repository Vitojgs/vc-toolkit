import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title="VC - Testador de Funções", layout="wide")

st.title("Visão por Computador - Teste de Funções")
st.write("Projeto para testar os algoritmos lecionados na disciplina.")

# 1. Upload da Imagem (Suporta as imagens da disciplina como ppm, pgm, jpg, png)
uploaded_file = st.file_uploader("Faça upload da imagem (.ppm, .pgm, .jpg, .png)", type=["ppm", "pgm", "jpg", "png", "jpeg"])

if uploaded_file is not None:
    # A biblioteca PIL consegue abrir ficheiros .ppm e .pgm facilmente
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Imagem Original")
        st.image(image, use_column_width=True)
        st.write(f"Dimensões: {img_array.shape}")

    # 2. Seleção da Função a testar
    st.sidebar.header("Operações")
    operacao = st.sidebar.selectbox(
        "Selecione a função:",
        ("1. Negativo", 
         "2. Extrair Canal Vermelho", 
         "3. RGB para Tons de Cinzento", 
         "4. Binarização Manual (Threshold)",
         "5. Filtro Média (Passa-baixo)",
         "6. Deteção de Contornos (Sobel)")
    )
    
    with col2:
        st.header("Imagem Processada")
        
        # --- AQUI IMPLEMENTA AS FUNÇÕES DA DISCIPLINA ---
        
        if operacao == "1. Negativo":
            # Exemplo de tradução do código C para Python/NumPy
            # C: image->data[i] = 255 - image->data[i]
            img_result = 255 - img_array
            st.image(img_result, use_column_width=True)
            
        elif operacao == "2. Extrair Canal Vermelho":
            # Exemplo de vc_rgb_get_red_gray
            if len(img_array.shape) == 3:
                img_result = img_array.copy()
                img_result[:, :, 1] = 0 # Zera Verde
                img_result[:, :, 2] = 0 # Zera Azul
                st.image(img_result, use_column_width=True)
            else:
                st.warning("A imagem não tem 3 canais (RGB).")
                
        elif operacao == "3. RGB para Tons de Cinzento":
            # Exemplo de conversão matemática manual conforme os slides:
            # Gray = R * 0.299 + G * 0.587 + B * 0.114
            if len(img_array.shape) == 3:
                R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
                img_gray = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)
                st.image(img_gray, cmap="gray", use_column_width=True)
            else:
                st.warning("A imagem já está em tons de cinzento.")
                
        elif operacao == "4. Binarização Manual (Threshold)":
            limiar = st.sidebar.slider("Valor do Threshold", 0, 255, 128)
            # Converte primeiro para gray se for RGB
            if len(img_array.shape) == 3:
                img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            else:
                img_gray = img_array
            
            # Aplica Binarização (vc_gray_to_binary)
            _, img_bin = cv2.threshold(img_gray, limiar, 255, cv2.THRESH_BINARY)
            st.image(img_bin, cmap="gray", use_column_width=True)
            
        # Adicione aqui os "elif" para as restantes funções...
