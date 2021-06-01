from PIL import Image 
from mtcnn.mtcnn import MTCNN
import cv2
from tensorflow.keras.models import load_model
from os import listdir
from os import system
from os import isdir
from numpy import asarray
system('cls')

detector = MTCNN()

def extrair_face(arquivo, size= (160, 160)):

    img = image.open(arquivo)

    img = img.convert('RGB')
    array = asarray(img)
    results = detector.detec_faces(array)
    x1, y1, width, heigth = results[0]['box']
    x2 = x1 + width
    y2 = y1 + heigth
    face = array[y1:y2 , x1:x2]
    image = Image.fromarray(face)
    image = image.rezsize(size)

    return image

def load_fotos(directory_src, directory_target ):
    print(directory_src)
    print(directory_target)
    
    for filename in listdir(directory_src):
        path = directory_src + filename
        path_tg = directory_target + filename

        try:
          face = extrair_face(path)
          face.save(path_tg, 'JPEG', quality= 100, optmize=True, progressive=True)
        except:
            print('Erro na imagem {}'.format(path))

def load_dir(directory_src, directory_target):
    for subdir in listdir(directory_src):
        path = directory_src + subdir + '\\'

        path = directory_target + subdir + '\\'

        if  not isdir(path):
            continue

        load_fotos(path, path, path_tg)
if __name__ == '__main__':
    load_dir('C:\\Users\\Tata\\Pictures\\fotos',
              'C:\\Users\\Tata\\Pictures\\faces')