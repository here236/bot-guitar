import keyboard

TECLAS = ["a", "s", "j", "k", "l"]

def play(colunas):

    for coluna in colunas:
        tecla = TECLAS[coluna]
        keyboard.press_and_release(tecla)