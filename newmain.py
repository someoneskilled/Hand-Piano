import cv2
import pygame.midi
from cvzone.HandTrackingModule import HandDetector

# Initialize Pygame MIDI
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)  # Acoustic Grand Piano

# Initialize Hand Detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)

# Piano Scale (G, D, C, F, Am)
chord_list = [
    ("G Major", [67, 71, 74]),
    ("D Major", [62, 66, 69]),
    ("C Major", [60, 64, 67]),
    ("F Major", [65, 69, 72]),
    ("A Minor", [69, 72, 76])
]

num_chords = len(chord_list)
current_chord_index = -1
is_playing = False

while True:
    success, img = cap.read()
    if not success:
        print("❌ Camera not capturing frames")
        continue

    img = cv2.flip(img, 1)  # Mirror the image
    h, w, _ = img.shape

    # Draw Chord Zones
    band_height = h // num_chords
    for i, (name, _) in enumerate(chord_list):
        y = i * band_height
        color = (200, 200, 200)
        thickness = 2

        if i == current_chord_index and is_playing:
            color = (0, 255, 0)
            thickness = -1
            cv2.putText(img, name, (w - 200, y + band_height // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        else:
            cv2.putText(img, name, (w - 200, y + band_height // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.rectangle(img, (w - 220, y), (w - 20, y + band_height), color, thickness)

    # Detect Hand
    hands, img = detector.findHands(img, draw=True)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        is_open = sum(fingers) >= 4  # Open palm
        is_fist = sum(fingers) == 0  # Fist

        cx, cy = hand["center"][:2]
        band_index = int(cy / band_height)
        band_index = max(0, min(band_index, num_chords - 1))

        if is_open:
            if not is_playing or band_index != current_chord_index:
                if is_playing:
                    player.note_off(0, 127)  # Stop previous note
                player.note_off(0, 127)
                player.note_off(0, 127)
                player.note_off(0, 127)
                player.note_off(0, 127)
                for note in chord_list[band_index][1]:
                    player.note_on(note, 127)
                is_playing = True
                current_chord_index = band_index
        elif is_fist and is_playing:
            for note in chord_list[current_chord_index][1]:
                player.note_off(note, 127)
            is_playing = False

    else:
        if is_playing:
            for note in chord_list[current_chord_index][1]:
                player.note_off(note, 127)
            is_playing = False

    cv2.imshow("Fist Controlled Piano", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.midi.quit()