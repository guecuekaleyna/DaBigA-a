import cv2
import numpy as np
import time

WEBCAM_INDEX = 1
try:
    CAP = cv2.VideoCapture(WEBCAM_INDEX, cv2.CAP_DSHOW)
except:
    CAP = cv2.VideoCapture(WEBCAM_INDEX)

if not CAP.isOpened():
    print(f"fehler: Kamera mit Index {}")

print("Webcam-Stream gestartet. Drücke 'q', um das Fenster zu schließen.")

while True:
    # Lese Frame für Frame
    ret, frame = cap.read()

    # Wenn der Frame korrekt gelesen wurde (ret ist True)
    if not ret:
        print("Kann keinen Frame empfangen (Stream-Ende?).")
        break

    # Zeige den Frame in einem Fenster an
    cv2.imshow('Webcam-Feed', frame)

    # Warte 1 Millisekunde. Wenn 'q' gedrückt wird, beende die Schleife.
    if cv2.waitKey(1) == ord('q'):
        break

# Gib die Kamera frei und schließe alle OpenCV-Fenster
cap.release()
cv2.destroyAllWindows()