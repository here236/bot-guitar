import cv2
import numpy as np
import mss

GAME_REGION = {
    "top": 170,
    "left": 560,
    "width": 320,
    "height": 550
}

NUM_COLUNAS = 5

def main():
    with mss.mss() as sct:
        while True:
            # Captura tela
            screenshot = sct.grab(GAME_REGION)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            altura, largura, _ = frame.shape
            HIT_LINE_Y = int(altura * 0.92)
            largura_coluna = largura // NUM_COLUNAS

            # Desenha linha de hit
            cv2.line(frame, (0, HIT_LINE_Y), (largura, HIT_LINE_Y), (0, 0, 255), 2)

            for i in range(NUM_COLUNAS):
                # Define faixa horizontal na coluna
                x_inicio = i * largura_coluna
                x_fim = x_inicio + largura_coluna

                # Faixa vertical pequena na linha de hit
                y_inicio = HIT_LINE_Y - 4
                y_fim = HIT_LINE_Y + 4

                if y_inicio < 0 or y_fim >= altura:
                    continue

                area = frame[y_inicio:y_fim, x_inicio:x_fim]

                # Converte para HSV
                area_hsv = cv2.cvtColor(area, cv2.COLOR_BGR2HSV)

                #mascara para verde (range inicial teste)
                verde_mask = cv2.inRange(
                    area_hsv,
                    (40, 150, 150), #limite inferior do hsv 
                    (85, 255, 255)  #limite superior do hsv 
                )

                quantidade_verde = cv2.countNonZero(verde_mask)

                print(f"coluna {i} - pixels verdes:", quantidade_verde)

                # Exemplo: detectar verde
                if quantidade_verde > 50:
                    print(f"🟢 Nota VERDE detectada na coluna {i}")

            cv2.imshow("Guitar Bot Vision", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()