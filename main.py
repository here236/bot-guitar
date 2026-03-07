import time 
import cv2 
import numpy as np
import mss

from config import GAME_REGION  
from detector import detect_notes
from input_controller import play

def main():

    with mss.mss() as sct:

        while True:

            screenshot = sct.grab(GAME_REGION)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            altura, largura, _ = frame.shape
            HIT_LINE_Y = int(altura * 0.92)

            notes = detect_notes(frame, HIT_LINE_Y)

            if notes:
                print("Notas: ", notes)
                play(notes)

            
            cv2.imshow("Guitar Bot Vision", frame)

            #killswitch
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()