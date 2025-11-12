import cv2
import numpy as np
import time

# WICHTIG: Passe den Index an, der bei dir funktioniert (wahrscheinlich 1 oder 2)
# Verwende cv2.CAP_DSHOW für Windows-Stabilität, falls nötig.
WEBCAM_INDEX = 1
try:
    # Versuche, das stabilere DSHOW-Backend für Windows zu nutzen
    CAP = cv2.VideoCapture(WEBCAM_INDEX, cv2.CAP_DSHOW)
except:
    # Fallback, falls DSHOW nicht verfügbar ist
    CAP = cv2.VideoCapture(WEBCAM_INDEX)

if not CAP.isOpened():
    print(f"Fehler: Kamera mit Index {WEBCAM_INDEX} konnte nicht geöffnet werden. Bitte Index prüfen!")

# Globale Variable, um den letzten Frame für die Bewegungsdetektion zu speichern
last_gray_frame = None

# Wartezeit vor der ersten Speicherung des Frames (damit sich die Kamera stabilisiert)
initial_wait_time = 0.5
time.sleep(initial_wait_time)


def get_touched_tiles(current_frame, tile_mapping):
    """
    Verarbeitet den aktuellen Kamerabild (current_frame) und prüft,
    welche Kacheln (definiert in tile_mapping) betreten wurden.
    """
    global last_gray_frame

    # 1. Bildvorverarbeitung
    gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # 2. Initialisiere den letzten Frame
    if last_gray_frame is None:
        last_gray_frame = gray_frame.copy()
        return []

    # 3. Bewegungsdetektion durch Frame-Differenz
    # Da sich das Spiel ändert, nutzen wir die Differenz zum VORHERIGEN Frame
    frame_delta = cv2.absdiff(last_gray_frame, gray_frame)

    # 4. Binärisierung (Helligkeitsunterschiede über Schwellenwert 30 werden weiß)
    # THRESHOLD (z.B. 30) muss eventuell angepasst werden!
    thresh_value = 30
    thresh = cv2.threshold(frame_delta, thresh_value, 255, cv2.THRESH_BINARY)[1]

    # 5. Rauschen entfernen (Dilatation)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # 6. Konturen (Bewegungsbereiche) finden
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    active_tiles = set()

    # 7. Konturen prüfen und Kacheln zuordnen
    for contour in contours:
        # Ignoriere Bewegungen unter einer gewissen Größe (Rauschen)
        # AREA_THRESHOLD (z.B. 1500) muss eventuell angepasst werden!
        AREA_THRESHOLD = 1500
        if cv2.contourArea(contour) < AREA_THRESHOLD:
            continue

        # Finde den Mittelpunkt der Bewegung
        (x, y, w, h) = cv2.boundingRect(contour)
        center_x = x + w // 2
        center_y = y + h // 2

        # Prüfe, welche Kachel vom Mittelpunkt betroffen ist
        for tile_obj, coords in tile_mapping.items():
            x_min, y_min, x_max, y_max = coords

            # WICHTIG: Die Webcam-Frames müssen auf die Pygame-Koordinaten skaliert werden,
            # falls die Auflösungen nicht übereinstimmen. Da wir die Auflösung nicht kennen,
            # gehen wir von 1:1 Matching aus.

            if x_min <= center_x <= x_max and y_min <= center_y <= y_max:
                active_tiles.add(tile_obj)

    # 8. Speichere den aktuellen Frame für die nächste Iteration
    last_gray_frame = gray_frame.copy()

    return list(active_tiles)