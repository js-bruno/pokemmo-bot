from genericpath import exists
from random import choice
from time import sleep

import pyautogui
from PIL import Image

# 1 - x=278, y=380
# 2 - x=531, y=483
# 3 - x=304, y=540
# 4 - x=529, y=539
class Auto_UP:  
    # TODO: PP CHECK
    # TODO: HP CHECK
    # TODO: NO EFFETIVE CHECK
    def auto_up(self):
        pyautogui.getWindowsWithTitle(title="РokeММO")[0].activate()
        sleep(2)
        while 1 == 1:
            self._battle_mode()
            self._random_moviments()

    def _battle_mode(self):
        in_battle = pyautogui.locateOnScreen(Image.open("battleon.png"), confidence=0.9)
        while in_battle != None:
            self._default_battle_position()
            sleep(1)
            exists_super_effetive= self._super_effetive_move()
            if not exists_super_effetive:
                self._battle_move([1,2,3,4])
            in_battle = pyautogui.locateOnScreen(
                Image.open("battleon.png"), confidence=0.9
            )

    def _random_moviments(self):
        moviment = ["w", "s", "a", "d"]
        pyautogui.keyDown(choice(moviment))
        sleep(1)
        pyautogui.keyUp(choice(moviment))
        pyautogui.press(moviment)

    def _battle_move(self, random_move: list):
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

    def _super_effetive_move(self) -> bool:
        super_effective_move = pyautogui.locateOnScreen(Image.open("supereffetive.png"), confidence=0.9)
        if super_effective_move != None:
            left_top_move = [super_effective_move.left, super_effective_move.top]
            pyautogui.click(left_top_move)
            return True
        return False
