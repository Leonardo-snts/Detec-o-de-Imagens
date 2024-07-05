import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4, 8)  # Ajustei o polegar para um índice e um polegar reais

while True:
    success, image = cap.read()
    if not success:
        continue

    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandmarks = results.multi_hand_landmarks

    if multiLandmarks:
        for handLms in multiLandmarks:
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            handList = []
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handList.append((cx, cy))

            upCont = 0
            for coord in finger_Coord:
                if handList[coord[0]][1] < handList[coord[1]][1]:
                    upCont += 1

            if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:  # Comparação para o polegar
                upCont += 1

            cv2.putText(image, str(upCont), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow("Contando", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
