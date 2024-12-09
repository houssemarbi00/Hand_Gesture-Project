import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands
#précisiant entre la detection et la position
hands = mp_hands.Hands(min_detection_confidence= 0.8,min_tracking_confidence=0.5,max_num_hands=2)

#choisir la camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    #apporter l'image
    ret, frame = cap.read()
    
    #convertir l'image de bgr au rgb
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    img = cv2.flip(img,1)
    
    results = hands.process(img)

    #convertir l'image de rgb au bgr
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks :
        for lmlist, hand in enumerate(results.multi_hand_landmarks) :
            mp_drawing.draw_landmarks(img ,hand ,mp_hands.HAND_CONNECTIONS ,mp_drawing.DrawingSpec(color=(121,22,76),thickness=2,circle_radius=4),
                                mp_drawing.DrawingSpec(color=(121,22,250),thickness=2,circle_radius=2))
        
    #afficher l'image
    cv2.imshow('Main',img)
    cv2.waitKey(1)
    
cap.release()
#detruire tous les fenetres
cv2.destroyAllWindows()    