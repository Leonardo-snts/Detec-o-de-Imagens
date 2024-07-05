import dlib
import cv2

# Carregar uma imagem de teste
image = cv2.imread("C:/Users/leona/projetos/camera/foto3.jpg")
if image is None:
    print("Erro: Não foi possível carregar a imagem.")
    exit()

# Converter a imagem para RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Criar um detector de rostos
detector = dlib.get_frontal_face_detector()
#detector = image.astype('uint8')

# Detectar rostos na imagem RGB
try:
    detections = detector(rgb_image, 1)
    print(f"Número de rostos detectados: {len(detections)}")

    # Desenhar retângulos nos rostos detectados
    for detection in detections:
        x1, y1, x2, y2 = (detection.left(), detection.top(), detection.right(), detection.bottom())
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

except Exception as e:
    print(f"Erro na detecção de rostos: {e}")

# Mostrar a imagem resultante para visualização
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
