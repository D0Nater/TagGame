# -*- coding: utf-8 -*-

from Scripts.var_storage import *
from config import *


class GameMenu:
    def __init__(self):
        pass

    def draw_menu(self):
        try: Main.GAME_TIMER.default_time()
        except: pass

        Main.MAIN_CANVAS.delete("all")

        Main.MAIN_CANVAS.create_window(window_width/2, window_height/2-100, window=Button(text="Играть", width=6, height=2, bd=0, font="Verdana 12", \
            command=lambda: Main.GAME_CANVAS.start_game()))
