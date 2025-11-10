import cv2
import time
try:
    # Haupt-Klasse aus der Bibliothek importieren
    from pykinect_azure.kinect_azure import KinectAzure
    print("Bibliothek pykinect_azure erfolgreich geladen.")
except ImportError:
    print("FEHLER: Konnte pykinect_azure nicht importieren.")
    print("Stellt sicher, dass es mit 'pip install pykinectazure' installiert ist.")
    exit()
except Exception as e:
    print(f"FEHLER beim Importieren: {e}")
    print("Stellt sicher, dass die Microsoft C++ Redistributables (Teil des SDKs) installiert sind.")
    exit()

# --- Haupt-Test ---
kinect = None
try:
    # 1. Kinect-Objekt erstellen
    kinect = KinectAzure()

    # 2. Mit dem Gerät verbinden
    if not kinect.connect():
        print("Verbindung zur Azure Kinect DK fehlgeschlagen.")
        print("Ist sie angeschlossen (Strom + USB) und sind die Microsoft SDKs installiert?")
        exit()

    print("Kinect erfolgreich verbunden!")

    # Kleine Wartezeit, damit die Kamera stabil läuft
    time.sleep(1)

    while True:
        # 3. Einen Frame abrufen (nur Farbbild für diesen Test)
        ret, color_image = kinect.get_color_image()

        if not ret:
            print("Warte auf Frame...")
            continue

        # 4. Frame in einem Fenster anzeigen
        cv2.imshow("Kinect Test (pyKinectAzure) - 'q' zum Beenden", color_image)

        # 5. Schleife beenden, wenn 'q' gedrückt wird
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Ein Fehler im Haupt-Loop ist aufgetreten: {e}")
finally:
    # 6. Aufräumen
    if kinect and kinect.is_connected():
        kinect.disconnect()
        print("Kamera getrennt.")
    cv2.destroyAllWindows()
    print("Fenster geschlossen.")
