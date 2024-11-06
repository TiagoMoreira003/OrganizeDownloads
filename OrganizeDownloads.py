import os
import shutil

path = r"C:\Users\ALEXA\Downloads"

pathPhotos = r"C:\Users\ALEXA\OneDrive\Ambiente de Trabalho\Fotos"
pathBooks = r"C:\Users\ALEXA\OneDrive\Ambiente de Trabalho\Livros"
pathAudios = r"C:\Users\ALEXA\OnoDrive\Ambiente de Trabalho\Audio"

for file in os.listdir(path):
    if file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".jpg"):
        source = os.path.join(path, file)
        if os.path.exists(pathPhotos) is False :
            os.makedirs (pathPhotos)
            print(f"Criada pasta fotos!")
        shutil.move(source, pathPhotos)
        print(f"Movido: {file}")
    
    if file.endswith(".epub"):
        source = os.path.join(path, file)
        if os.path.exists(pathBooks) is False :
            os.makedirs(pathBooks) 
            print(f"Criada pasta Livros!")
        shutil.move(source, pathBooks)
        print(f"Movido: {file}")
    
    if file.endswith(".mp3"):
        source = os.path.join(path, file)
        if os.path.exists(pathAudios) is False :
            os.makedirs(pathAudios)
            print(f"Criada pasta Audios!")
        shutil.move(source, pathAudios)
        print(f"Movido: {file}")
