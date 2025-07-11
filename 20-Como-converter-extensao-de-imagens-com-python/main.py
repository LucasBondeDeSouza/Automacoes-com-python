from PIL import Image
import os

lista_arquivos = os.listdir("imagens")

for arquivo in lista_arquivos:
    # Abrir arquivo
    imagem = Image.open(f"imagens/{arquivo}").convert("RGB")

    # Salvar o arquivo com outro formato
    imagem.save(f'pdf/{arquivo.replace("png", "pdf")}')