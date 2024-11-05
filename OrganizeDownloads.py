import os
import shutil

path = r"C:\Users\ALEXA\Downloads"

for file in os.listdir(path):
    if file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".jpg"):
        source = os.path.join(path, file)
        shutil.move(source, r"C:\Users\ALEXA\OneDrive\Ambiente de Trabalho\Fotos")
        print(f"Movido: {file}")
    
    if file.endswith(".epub"):
        source = os.path.join(path, file)
        shutil.move(source, r"C:\Users\ALEXA\OneDrive\Ambiente de Trabalho\Livros")
        print(f"Movido: {file}")
    
    if file.endswith(".mp3"):
        source = os.path.join(path, file)
        shutil.move(source, r"C:\Users\ALEXA\OneDrive\Ambiente de Trabalho\Audio")
        print(f"Movido: {file}")
