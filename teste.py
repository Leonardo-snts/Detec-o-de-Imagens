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

    # Verifique se a imagem foi capturada corretamente
    if frame is None or frame.size == 0:
        print("Erro: Frame vazio.")
        continue

    # Debug: Exibir informações sobre o frame capturado
    print("Frame capturado:", frame.shape, frame.dtype)

    # Converta a imagem de BGR (OpenCV) para RGB (face_recognition)
    try:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"Erro na conversão de BGR para RGB: {e}")
        continue

    # Verifique se a conversão foi bem-sucedida
    if rgb_frame is None or rgb_frame.size == 0:
        print("Erro: Falha na conversão para RGB.")
        continue

    # Debug: Exibir informações sobre o frame convertido
    print("Frame convertido:", rgb_frame.shape, rgb_frame.dtype)

    # Verifique o tipo de imagem antes de detectar os rostos
    if rgb_frame.dtype != 'uint8':
        print("Erro: A imagem não é do tipo uint8.")
        continue

    # Verifique se a imagem é RGB (3 canais)
    if rgb_frame.shape[2] != 3:
        print("Erro: A imagem não é RGB (3 canais).")
        continue

    # Encontre todos os rostos na imagem
    try:
        face_locations = face_recognition.face_locations(rgb_frame, model='hog')
    except Exception as e:
        print(f"Erro na detecção de rostos: {e}")
        continue

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