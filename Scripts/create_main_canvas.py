# -*- coding: utf-8 -*-

from Scripts.var_storage import *
from config import *


class GameCanvas:
    def __init__(self):
        Main.MAIN_CANVAS = Canvas(Main.ROOT, width=window_width, height=main_canvas_height, bg="grey80", highlightthickness=0)
        Main.MAIN_CANVAS.pack()

    def start_game(self):
        Main.STAPS = 0

        Main.CREATE_MAP.create_new_game_map()

        Main.GAME_TIMER.default_time()
        Main.GAME_TIMER.start_timer()

    def win_game(self):
        Main.GAME_TIMER.stop_timer()

        Main.MAIN_CANVAS.delete("all")

        Main.MAIN_CANVAS.create_text(window_width/2, 50, text=f"Время: {Main.GAME_TIMER.finish_time_str}", font="Verdana 14")
        Main.MAIN_CANVAS.create_text(window_width/2, 100, text=f"Шагов: {Main.STAPS}", font="Verdana 14")
