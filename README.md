# 🎹 Gesture-Controlled Piano (Hand Tracking MIDI)

A **gesture-based piano** that lets you play chords using **hand movements**! 🖐️🎶  
Move your hand **up/down** to switch chords and use **open palm** to play, **closed fist** to stop.  

## ✨ Features  
- **Hand-Tracked Chord Control** – No buttons, just gestures!  
- **Smooth Transitions** – Move up/down to switch between chords.  
- **Easy Playability** – Open palm = Play 🎵 | Closed fist = Stop 🎵🚫  
- **MIDI Output** – Works with digital instruments and DAWs.  

## 🎵 Chords Used (Scale: G, D, C, F, Am)  
| Hand Position | Chord | Notes |
|--------------|------|-------|
| Top          | G Major  | G, B, D  |
| Upper-Mid    | D Major  | D, F#, A  |
| Middle       | C Major  | C, E, G  |
| Lower-Mid    | F Major  | F, A, C  |
| Bottom       | A Minor  | A, C, E  |

## 🛠️ Tech Stack  
- **Python**
- **OpenCV** (Hand Tracking)
- **cvzone** (Simplified Hand Detection)
- **pygame.midi** (MIDI Sound Output)

## 🚀 How to Run  
1. Install dependencies:  
   ```sh
   pip install opencv-python cvzone pygame
