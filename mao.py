import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
mpMaos = mp.solutions.hands
abc = mpMaos.Hands()
mpDesenho = mp.solutions.drawing_utils

while True:
    sucesso, imagem = camera.read()
    imagemRGB = cv2.cvtColor(imagem, cv2.COLOR_BayerBG2BGR)  # Correção da constante
    resultados = abc.process(imagemRGB)
    
    if resultados.multi_hand_landmarks:  # Correção do nome do atributo
        for maosPntRef in resultados.multi_hand_landmarks:
            mpDesenho.draw_landmarks(imagem, maosPntRef, mpMaos.HAND_CONNECTIONS)  # Correção do parâmetro

    cv2.imshow("Câmera", imagem)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
