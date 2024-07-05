import cv2
import face_recognition

# Inicialize a câmera
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Erro: Não foi possível acessar a câmera.")
    exit()

while True:
    # Capture um único frame do vídeo
    ret, frame = video_capture.read()

    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break

    # Converta a imagem de BGR (OpenCV) para RGB (face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Encontre todos os rostos na imagem
    face_locations = face_recognition.face_locations(rgb_frame)

    # Desenhe retângulos ao redor dos rostos
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Mostre o frame resultante
    cv2.imshow('Video', frame)

    # Saia do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a câmera e feche as janelas
video_capture.release()
cv2.destroyAllWindows()
