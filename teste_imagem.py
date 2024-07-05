import cv2
import face_recognition

# Carregar uma imagem de teste
image = cv2.imread("C:/Users/leona/projetos/camera/foto.png")
if image is None:
    print("Erro: Não foi possível carregar a imagem.")
    exit()

# Converta a imagem de BGR (OpenCV) para RGB (face_recognition)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Encontre todos os rostos na imagem
try:
    face_locations = face_recognition.face_locations(rgb_image, model='hog')
except Exception as e:
    print(f"Erro na detecção de rostos: {e}")
    exit()

# Desenhe retângulos ao redor dos rostos
for top, right, bottom, left in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Mostre a imagem resultante
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
