from random import choice
from time import sleep

import pyautogui
from PIL import Image


class Auto_UP:
    def auto_up(self):
        print(pyautogui.getAllTitles())
        pyautogui.getWindowsWithTitle("РokеММO")[0].activate()
        while 1 == 1:
            self._battle_mode()
            self._random_moviments()

    def _battle_mode(self):
        in_battle = pyautogui.locateOnScreen(Image.open("battleon.png"), confidence=0.9)
        while in_battle != None:
            self._default_battle_position()
            sleep(1)
            self._battle_move(range(1, 4))
            in_battle = pyautogui.locateOnScreen(
                Image.open("battleon.png"), confidence=0.9
            )

    def _random_moviments(self):
        moviment = ["w", "s", "a", "d"]
        pyautogui.keyDown(choice(moviment))
        sleep(1)
        pyautogui.keyUp(choice(moviment))
        pyautogui.press(moviment)

    def _battle_move(self, random_move: range):
        move = choice(random_move)
        if move == 1:
            pyautogui.press(["a", "w"])
        elif move == 2:
            pyautogui.press(["d", "w"])
        elif move == 3:
            pyautogui.press(["a", "s"])
        elif move == 4:
            pyautogui.press(["s", "d"])

        pyautogui.press(["z", "z"])

    def _default_battle_position(self):
        pyautogui.press(["a", "w"])
        pyautogui.press(["a", "w"])
        pyautogui.press("z")
