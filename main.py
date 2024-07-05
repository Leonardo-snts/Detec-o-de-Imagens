import cv2

image_path = r'C:/Users/leona/projetos/camera/foto2.png'

# Carregar a imagem
try:
    frame = cv2.imread(image_path)
    if frame is None:
        raise FileNotFoundError(f"Erro ao carregar a imagem de {image_path}")
except Exception as e:
    print(f"Erro: {e}")
    exit()

# Converta a imagem de BGR (OpenCV) para RGB (face_recognition)
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Exemplo de utilização posterior
# face_locations = face_recognition.face_locations(rgb_frame)
# ...

# Mostrar a imagem
cv2.imshow('Imagem Carregada', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
