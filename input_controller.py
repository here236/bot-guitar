import keyboard

TECLAS = ["a", "s", "j", "k", "l"]

columnState = [False, False, False, False, False]

def play(colunas):

    global columnState

    for i in range(len(TECLAS)):

        if i in colunas:

            if not columnState[i]:
                keyboard.press_and_release(TECLAS[i])
                columnState[i] = True


        else:
            columnState[i] = False
    